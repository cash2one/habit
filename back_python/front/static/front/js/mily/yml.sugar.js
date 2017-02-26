/**
 * 工具对象，单例
 */
(function(window,$){
	$yml.sound=$yml.object.New({
		ctor:function(){
			//Preload the sound
			// auto, metadata, none
			buzz.defaults.preload = 'auto';
			// Play the sound when ready
			// bool
			buzz.defaults.autoplay = false;
			// Loop the sound
			// bool
			buzz.defaults.loop = false;
			// value to display when a time convertion is impossible
			buzz.defaults.placeholder = '--';
			// Duration of a fading effect
			// milliseconds
		  buzz.defaults.duration = 100;
			// Audio formats of your files
			//buzz.defaults.formats = ['amr','ogg', 'mp3', 'aac', 'wav'];
			var that=this;

			$(document).on("ready",function(){
         $("div.sound").click(function(){
					 that.openSound();
				 });
			});
			this.soundsArray=[];
			this.sound=new buzz.sound("/static/front/js/buzz/sounds/btnClick.mp3");
			this.isPlay=false;
		},
		openSound:function(){

    		this.sound.play();
		},
		groupPlay:function(audioUrls){
			var self=this;
			this.isPlay=true;
			this.soundsArray.length=0;

			var tmpArray=[];
			audioUrls.forEach(function(r){
				if(r.indexOf(".mp3")>-1){
					tmpArray.push(r);
				}
			});
      tmpArray.forEach(function(r){
				var sound=new buzz.sound(r);
				sound.setVolume(100);
				sound.load();
				self.soundsArray.push(sound);
				var me=self;
				sound.bind("ended",function(){
					sound=null;
					var soundTmp=me.soundsArray.shift();
					if(soundTmp){
						soundTmp.play();
					}else{
						me.isPlay=false;
					}
				});
				sound.bind("error",function(err){
					alert("error");
					me.isPlay=false;
				});
				sound.bind("sourceerror",function(){
					alert("sourceerror");
					me.isPlay=false;
				});
			});
			var firstsound=this.soundsArray.shift();
			firstsound.play();
		}
	});
	//分页对象，缓存当前页面
	$yml.pagination=$yml.object.Abstract({
		ctor:function(initParams){
			this.currentPage=initParams.currentPage;
			this.totalCount=initParams.totalCount;
			this.pageSize=initParams.pageSize;
			this.pcount=0;
			this.url=initParams.url;
			this.initTop=0;
			this.query=initParams.query;
			this.tmpDataRef=null;
			this.isQuerying=false;
		},
		initData:function(callback){
			this.nextPage(callback);
		},
		pageCount:function(){
			var intPage= Math.floor(this.totalCount/this.pageSize);
			console.log("this.totalCount"+this.totalCount);
			var other=this.totalCount%this.pageSize;
			if(other>0){
				this.pcount=intPage+1;
				return this.pcount;
			}else{
				this.pcount=intPage;
				return this.pcount;
			}
		},
		nextPage:function(cbk){
			if(!this.isQuerying){
				this.isQuerying=true;
				var pageCount= this.pageCount();
				console.log("page count....."+pageCount);
				if(this.currentPage+1<=pageCount)
						this.currentPage++;
				console.log(this.currentPage);
				var self=this;
				$yml.ajaxPageQuery(this.url,this,function(resData){
					//只要是返回了
					self.isQuerying=false;
					if(resData.status==0){
						if(resData.content){
							 self.totalCount=resData.content.total;
							 console.log(resData.content);
							 console.log("from query total"+self.totalCount);
							 if(self.tmpDataRef){
								 var len=self.tmpDataRef.length;
								 var lastDataRow=self.tmpDataRef[len-1];
								 if(resData.content.data && resData.content.data.length>0){
									 var len2=resData.content.data.length;
									 var rtnLastData=resData.content.data[len2-1];
									 if(lastDataRow.id==rtnLastData.id){
										 return cbk(null);
									 }else{
										 self.tmpDataRef=resData.content.data;
										 return cbk(resData.content.data);
									 }
								 }else{
										return cbk(null);
								 }
							 }else{
								 self.tmpDataRef=resData.content.data;
								 return cbk(resData.content.data);
							 }
						}else{
							 return cbk(null);
						}
					}else{
						return cbk(null);
					}
				});
			}

		},
		prevPage:function(cbk){
			var pageCount= this.pageCount();
			if(this.currentPage-1>=1)
			   this.currentPage--;

			var self=this;
 	    $yml.ajaxPageQuery(this.url,this,function(resData){
 					if(resData.status==0){
 						if(resData.content){
 							 self.totalCount=resData.content.total;
 							 return cbk(resData.content.data);
 						}else{
 							 return cbk(null);
 						}
 					}else{
 						return cbk(null);
 					}
 			});
		},
		onScroll:function(ele,cbk){
			var self=this;
			$("#"+ele).scroll(function(){
				var $this =$(this),
				viewH =$(this).height(),//可见高度
				contentH =$(this).get(0).scrollHeight,//内容高度
				scrollTop =$(this).scrollTop();//滚动高度
				//if(contentH - viewH - scrollTop <= 100) { //到达底部100px时,加载新内容
				if(scrollTop/(contentH -viewH)>=0.98 && scrollTop>self.initTop){ //到达底部100px时,加载新内容
				// 这里加载数据..
					self.nextPage(function(res){
						if(res){
								return cbk(res);
						}else{
							//	alert("目前没有数据");
								return cbk(null);
						}
						//$this.scrollTop(1);
					});
				    // setTimeout(function(){
						//
						// },500);
				}
			// 	if(scrollTop==0){
			// 		setTimeout(function(){
			// 			self.prevPage(function(res){
			// 				if(res){
			// 							return cbk(res);
			// 				}else{
			// 					//alert("目前没有数据");
			// 					return cbk(null);
			// 				}
			// 				//$this.scrollTop(100);
			// 			});
			// 		},500);
			//
			// 	}
			 	self.initTop=scrollTop;
			});
		},
		currentPage:function(){
			return this.currentPage;
		},
		getPageParam:function(){
			var rtn={};
			if(this.currentPage==1){
				rtn.skip=0;
				rtn.limit=this.pageSize;
				return rtn;
			}else{
				rtn.skip=(this.currentPage-1)*this.pageSize;
				rtn.limit=this.pageSize;
				return rtn;
			}
		}
	});
	$yml.ajax=function(url,paramJson,cbk){
		var paramObj=null;
		if(paramJson){
				  paramJson["ak"]=$.localStorage.get("accessKey");
					paramObj=paramJson;
		}
		else {
			paramObj={};
			paramObj["ak"]=$.localStorage.get("accessKey");
		}

			avalon.ajax({
				url: url,
				type: 'post',
				data: paramObj,
				dataType:'json'
			}).done(function(res){
				//var obj=JSON.parse(res);
					cbk(res);
			});

	};
	// $yml.ajax=function(url,paramJson,cbk){
	// 	var paramObj=null;
	// 	if(paramJson){
	// 			  paramJson["ak"]=$.localStorage.get("accessKey");
	// 				paramObj=paramJson;
	// 	}
	// 	else {
	// 		paramObj={};
	// 		paramObj["ak"]=$.localStorage.get("accessKey");
	// 	}
	// 	if(!paramJson.ignore){
	// 		wx.getNetworkType({
	// 				success: function (res) {
	// 						var networkType = res.networkType; // 返回网络类型2g，3g，4g，wifi
	// 						if(networkType!="fail"){
	// 							avalon.ajax({
	// 								url: url,
	// 								type: 'post',
	// 								data: paramObj,
	// 								dataType:'json'
	// 							}).done(function(res){
	// 								//var obj=JSON.parse(res);
	// 									cbk(res);
	// 							});
	// 						}else{
	// 							$yml.sysMsg("当前网络无法链接，请检查网络。")
	// 						}
	//
	// 				}
	// 		});
	// 	}else{
	// 		avalon.ajax({
	// 			url: url,
	// 			type: 'post',
	// 			data: paramObj,
	// 			dataType:'json'
	// 		}).done(function(res){
	// 			//var obj=JSON.parse(res);
	// 				cbk(res);
	// 		});
	// 	}
	// };
	$yml.ajaxPageQuery=function(url,pager,cbk){
		var paramObj=null;
		var paramJson=pager.query;
		if(paramJson){
					paramJson["ak"]=$.localStorage.get("accessKey");
					paramObj=paramJson;
					paramObj.pageParam=pager.getPageParam();
		}
		else {
			paramObj={};
			paramObj["ak"]=$.localStorage.get("accessKey");
			paramObj.pageParam=pager.getPageParam();
		}
		console.log(paramObj);
		avalon.ajax({
			url: url,
			type: 'post',
			data: paramObj,
			dataType:'json'
		}).done(function(res){
			//var obj=JSON.parse(res);
				cbk(res);
		});
	};
	$yml.icons={
		"life":"fa fa-sun-o sun",
		"honest":"fa fa-diamond diamond",
		"share":"fa fa-share-alt",
		"thank":"fa fa-birthday-cake thank",
		"read":"fa fa-book read",
    "readCOneHour":"fa fa-book read",
		"readChengyu":"fa fa-book read",
		"readEOneHour":"fa fa-book read",
		"readWord":"fa fa-book read",
		"pardon":"fa fa-child pardon",
		"resp":"fa fa-chain",
		"homework":"fa fa-clock-o",
		"promise":"fa fa-lock",
		"dabian":"fa fa-smile-o",
		"drink":"fa fa-coffee",
		"fruit":"fa fa-apple",
		"oldLook":"fa fa-wheelchair",
		"giftFriend":"fa fa-modx",
		"sport":"fa fa-bicycle",
		"word":"fa fa-paint-brush",
		"cubes":"fa fa-cubes","music":"fa fa-music","picture":"fa fa-picture-o",
		"fat":"fa fa-flash","daynote":"fa fa-edit",
		"plantKnow":"fa fa-tree","starKnow":"fa fa-cogs","childDance":"fa fa-child"
	};
	$yml.dlgCenter=function(dlgName){
		$("#"+dlgName).on('show.bs.modal', function(){
							var $this = $(this);
							var $modal_dialog = $this.find('.modal-dialog');
							// 关键代码，如没将modal设置为 block，则$modala_dialog.height() 为零
							$this.css('display', 'block');
							$modal_dialog.css({'margin-top': Math.max(0, ($(window).height() - $modal_dialog.height()-20) / 2) });
						});
	};
	$yml.sysMsg=function(msg){
		var $dlg="#sysMsg";
		$("#contentMsg",$dlg).html(msg);
		$($dlg).modal('show');
	};
	$yml.editor=function(eleName,pos){
		var eleIdJuery="#"+eleName;
		var pos=pos || "bottom";
		$(eleIdJuery).wysiwyg({
			toolbar:pos,
			buttons:{
				smilies: {
									title: 'Smilies',
									image: '\uf118', // <img src="path/to/image.png" width="16" height="16" alt="" />
									popup: function( $popup, $button ) {
													var list_smilies = [
																	'<img src="/vendor/editor/smiley/1.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/2.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/3.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/4.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/5.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/6.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/7.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/8.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/9.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/10.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/11.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/12.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/13.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/14.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/15.png" width="24" height="24" alt="" />',
																	'<img src="/vendor/editor/smiley/16.png" width="24" height="24" alt="" />',

													];
													var $smilies = $('<div/>').addClass('well')
																										.attr('unselectable','on');
													$.each( list_smilies, function(index,smiley){
															if( index != 0 ){
																$smilies.append(' ');
																if(index % 8==0 && index!=0){
																	$smilies.append('<br/><br/>');
																}
															}

															var $image = $(smiley).attr('unselectable','on');
															// Append smiley
															var imagehtml = ' '+$('<div/>').append($image.clone()).html()+' ';
															$image
																	.css({ cursor: 'pointer' })
																	.click(function(event){
																			$(eleIdJuery).wysiwyg('shell').insertHTML(imagehtml); // .closePopup(); - do not close the popup
																	})
																	.appendTo( $smilies );
													});
													var $container = $(eleIdJuery).wysiwyg('container');
													$smilies.css({ maxWidth: parseInt($container.width()*0.95)+'px' });
													$popup.append( $smilies );
													// Smilies do not close on click, so force the popup-position to cover the toolbar
													var $toolbar = $button.parents( '.wysiwyg-toolbar' );
													if( ! $toolbar.length ) // selection toolbar?
															return ;
													var left = 0,
															top = 0,
															node = $toolbar.get(0);
													while( node )
													{
															left += node.offsetLeft;
															top += node.offsetTop;
															node = node.offsetParent;
													}
													left += parseInt( ($toolbar.outerWidth() - $popup.outerWidth()) / 2 );
													if( $toolbar.hasClass('wysiwyg-toolbar-top') )
															top -= $popup.height() - parseInt($button.outerHeight() * 1/4);
													else
															top += parseInt($button.outerHeight() * 3/4);
													$popup.css({ left: left + 'px',
																			 top: top + 'px'
																		 });
													// prevent applying position
													return false;
												 },
									//showstatic: true,    // wanted on the toolbar
									//showselection: index == 2 ? true : false    // wanted on selection
							},
			}
		});
	};
})(window,$);