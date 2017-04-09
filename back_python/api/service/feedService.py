from django.db import transaction
from django.db.models import Q
from django.contrib.auth.models import User
from org.models import Profile,MapEngToRole,Org
from school.models import ClassGroup
import datetime
from activity.models import Activity
from django.conf import settings
from feedback.models import OrgActivityHistory
from account.models import Account,AccountHistory,SysAccountHistory,SysAccount,MAP_TRADE_TYPE,MAP_ACCOUNT_TYPE,MAP_SYS_TRADE_TYPE
from habitinfo.models import Habit
from back.models import JsonResultService
from feedback.models import FeedBack,Post,Comment
import sys
import json
from django.core.cache import cache
import logging
logger = logging.getLogger("django")

# Create your views here.
class FeedbackService(JsonResultService):
    def orghabits(self,org,role,schema):
        jsonResult=self.initJsonResult()
        content={}
        data=[]
        logger.error("FeedbackService")
        try:
            with transaction.atomic():
                fstr=None
                if role=="4":
                    fstr="p0"
                else:
                    fstr="p1"
                # to do performance
                orgacthistorys=OrgActivityHistory.objects.filter(org__id__exact=org.id).filter(habits__contains=fstr).order_by("createdTime");
                for orgacthistory in orgacthistorys:
                    habitsArrayStr=orgacthistory.habits.split(",")
                    activity=orgacthistory.activity
                    for habitstr in habitsArrayStr:
                        habitstrArray=habitstr.split("|")
                        habittmp={}
                        habittmp["id"]=habitstrArray[0]
                        habittmp["name"]=habitstrArray[1]
                        habittmp["isForParent"]=habitstrArray[2]
                        habittmp["icon"]=habitstrArray[3]
                        habittmp["hid"]=orgacthistory.id
                        habittmp["isFeedBack"]="0"
                        # habittmp["actImg"]=schema+settings.MEDIA_URL+activity.img.img.name
                        if fstr==habittmp["isForParent"]:
                            data.append(habittmp)
                content["data"]=data
        except:
            info=sys.exc_info()
            logging.error(info)
            jsonResult.rtnDic["status"]=-1
        else:
            jsonResult.rtnDic["content"]=content
        finally:
            return jsonResult

    def create(self,pid,habitid,hid):
        jsonResult=self.initJsonResult()
        content={}
        logger.error("create")
        try:
            with transaction.atomic():
                # 创建反馈
                feedBack=FeedBack()
                # 查询出当前打卡用户,
                profileTmp=Profile.objects.get(pk=int(pid))
                feedBack.profile=profileTmp
                # 查询出当前活动历史,在创建活动历史的时候，建立缓存活动历史缓存,缓存时间是活动的时间
                acthistoryTmp=None
                # 活动历史缓存key
                acthistory_key=settings.CACHE_FORMAT_STR['acthistory_key'] % (int(hid))
                acthistoryTmp=cache.get(acthistory_key)
                if not acthistoryTmp:
                    acthistoryTmp=OrgActivityHistory.objects.get(pk=int(hid))
                    cache.set(acthistory_key,acthistoryTmp,acthistoryTmp.activityDays*24*3600)

                feedBack.orgActivityHistory=acthistoryTmp
                # 查询出当前打卡的习惯 to do 从缓存中取
                habitTmp=None
                habit_key=settings.CACHE_FORMAT_STR['habit_key'] % (int(habitid))
                habitTmp=cache.get(habit_key)
                if not habitTmp:
                    habitTmp=Habit.objects.get(pk=int(habitid))
                    cache.set(habit_key,habitTmp)
                feedBack.habit=habitTmp
                feedBack.save()
                #创建头贴
                post=Post()
                post.feedBack=feedBack
                post.save()
                # 初始化缓存　Key:打卡用户id+habitid+打卡日期 value:1-表示已经打卡，０表示未打卡
                logger.error("date format...........")
                logger.error(type(post.feedDate))
                dtmpstr=post.feedDate.strftime('%Y-%m-%d')
                logger.error(dtmpstr)
                userid_habitid_date_key=settings.CACHE_FORMAT_STR['userid_habitid_date_key'] % (int(pid),int(habitid),dtmpstr)
                cache.set(userid_habitid_date_key,1,settings.CACHE_FORMAT_STR['userid_habitid_date_key_timeout'])
                # 返回当前帖子
                # rtnPost=self.toJSON(post,["id"])
                content["postid"]=post.id
        except:
            info=sys.exc_info()
            logging.error(info)
            jsonResult.rtnDic["status"]=-1
        else:
            jsonResult.rtnDic["content"]=content
        finally:
            return jsonResult

feedbackService=FeedbackService()
