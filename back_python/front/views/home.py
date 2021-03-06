from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
import urllib.request

# Create your views here.
def index(request):
    return render(request,"front/index.html");

# 返回信任域名的文件,返回文件
class HomeWxAuthView(TemplateView):
    template_name="front/index.html"
    def get(self,*args,**kwargs):
        from django.http import FileResponse
        response = FileResponse(open(settings.STATIC_ROOT+'front/MP_verify_HAONGKquSEXIsxKN.txt', 'rb'))
        return response


class HomeMobileView(TemplateView):
    template_name="front/mobile.html"
    def get_context_data(self, **kwargs):
        ctx=super(HomeMobileView,self).get_context_data(**kwargs)
        hostRedirect=settings.WX['WX_APP_REDIRECT'].replace("{role}","host")
        teacherRedirect=settings.WX['WX_APP_REDIRECT'].replace("{role}","teacher")
        childRedirect=settings.WX['WX_APP_REDIRECT'].replace("{role}","child")


        ctx["host"]=settings.WX['WX_AUTH_URL_CODE'].replace("{redirect_uri}",urllib.parse.urlencode({'redirect_uri':hostRedirect}))
        ctx["teacher"]=settings.WX['WX_AUTH_URL_CODE'].replace("{redirect_uri}",urllib.parse.urlencode({'redirect_uri':teacherRedirect}))
        ctx["child"]=settings.WX['WX_AUTH_URL_CODE'].replace("{redirect_uri}",urllib.parse.urlencode({'redirect_uri':childRedirect}))
        return ctx
