#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Benjamin
 
import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import asyncio
import threading
from threading import Thread
from threading import Timer
import os
import pymssql #引入pymssql模块
import uuid
import configparser
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.touch_actions import TouchActions

class PFDataHelper:  
  @staticmethod
  def DateFormat():
    return '%Y-%m-%d'
  @staticmethod
  def DomClick(driver,tag_element):
    ee=None
    #tag_element=driver.find_element_by_xpath(tag_element_xpath)
    try:
      tag_element.click()
    except BaseException as e:
      ee=e
      try:
        ActionChains(driver).move_to_element(tag_element).click().perform() 
      except BaseException as e1:
        ee=e1
        try:
          driver.execute_script("arguments[0].click();", tag_element)
        except BaseException as e2:
          ee=e2
    if ee==None:
      print('DomClick() Success: ')    
      print(tag_element.tag_name)
      return True
    else:
      print('DomClick() Error e: ')
      print(e)
  @staticmethod
  def DomClickXPath(driver,tag_element_xpath):
    ee=[]
    tag_element=driver.find_element_by_xpath(tag_element_xpath)
    try:
      tag_element.click()
    except BaseException as e:
      ee+=[e]
      try:
        ActionChains(driver).move_to_element(tag_element).click().perform() 
      except BaseException as e1:
        ee+=[e1]
        try:
          driver.execute_script("arguments[0].click();", tag_element)
        except BaseException as e2:
          ee+=[e2]
    if len(ee)<3:
      print('DomClick() Success: '+str(len(ee)))    
      print(tag_element_xpath)
      return True
    else:
      print('DomClick() Error e: ')
      print(ee)
class PFPageCatcher:
    'Perfect爬虫类'
    def __init__(self, userName, pwd):
      self._userName = userName
      self._pwd = pwd
    def login(self,hideBrowser):        
      #https需要
      # profile=webdriver.FirefoxProfile()
      # profile.accept_untrusted_certs=True
      # profile=webdriver.ChromeProfile()#报错
      # self.driver = webdriver.Firefox(firefox_profile=profile)
      if hideBrowser==1:        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
      else:
        self.driver = webdriver.Chrome()
      driver=self.driver
      driver.set_page_load_timeout(5000)
      #尝试登陆:https://www.cnblogs.com/andy9468/p/10901608.html
      loginUrl="https://zxy9.zhixueyun.com/oauth/#login/cmVzcG9uc2VfdHlwZT10b2tlbiZjbGllbnRfaWQ9OTk5JnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRnBlcmZlY3QuemhpeHVleXVuLmNvbSZzdGF0ZT0lMkZob21lJmxhbmc9Y24mY2FuY2VsUmVtZW1iZXJTdGF0ZT0w"
      #loginUrl="http://192.168.0.26:28102/User/Login?ReturnUrl=%2f"
      driver.get(loginUrl)

      print('打开了页面')

      time.sleep(5) #driver.get之后要等待页面加载完(有的情况下get会自动等待加载完)--benjamin
  #     # 点击账号和密码登录
      #input_username = driver.find_element_by_xpath("//input[@name='userid']")
      # input_password = driver.find_element_by_xpath("//input[@name='password']")
      # input_box0 = driver.find_element_by_xpath("//input[@class='btn']")
      
      input_username = driver.find_element_by_xpath("//input[@name='username']")
      input_password = driver.find_element_by_xpath("//input[@name='pword']")
      input_box0 = driver.find_element_by_xpath("//button[@class='btn-login']")

      # input_username.send_keys(u"1712002")
      # input_password.send_keys(u"123456a")
      # # # input_username.value="aaa"
      input_username.send_keys(self._userName)
      input_password.send_keys(self._pwd)

      input_box0.click()

      print('点击了登陆按钮')
      time.sleep(8)#10)
    def getHtml(self):
      # return self.driver.page_source.get_text()
      return self.driver.page_source
    def getPage(self,url):
      self.driver.get(url)
      time.sleep(8)  #5时有报错
      return self.driver.page_source
    # def getLesson(self):
    #   driver=self.driver
    #   # videoListUrl="https://perfect.zhixueyun.com/#/study/subject/detail/a4068ba4-891e-4b04-8aca-c1365bd68fb2"
    #   # #videoListUrl="https://perfect.zhixueyun.com/api/v1/course-study/subject/chapter-progress?courseId=a4068ba4-891e-4b04-8aca-c1365bd68fb2&_=1590047045850"
    #   # driver.get(videoListUrl)
    #   time.sleep(10)
    #   #return driver.page_source
    #   soup = BeautifulSoup(driver.page_source, 'lxml')
    #   print(driver.page_source)
    #   #div=soup.find('div',attrs={'class':'name-des'})
    #   #print(div.get_text())
    #   # result=[]
    #   # #return soup.body.select('div[class=item] div[data-resource-id]')
    #   # print(soup.body)
    #   # # for img_tag in soup.body.select('div[class=item][data-resource-id]'):
    #   # # for img_tag in soup.body.select('div[class=item] div[data-resource-id]'):
    #   # for img_tag in soup.body.select('div[class=name-des]'):   
    #   #   print(img_tag.text)     
    #   #   result+=[img_tag.text]
    #   # return result
    #   # print(img_tag.attrs['href'])


class PfCatcherForm:
  def __init__(self):
    config = configparser.ConfigParser()
    conf_file = open("postAnswerPageApp_config.ini")
    #config.readfp(conf_file)
    config.read_file(conf_file)

    #默认参数
    ## defaultLessonUrl="https://perfect.zhixueyun.com/#/study/subject/detail/8247851a-a8a1-446a-988d-51697e32114b"
    # defaultLessonUrl="https://perfect.zhixueyun.com/#/study/course/index"
    # defaultUserName="1712002"
    # defaultUserPwd="123456a"
    defaultLessonUrl=config.get("pageUrl","lessonUrl")
    defaultUserName=config.get("userInfo","userName")
    defaultUserPwd=config.get("userInfo","userPwd")
    defaultStartAfterLogin=config.get("userSetting","startAfterLogin")
    defaultAutoPunchIn=config.get("userSetting","autoPunchIn")
    defaultAutoPassLearned=config.get("userSetting","autoPassLearned")
    # defaultUserName=""

    conf_file.close()


    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    
    # 第2步，给窗口的可视化起名字
    window.title("自动学习程序")
    
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('750x720')  # 这里的乘是小x
    
    # 第4步，在图形界面上设定标签
    l = tk.Label(window, text='你好！本 python 程序由 Benjamin 开发', bg='green', font=('Arial', 12), width=30, height=2)
    # 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
    
    # 第5步，放置标签
    l.pack()    # Label内容content区域放置位置，自动调节尺寸
    # 放置lable的方法有：1）l.pack(); 2)l.place();

    userNameLabel = tk.Label(window, text='用户名:', bg='green', font=('Arial', 12), width=30, height=1)
    userNameLabel.pack()
    #userNameLabel.grid(row=0, column=0, padx=10, pady=10, ipadx=10, ipady=10)

    self.userNameInputStr =StringVar(value=defaultUserName)
    userNameInput = tk.Entry(window, textvariable=self.userNameInputStr,show=None, font=('Arial', 14)) 
    userNameInput.pack()

    userPwdLabel = tk.Label(window, text='密码:', bg='green', font=('Arial', 12), width=30, height=1)
    userPwdLabel.pack()

    self.userPwdInputStr =StringVar(value=defaultUserPwd)
    userPwdInput = tk.Entry(window, textvariable=self.userPwdInputStr,show="*", font=('Arial', 14)) 
    userPwdInput.pack()

    lessonUrlLabel = tk.Label(window, text='课程地址:', bg='green', font=('Arial', 12), width=30, height=1)
    lessonUrlLabel.pack()

    self.lessonUrlInputStr =StringVar(value=defaultLessonUrl)
    lessonUrlInput = tk.Entry(window, textvariable=self.lessonUrlInputStr,show=None, font=('Arial', 14)) 
    lessonUrlInput.pack()

    self.pageInput= tk.Text(window,height = 5)
    self.lessonInput= tk.Text(window,height = 5)
    self.lessonListInput= tk.Text(window,height = 5)

    processLabel = tk.Label(window, text='进度:', bg='green', font=('Arial', 12), width=30, height=1)
    processLabel.pack()

    self.processInputStr =StringVar(value="0/0")
    processInput = tk.Entry(window, textvariable=self.processInputStr,show=None, font=('Arial', 14),state='readonly') 
    processInput.pack()

    learnedTimeLabel = tk.Label(window, text='已学习:', bg='green', font=('Arial', 12), width=30, height=1)
    learnedTimeLabel.pack()

    self.learnedTimeInputStr =StringVar(value="")
    learnedTimeInput = tk.Entry(window, textvariable=self.learnedTimeInputStr,show=None, font=('Arial', 14),state='readonly') 
    learnedTimeInput.pack()

    self.startAfterLoginInt = tk.IntVar()
    self.startAfterLoginInt.set(defaultStartAfterLogin)
    startAfterLoginInput = tk.Checkbutton(window,text = "登陆后自动开始",variable = self.startAfterLoginInt,onvalue = 1,offvalue = 0)
    startAfterLoginInput.pack()

    self.autoPunchLoginInt = tk.IntVar(value=defaultAutoPunchIn)
    autoPunchLoginInput = tk.Checkbutton(window,text = "自动打卡",variable = self.autoPunchLoginInt,onvalue = 1,offvalue = 0)
    autoPunchLoginInput.pack()
    
    self.autoPassLearnedInt = tk.IntVar(value=defaultAutoPassLearned)
    autoPassLearnedInput = tk.Checkbutton(window,text = "自动跳过完成的课程",variable = self.autoPassLearnedInt,onvalue = 1,offvalue = 0)
    autoPassLearnedInput.pack()

    self.autoShutdownInt = tk.IntVar()
    autoShutdownInput = tk.Checkbutton(window,text = "完成时关机",variable = self.autoShutdownInt,onvalue = 1,offvalue = 0)
    autoShutdownInput.pack()
    
    self.hideBrowserInt = tk.IntVar()
    hideBrowserInput = tk.Checkbutton(window,text = "隐藏浏览器",variable = self.hideBrowserInt,onvalue = 1,offvalue = 0)
    hideBrowserInput.pack()

    self.loginInput=tk.Button(window, text='登陆', bg='green', font=('Arial', 14), command=self.asyncLogin )
    self.loginInput.pack()

    self.postAnswerInput=tk.Button(window, text='保存答案', bg='green', font=('Arial', 14), command=self.asyncPostAnswer )
    self.postAnswerInput.pack()
    # self.postAnswerInput.config(state="disabled")

    self.answerPagInput=tk.Button(window, text='开始回答问题', bg='green', font=('Arial', 14), command=self.asyncAnswerPage )
    self.answerPagInput.pack()
    
    self.testReplayInput=tk.Button(window, text='测试重播', bg='blue', font=('Arial', 14), command=self.clickReplayBtn )
    self.testReplayInput.pack()
    
    self.testPlayInput=tk.Button(window, text='测试播放', bg='blue', font=('Arial', 14), command=self.clickPlayBtn )
    self.testPlayInput.pack()

    # self.answerPagInput.config(state="disabled")

    # self.playCurPageInput=tk.Button(window, text='播放当前列表页', bg='green', font=('Arial', 14), command=self.asyncPlayCurPage )
    # self.playCurPageInput.pack()

    self.pageInput.pack()
    self.lessonInput.pack()
    self.lessonListInput.pack()

    self.isLogin=0
    self.pfCatcher=None
    self.lastPushTime='' #上次打卡时间 
    # 第6步，主窗口循环显示
    # self.root=window
    # self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    window.mainloop()
    # 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
    # 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。

  # def on_closing(self):
  #   # self.new_loop.close()
  #   # self.t.destroy()
  #   self.t.cancel()
  #   self.root.destroy()
  #   asyncio
  def asyncLogin(self):
    #return await _thread.start_new_thread( self.doCalculate, ("Thread-1", 2, ) )#报错：RuntimeWarning: Enable tracemalloc to get the object allocation traceback
    # _thread.start_new_thread( self.doCalculate, () )
    self.t = Thread(target=self.login,args=())  #通过当前线程开启新的线程去启动事件循环
    self.t.start()

  def asyncPostAnswer(self):
    self.tPostAnswer = Thread(target=self.postAnswer,args=())  #通过当前线程开启新的线程去启动事件循环
    self.tPostAnswer.start()
  def asyncAnswerPage(self):
    self.tAnswerPage = Thread(target=self.answerPage,args=())  #通过当前线程开启新的线程去启动事件循环
    self.tAnswerPage.start()
    
  def doPlayCurPage(self):    
    # #判断是哪一种课程页,类型参考E:\web\html_all\study\自动在线学习程序_readme.txt
    # if self.lessonUrlInputStr.get().find('perfect.zhixueyun.com/#/study/subject/detail')>-1:
    #   self.lessonUrlType=1  #https://perfect.zhixueyun.com/#/study/subject/detail/8247851a-a8a1-446a-988d-51697e32114b
    # else:
    #   self.lessonUrlType=2  #https://perfect.zhixueyun.com/#/study/course/index
    #   self.curLessonPage=1  #这种类型是分页的

    lessonPage=self.pfCatcher.getHtml()      

    soup = BeautifulSoup(lessonPage, 'lxml')    
    self.lessons=[]
    if self.lessonUrlType==1:
      items = soup.select('.name-des')  
      for item in items:
        li=item.parent.parent
        title=item.get('title')
        btn=li.select('i.iconfont div')[0].get_text()
        attachmentId=li.get('data-resource-id')
        print(title )#attrs字典取属性
        print(btn )#attrs字典取属性
        self.lessons+=[{'title':title,'btn': btn,'attachmentId':attachmentId}]
    else:          
      items = soup.select('li.list-item')  
      for item in items:
        urlItem=item.select('.content-bottom a')[0]
        title=urlItem.get_text()
        url=urlItem.get('href')

        btnItem=item.select('.content .img .study-status')
        if len(btnItem)>0:
          btn=btnItem[0].get_text()
        else:
          btn=''
        if btn=="已完成":
          btn="重新学习"

        self.lessons+=[{'title':title,'btn':btn,'url':url}]
      # items = soup.select('li.list-item .content-bottom a')  
      # for item in items:
      #   title=item.get_text()
      #   url=item.get('href')
      #   self.lessons+=[{'title':title,'url':url}]
    
    self.lessonListInput.insert(1.0,self.lessons)

    self.lessonCnt=len(self.lessons) 

    self.playLesson(self.pfCatcher) 

  # def goToNextPage(self):
  #   soup=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml')
  #   idx=int(soup.select('.pagination .active')[0].get_text())  #这种类型是分页的
  #   nextIdx=idx+1
  #   nextBtn=soup.select('.pagination .item[data-page="{0}"]'.format(nextIdx))
  #   if len(nextBtn)>0:
  #     tmpstr="//div[@class='pagination']/div[@data-page='{0}']".format(nextIdx)
  #     self.pfCatcher.driver.find_element_by_xpath(tmpstr).click()
  #     time.sleep(2)
  #     return 1  
  #   else:
  #     return 0
  def goToPage(self):
    # self.pfCatcher.getPage(self.lessonUrlInputStr.get())
    # while self.goToNextPage()==1:
      
    # nextBtn=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .item[data-page="{0}"]'.format(self.curLessonPage))
    nextBtn=BeautifulSoup(self.pfCatcher.getPage(self.lessonUrlInputStr.get()), 'lxml').select('.pagination .item[data-page="{0}"]'.format(self.curLessonPage))#如果上一次也是在列表页,即url没变化的话,找第5页就已经找不到了
    if len(nextBtn)>0:
      return 1  #5页之前都是可以直接一次切换

    #有时页面超时打不开,页面都是空的--benjamin20200603
    while len(BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .active'))<1:
      return -1
      # self.pfCatcher.getPage(self.lessonUrlInputStr.get())
      
    #8页之后要一次一次切换
    curP=int(BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .active')[0].get_text())+1
    while curP<=self.curLessonPage:
      nextBtn=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .item[data-page="{0}"]'.format(curP))
      if len(nextBtn)>0:
        tmpstr="//div[@class='pagination']/div[@data-page='{0}']".format(curP)
        self.pfCatcher.driver.find_element_by_xpath(tmpstr).click()
        # nextBtn0 = self.pfCatcher.driver.find_element_by_xpath(tmpstr)
        # time.sleep(1)#这里不延迟好像会有问题,因为find_element_by_xpath调用后页面会刷新一下的
        # nextBtn0.click()
        time.sleep(2)
      else:
        return 0
      curP+=1
    return 1
    # if curP>=self.curLessonPage:
    #   return 1
    # return 0
  def playCurPage(self):
    self.startTime=datetime.datetime.now()
    # self.lessonUrlInputStr.set(self.pfCatcher.driver.current_url)
    
    #判断是哪一种课程页,类型参考E:\web\html_all\study\自动在线学习程序_readme.txt
    if self.lessonUrlInputStr.get().find('perfect.zhixueyun.com/#/study/subject/detail')>-1:
      self.lessonUrlType=1  #https://perfect.zhixueyun.com/#/study/subject/detail/8247851a-a8a1-446a-988d-51697e32114b
    else:
      self.lessonUrlType=2  #https://perfect.zhixueyun.com/#/study/course/index      
      self.curLessonPage=int(BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .active')[0].get_text())  #这种类型是分页的

        
    if self.lessonUrlType==1:
      self.doPlayCurPage()    
    else:#找下一页      
      hasPage=1
      while hasPage==1:     
        self.doPlayCurPage()      
        self.curLessonPage+=1
        hasPage=self.goToPage()
        while hasPage==-1:#网络错误重试
          hasPage=self.goToPage()
        # nextBtn=BeautifulSoup(self.pfCatcher.getPage(self.lessonUrlInputStr.get()), 'lxml').select('.pagination .item[data-page="{0}"]'.format(self.curLessonPage))
        # if len(nextBtn)>0:
        #   tmpstr="//div[@class='pagination']/div[@data-page='{0}']".format(self.curLessonPage)
        #   nextBtn0 = self.pfCatcher.driver.find_element_by_xpath(tmpstr)
        #   time.sleep(5)#这里不延迟好像会有问题,因为find_element_by_xpath调用后页面会刷新一下的
        #   nextBtn0.click()
        #   time.sleep(5)
        # else:
        #   hasPage=0

    self.processInputStr.set("已完成")
    self.loginInput.config(state='normal',text='重新学习')
    # self.playCurPageInput.config(state="normal")
    if self.autoShutdownInt.get()==1:
      os.system('shutdown -s -f -t 59') #取消关机命令 shutdown /a

  def playCurLesson(self,pfCatcher):  
    # learnedTime=datetime.datetime.now()-self.startTime
    lesson=self.lessons[self.curIdx]
    # self.learnedTimeInputStr.set('{0}分'.format(round(learnedTime.seconds/60,2)))
    if self.lessonUrlType==1:
      self.processInputStr.set('{0}/{1}'.format(self.curIdx,self.lessonCnt))
      pfCatcher.getPage("https://perfect.zhixueyun.com/#/study/course/detail/10&{0}/6/1".format(lesson['attachmentId']))
    else:
      self.processInputStr.set('{0}/{1} 第{2}页'.format(self.curIdx,self.lessonCnt,self.curLessonPage))
      # pfCatcher.getPage("https://perfect.zhixueyun.com/{0}".format(lesson['url'])) 
      pfCatcher.getPage("https://perfect.zhixueyun.com/{0}/6/1".format(lesson['url']))#后面没有6/1时不能播放,试试加上(似乎有了6/1就能自动播放)--benjamin20200528


  def clickExceptOther(self,netErrorEle):
      # netErrorEle=self.pfCatcher.driver.find_element_by_xpath("//div[@class='vjs-netslow']//div[@class='slow-img']")
      self.pfCatcher.driver.execute_script("arguments[0].click();", netErrorEle)
  def pushIn(self):#打卡
    nowtime=datetime.datetime.now().strftime(PFDataHelper.DateFormat())
    if self.autoPunchLoginInt.get()==1 and self.lastPushTime!=nowtime:
      self.pfCatcher.getPage('https://perfect.zhixueyun.com/#/ask/index') 
      # self.pfCatcher.driver.find_element_by_xpath("//div[@class='publish-btn']").click()
      #上句报错is not clickable at point (862, 18). Other element would receive the click: <div
 #id="D66message-id" class="menu-item">...</div>
      self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//div[@class='publish-btn']"))
      self.lastPushTime=nowtime
      time.sleep(2)
      self.pfCatcher.driver.find_element_by_xpath("//div[@class='form relative pulish-content-page']//input[@name='title']").send_keys(u"打卡")
      # self.pfCatcher.driver.find_element_by_xpath("//div[@class='tag-btn radius ' and text()='打卡']").click()
      time.sleep(1)
      self.pfCatcher.driver.find_element_by_xpath("//div[@class='dialog-footer']//div[@class='btn' and text()='发布']").click()            
      time.sleep(3)       
      self.pfCatcher.driver.refresh()
      time.sleep(2)
      #打卡之后弹窗不能关闭,要刷新   
  def clickReplayBtn(self):
    #实测试ok
    tag_element = self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']")
    ActionChains(self.pfCatcher.driver).move_to_element(tag_element).click().perform() 

    #ActionChains(self.pfCatcher.driver).move_to_element(tag_element).perform()
    # Action = TouchActions(self.pfCatcher.driver)
    # Action.tap(tag_element)
    # Action.perform()
    #self.clickExceptOther(tag_element)
    #ActionChains(self.pfCatcher.driver).move_to_element(tag_element).perform()

    # self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']").click() #报错,被挡
    # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']"))
    # self.pfCatcher.driver.execute_script("$('.videojs-referse-btn').click();")
    # self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']//span[@class='vjs-control-text']").click()  #报错,Other element would receive the click
    # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']//span[@class='vjs-control-text']"))
    # self.pfCatcher.driver.find_element_by_xpath("//video[@class='vjs-tech']").click() #报错,被挡
    # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//video[@class='vjs-tech']"))  #点了还是没隐藏
    # self.pfCatcher.driver.execute_script("arguments[1].click();", self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']"))  #Cannot read property 'click' of undefined    
    # self.pfCatcher.driver.execute_script("arguments[0].click();", self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']"))
    # self.pfCatcher.driver.find_element_by_xpath("//span[text()='重新学习']").click()
    # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//span[text()='重新学习']"))#点了还是没隐藏
    time.sleep(5)
  def clickPlayBtn(self):    
    # PFDataHelper.DomClick(self.pfCatcher.driver,self.pfCatcher.driver.find_element_by_xpath("//button[@class='vjs-play-control vjs-control vjs-button vjs-paused' and @title='播放']"))    
    PFDataHelper.DomClickXPath(self.pfCatcher.driver,"//button[@class='vjs-play-control vjs-control vjs-button vjs-paused' and @title='播放']")
    # try:
    #   #实测试ok
    #   tag_element = self.pfCatcher.driver.find_element_by_xpath("//button[@class='vjs-play-control vjs-control vjs-button vjs-paused' and @title='播放']")
    #   tag_element.click()
    # except BaseException as e:
    #   try:
    #     tag_element = self.pfCatcher.driver.find_element_by_xpath("//button[@class='vjs-play-control vjs-control vjs-button vjs-paused' and @title='播放']")
    #     ActionChains(self.pfCatcher.driver).move_to_element(tag_element).click().perform() 
    #   except BaseException as e1:
    #     time.sleep(1)
    time.sleep(5)
  def playLesson(self,pfCatcher):  
    self.pushIn()

    self.curIdx=0
    cnt=len(self.lessons)

    while self.curIdx<cnt:
      lesson=self.lessons[self.curIdx]
      if ('btn' not in lesson) or self.autoPassLearnedInt.get()==0 or lesson['btn']!='重新学习':
        self.playCurLesson(pfCatcher)
        time.sleep(10)#(900)

        #如果不能自动播放,还是先检测后点一下播放吧  
        soup=BeautifulSoup(pfCatcher.getHtml(), 'lxml')      
        replayDom=soup.find('button',attrs={'class': 'videojs-referse-btn'})#重新播放按钮
        if replayDom is not None and 'vjs-hidden' not in replayDom.get('class'):
          # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']"))
          self.clickPlayBtn()

        finishCnt=0
        while finishCnt==0:
          self.pushIn()  #以防被某些课程卡住,在这里打卡比较保险
          learnedTime=datetime.datetime.now()-self.startTime
          self.learnedTimeInputStr.set('{0}分'.format(round(learnedTime.seconds/60,2)))
          soup=BeautifulSoup(pfCatcher.getHtml(), 'lxml')

          finishDom=soup.find('div', text="您已完成该课程的学习")
          if finishDom is not None:
            finishCnt=1
            continue
          
          # H5课程
          # h5Dom=soup.find('div',attrs={'class': 'item sub-text focus'}, text="H5")
          # if h5Dom is not None:
          #   finishCnt=1
          #   continue
          if len(soup.select('div.player-content div.h5-bg-img'))>0:
            finishCnt=1
            continue
          
          netErrorDom=soup.find('div', text="网络不稳定，请刷新重试")
          if netErrorDom is not None:
            #self.pfCatcher.driver.refresh()
            try:
              netErrorEle=self.pfCatcher.driver.find_element_by_xpath("//div[@class='vjs-netslow']//div[@class='slow-img']")
              self.pfCatcher.driver.execute_script("arguments[0].click();", netErrorEle)
            except BaseException as e:
              print(e)
            # netErrorEle.click()
            # webdriver.ActionChains(self.pfCatcher.driver).move_to_element(netErrorEle ).click(netErrorEle ).perform()
            time.sleep(2)
            continue
          
          goawayDom=soup.find('p', text="亲爱的学员，目前学习正在计时中，请不要走开哦!")
          if goawayDom is not None:
            try:
              self.pfCatcher.driver.find_element_by_xpath("//div[@class='alert-wrapper']//div[@class='btn-ok btn']").click()
            except BaseException as e:
              print(e)
            time.sleep(2)
            continue

          openOtherDom=soup.find('div', text="您已打开新的课程详情页，点击按钮，可继续学习。")
          if openOtherDom is not None:
            try:
              self.pfCatcher.driver.find_element_by_xpath("//div[@class='study-errors-page']//div[@class='btn']").click()
            except BaseException as e:
              print(e)
            time.sleep(2)
            continue
          
          replayDom=soup.find('button',attrs={'class': 'videojs-referse-btn'})#重新播放按钮
          if replayDom is not None and 'vjs-hidden' not in replayDom.get('class'):
            if self.autoPassLearnedInt.get()==1:
              finishCnt=1
              # self.pfCatcher.driver.find_element_by_xpath("//div[@class='videojs-referse-btn']").click()
              # time.sleep(2)
              continue
            else:#当打开已学完的课程时,有可能进入这里
              # self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']").click()
              # self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']"))
              # self.pfCatcher.driver.find_element_by_xpath("//button[@class='videojs-referse-btn']//span[@class='vjs-control-text']").click()
              self.clickPlayBtn()
              continue
          
          videoDom=soup.find('video',attrs={'class': 'vjs-tech'}) #如果没有找到这个元素，认为页面加载失败(（)可能是网络原因)
          if videoDom is None:
            if self.isLoginTimeout()==1:
              self.pfCatcher.login(self.hideBrowserInt.get())
              self.playCurLesson(pfCatcher)
              continue
            else:                
              self.pfCatcher.driver.refresh()
              time.sleep(5)
              continue
          
          time.sleep(20)

      self.curIdx+=1
      
  def isLoginTimeout(self):#是否登陆失效
    soup=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml')
    loginBtnDom=soup.find('button',attrs={'class': 'btn-login'})#重新播放按钮
    if loginBtnDom is not None:
      return 1
    else:
      return 0

  def postAnswer(self):#是否登陆失效

    lessonPage=self.pfCatcher.getHtml()      

    soup = BeautifulSoup(lessonPage, 'lxml')    
    self.questions=[]
    self.answers=[]

    items = soup.select('div.question')  
    for item in items:
      question=item.get_text()
      question=re.sub('^\n[\d]+、\n[ ]*', '', question, count=0, flags=0)
      question=re.sub('\n[ ]*$', '', question, count=0, flags=0)
      
      answerDoms=item.parent.parent.select('div.answer-options')
      tmpAnswers=[]
      for answerDom in answerDoms:
        answer=answerDom.get_text()
        tmpAnswers+=[{'Answer':answer}]
      
      showAnswerText=item.parent.parent.select('div.show-answer div div')[0].get_text()

      answerCnt=0
      questionType=1
      rightAnswers=[]
      if showAnswerText.find('A')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[0]['Answer']}]
        rightAnswers+=[tmpAnswers[0]['Answer']]
        answerCnt+=1

      if showAnswerText.find('B')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[1]['Answer']}]
        rightAnswers+=[tmpAnswers[1]['Answer']]
        answerCnt+=1

      if showAnswerText.find('C')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[2]['Answer']}]
        rightAnswers+=[tmpAnswers[2]['Answer']]
        answerCnt+=1

      if showAnswerText.find('D')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[3]['Answer']}]
        rightAnswers+=[tmpAnswers[3]['Answer']]
        answerCnt+=1
        
      if showAnswerText.find('E')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[4]['Answer']}]
        rightAnswers+=[tmpAnswers[4]['Answer']]
        answerCnt+=1

      if showAnswerText.find('F')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[5]['Answer']}]
        rightAnswers+=[tmpAnswers[5]['Answer']]
        answerCnt+=1

      if showAnswerText.find('G')>-1:
        self.answers+=[{'Question':question,'Answer':tmpAnswers[6]['Answer']}]
        rightAnswers+=[tmpAnswers[6]['Answer']]
        answerCnt+=1

      isRight=0

      if showAnswerText.find('正确')>-1:
        isRight=1

      if answerCnt>1:
        questionType=2
      elif answerCnt==0:
        questionType=3      

      self.questions+=[{'Question':question,'QuestionType':questionType,'IsRight':isRight,'Answers':rightAnswers}]
      
      # urlItem=item.select('.content-bottom a')[0]
      # title=urlItem.get_text()
      # url=urlItem.get('href')

      # btnItem=item.select('.content .img .study-status')
      # if len(btnItem)>0:
      #   btn=btnItem[0].get_text()
      # else:
      #   btn=''
      # if btn=="已完成":
      #   btn="重新学习"

      # self.lessons+=[{'title':title,'btn':btn,'url':url}]
      
    self.pageInput.insert(1.0,self.questions)
    self.lessonInput.insert(1.0,self.answers)

    connect = pymssql.connect('121.199.2.204', 'sa', 'luluSKIcom', 'SellGirl.Game')  #建立连接
    if connect:
        print("连接成功!")

    for question in self.questions:
      cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
      sql ="select Question from game_question where Question='{0}'".format(question['Question'])
      cursor.execute(sql)   #执行sql语句
      row = cursor.fetchone()  #读取查询结果,
      isExist=0
      while row:              #循环读取所有结果
        isExist=1
        break
        # print("Name=%s, Sex=%s" % (row[0],row[1]))   #输出结果
        # row = cursor.fetchone()
      if isExist==0:
        questionId=uuid.uuid4()
        sql = "insert into game_question (QuestionId,Question,QuestionType,IsRight)values('{0}','{1}',{2},{3})".format(questionId,question['Question'],question['QuestionType'],question['IsRight'])
        
        try:
          cursor.execute(sql)   #执行sql语句
          connect.commit()  #提交
        except BaseException as e:
          print(e)
        for answer in question['Answers']:
          sql = "insert into game_answer (AnswerId,QuestionId,Answer)values('{0}','{1}','{2}')".format(uuid.uuid4(),questionId,answer)
          cursor.execute(sql)   #执行sql语句
          connect.commit()  #提交
    cursor.close()   
    connect.close()

  def answerPage(self):#是否登陆失效

    lessonPage=self.pfCatcher.getHtml()      

    soup = BeautifulSoup(lessonPage, 'lxml')    
    self.questions=[]
    self.answers=[]

    items = soup.select('div.question')  
    
    connect = pymssql.connect('121.199.2.204', 'sa', 'luluSKIcom', 'SellGirl.Game')  #建立连接
    if connect:
        print("连接成功!")

    questionIdx=0 #为了定位xpath
    for item in items:
      question=item.get_text()
      question=re.sub('^\n[\d]+、\n[ ]*', '', question, count=0, flags=0)
      question=re.sub('\n[ ]*$', '', question, count=0, flags=0)

      dataDynamicKey=item.parent.parent.parent.get('data-dynamic-key')  #因为xpath不能用eq(1)方法
      
      cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
      sqlAnswers=[]
      sqlQuestionType=0
      sqlIsRight=0

      sql =("select a.Answer,b.QuestionType,b.IsRight from [SellGirl.Game].[dbo].[game_answer] a "+
"right join [SellGirl.Game].[dbo].[game_question] b on b.QuestionId=a.QuestionId "+
"where b.Question='{0}'").format(question)
      cursor.execute(sql)   #执行sql语句
      row = cursor.fetchone()  #读取查询结果,
      #isExist=0
      while row:              #循环读取所有结果
        # isExist=1
        # break
        sqlAnswers+=[row[0]]
        sqlQuestionType=row[1]
        sqlIsRight=row[2]
        # print("Name=%s, Sex=%s" % (row[0],row[1]))   #输出结果
        row = cursor.fetchone()
      
      if sqlQuestionType==3: #判断题
        if sqlIsRight==1:
          # self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//span[text()='{1}']".format(dataDynamicKey,"正确")).click()
          # self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//div[@class='radio']//input[@value=1]".format(dataDynamicKey)).click()
          self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//div[@class='radio']//input[@value=1]".format(dataDynamicKey)))
        else:
          # self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//span[text()='{1}']".format(dataDynamicKey,"错误")).click()
          # self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//div[@class='radio']//input[@value=0]".format(dataDynamicKey)).click()
          self.clickExceptOther(self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//div[@class='radio']//input[@value=0]".format(dataDynamicKey)))
      else:
        answerDoms=item.parent.parent.select('div.answer-options')
        #tmpAnswers=[]       

        for answerDom in answerDoms:
          answer=answerDom.get_text()
          if answer in sqlAnswers:
            # self.pfCatcher.driver.find_element_by_xpath("//div[@class='answer'][{0}]//div[@class='answer-options m-left' and text()='{1}']".format(questionIdx+1,answer)).click()//不能用索引找
            self.pfCatcher.driver.find_element_by_xpath("//div[@data-dynamic-key='{0}']//div[@class='answer']//div[@class='answer-options m-left' and text()='{1}']".format(dataDynamicKey,answer)).click()

      questionIdx+=1

    cursor.close()   
    connect.close()

  def login(self):
    config = configparser.ConfigParser()
    conf_file = open("postAnswerPageApp_config.ini")
    config.read_file(conf_file)
    conf_file.close()
    config.set("userInfo","userName",self.userNameInputStr.get())
    config.set("userInfo","userPwd",self.userPwdInputStr.get())
    config.set("pageUrl","lessonUrl",self.lessonUrlInputStr.get())
    config.set("userSetting","startAfterLogin",str(self.startAfterLoginInt.get()))
    config.set("userSetting","autoPunchIn",str(self.autoPunchLoginInt.get()))
    config.set("userSetting","autoPassLearned",str(self.autoPassLearnedInt.get()))
    file_write = open("postAnswerPageApp_config.ini","w")
    config.write(file_write) 
    file_write.close()

    if tk.messagebox.askokcancel(title='Hi', message=self.userNameInputStr.get()):
      self.loginInput.config(state="disabled")
      # self.playCurPageInput.config(state="disabled")
      if self.isLogin==1:#如果是已登陆的状态,就播放当前打开的页面,而不是lessonUrlInputStr
        self.lessonUrlInputStr.set(self.pfCatcher.driver.current_url)
        self.playCurPage()
      else :
        self.pfCatcher=PFPageCatcher(self.userNameInputStr.get(),self.userPwdInputStr.get())
        self.pfCatcher.login(self.hideBrowserInt.get())
        self.isLogin=1

        if self.startAfterLoginInt.get()==1:       
          self.pfCatcher.getPage(self.lessonUrlInputStr.get())        
          self.playCurPage()
        else:
          self.loginInput.config(state='normal',text='开始学习')

        #题目答案页(抓题)
        #self.pfCatcher.getPage('https://perfect.zhixueyun.com/#/exam/exam/front/score-detail/f51c8545-b12a-4bcc-9032-7c1accfdb4d4') 
        #答题页
        self.pfCatcher.getPage('https://perfect.zhixueyun.com/#/exam/exam/answer-paper/2a6d1120-9dd1-4a55-a056-2bd7df67f1ec') 

        self.postAnswerInput.config(state='normal')          
        self.answerPagInput.config(state="normal")
           



if __name__=='__main__':
    form=PfCatcherForm()
