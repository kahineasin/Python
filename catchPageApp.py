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

class PFPageCatcher:
    'Perfect爬虫类'
    def __init__(self, userName, pwd):
      self._userName = userName
      self._pwd = pwd
    def login(self):        
      #https需要
      # profile=webdriver.FirefoxProfile()
      # profile.accept_untrusted_certs=True
      # profile=webdriver.ChromeProfile()#报错
      # self.driver = webdriver.Firefox(firefox_profile=profile)
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

      input_username.send_keys(u"1712002")
      input_password.send_keys(u"123456a")
      # # input_username.value="aaa"

      input_box0.click()

      print('点击了登陆按钮')
      time.sleep(8)#10)
    def getHtml(self):
      # return self.driver.page_source.get_text()
      return self.driver.page_source
    def getPage(self,url):
      self.driver.get(url)
      time.sleep(5)
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
    #默认参数
    # defaultLessonUrl="https://perfect.zhixueyun.com/#/study/subject/detail/8247851a-a8a1-446a-988d-51697e32114b"
    defaultLessonUrl="https://perfect.zhixueyun.com/#/study/course/index"


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

    self.userNameInputStr =StringVar(value="1712002")
    userNameInput = tk.Entry(window, textvariable=self.userNameInputStr,show=None, font=('Arial', 14)) 
    userNameInput.pack()

    userPwdLabel = tk.Label(window, text='密码:', bg='green', font=('Arial', 12), width=30, height=1)
    userPwdLabel.pack()

    self.userPwdInputStr =StringVar(value="123456a")
    userPwdInput = tk.Entry(window, textvariable=self.userPwdInputStr,show=None, font=('Arial', 14)) 
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
    startAfterLoginInput = tk.Checkbutton(window,text = "登陆后自动开始",variable = self.startAfterLoginInt,onvalue = 1,offvalue = 0)
    startAfterLoginInput.pack()

    self.autoShutdownInt = tk.IntVar()
    autoShutdownInput = tk.Checkbutton(window,text = "完成时关机",variable = self.autoShutdownInt,onvalue = 1,offvalue = 0)
    autoShutdownInput.pack()

    self.loginInput=tk.Button(window, text='登陆', bg='green', font=('Arial', 14), command=self.asyncLogin )
    self.loginInput.pack()

    # self.playCurPageInput=tk.Button(window, text='播放当前列表页', bg='green', font=('Arial', 14), command=self.asyncPlayCurPage )
    # self.playCurPageInput.pack()

    self.pageInput.pack()
    self.lessonInput.pack()
    self.lessonListInput.pack()

    self.isLogin=0
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
  # def asyncPlayCurPage(self):
  #   #return await _thread.start_new_thread( self.doCalculate, ("Thread-1", 2, ) )#报错：RuntimeWarning: Enable tracemalloc to get the object allocation traceback
  #   # _thread.start_new_thread( self.doCalculate, () )
  #   self.t = Thread(target=self.playCurPage,args=())  #通过当前线程开启新的线程去启动事件循环
  #   self.t.start()

  # def test(self):
  #     loop = asyncio.new_event_loop()  
  #     loop.run_until_complete(self.login())
  #     loop.close()  
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

  def goToPage(self):
    nextBtn=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .item[data-page="{0}"]'.format(self.curLessonPage))
    if len(nextBtn)>0:
      return 1  #5页之前都是可以直接一次切换
    #8页之后要一次一次切换
    curP=5
    while curP<=self.curLessonPage:
      nextBtn=BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .item[data-page="{0}"]'.format(curP))
      if len(nextBtn)>0:
        tmpstr="//div[@class='pagination']/div[@data-page='{0}']".format(curP)
        nextBtn0 = self.pfCatcher.driver.find_element_by_xpath(tmpstr)
        time.sleep(1)#这里不延迟好像会有问题,因为find_element_by_xpath调用后页面会刷新一下的
        nextBtn0.click()
        time.sleep(2)
      if curP==self.curLessonPage:
        return 1
      curP+=1
    return 0
  def playCurPage(self):
    self.startTime=datetime.datetime.now()
    self.lessonUrlInputStr.set(self.pfCatcher.driver.current_url)
    
    #判断是哪一种课程页,类型参考E:\web\html_all\study\自动在线学习程序_readme.txt
    if self.lessonUrlInputStr.get().find('perfect.zhixueyun.com/#/study/subject/detail')>-1:
      self.lessonUrlType=1  #https://perfect.zhixueyun.com/#/study/subject/detail/8247851a-a8a1-446a-988d-51697e32114b
    else:
      self.lessonUrlType=2  #https://perfect.zhixueyun.com/#/study/course/index      
      self.curLessonPage=int(BeautifulSoup(self.pfCatcher.getHtml(), 'lxml').select('.pagination .active')[0].get_text())  #这种类型是分页的

    # lessonPage=self.pfCatcher.getHtml()      

    # soup = BeautifulSoup(lessonPage, 'lxml')    
    # self.lessons=[]
    # if self.lessonUrlType==1:
    #   items = soup.select('.name-des')  
    #   for item in items:
    #     li=item.parent.parent
    #     title=item.get('title')
    #     btn=li.select('i.iconfont div')[0].get_text()
    #     attachmentId=li.get('data-resource-id')
    #     print(title )#attrs字典取属性
    #     print(btn )#attrs字典取属性
    #     self.lessons+=[{'title':title,'btn': btn,'attachmentId':attachmentId}]
    # else:          
    #   items = soup.select('li.list-item')  
    #   for item in items:
    #     urlItem=item.select('.content-bottom a')[0]
    #     title=urlItem.get_text()
    #     url=urlItem.get('href')

    #     btnItem=item.select('.content .img .study-status')
    #     if len(btnItem)>0:
    #       btn=btnItem[0].get_text()
    #     else:
    #       btn=''
    #     if btn=="已完成":
    #       btn="重新学习"

    #     self.lessons+=[{'title':title,'btn':btn,'url':url}]
    #   # items = soup.select('li.list-item .content-bottom a')  
    #   # for item in items:
    #   #   title=item.get_text()
    #   #   url=item.get('href')
    #   #   self.lessons+=[{'title':title,'url':url}]
    
    # self.lessonListInput.insert(1.0,self.lessons)

    # self.lessonCnt=len(self.lessons) 
        
    if self.lessonUrlType==1:
      self.doPlayCurPage()    
    else:#找下一页      
      hasPage=1
      while hasPage==1:     
        self.doPlayCurPage()      
        self.curLessonPage+=1
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

  # def playLesson(self,pfCatcher):  
  #   self.curIdx=0
  #   cnt=len(self.lessons)
  #   self.startTime=datetime.datetime.now()
  #   self.playCurLesson(pfCatcher)    
  #   self.t = Timer(1,self.playCurLesson,args=())  #通过当前线程开启新的线程去启动事件循环
  #   self.t.start()

  # def playLesson(self,pfCatcher):  
  #   self.curIdx=0
  #   cnt=len(self.lessons)
  #   self.startTime=datetime.datetime.now()
  #   for lesson in self.lessons:
  #     learnedTime=datetime.datetime.now()-self.startTime
  #     self.processInputStr.set('{0}/{1}'.format(self.curIdx,cnt))
  #     # learnedTimeInputStr.set('{0}时{1}分{2}秒'.format(learnedTime.hours,learnedTime.minutes,learnedTime.seconds))
  #     self.learnedTimeInputStr.set('{0}分'.format(learnedTime.seconds/60))
  #     if lesson['btn']!='重新学习':
  #       pfCatcher.getPage("https://perfect.zhixueyun.com/#/study/course/detail/10&{0}/6/1".format(lesson['attachmentId']))
  #       time.sleep(900)#1)#(900)
  #     self.curIdx+=1
    
  #   self.processInputStr.set("已完成")
  #   self.loginInput.config(state='normal',text='重新学习')
  #   if self.autoShutdownInt.get()==1:
  #     os.system('shutdown -s -f -t 59')

  def playLesson(self,pfCatcher):  
    self.curIdx=0
    cnt=len(self.lessons)

    while self.curIdx<cnt:
      lesson=self.lessons[self.curIdx]
      if ('btn' not in lesson) or lesson['btn']!='重新学习':
        self.playCurLesson(pfCatcher)
        time.sleep(10)#(900)
        finishCnt=0
        while finishCnt==0:
          learnedTime=datetime.datetime.now()-self.startTime
          self.learnedTimeInputStr.set('{0}分'.format(round(learnedTime.seconds/60,2)))
          finishDom=BeautifulSoup(pfCatcher.getHtml(), 'lxml').find('div', text="您已完成该课程的学习")

          if finishDom is not None:
            finishCnt=1
          else:
            time.sleep(20)

      self.curIdx+=1

  def login(self):
      if tk.messagebox.askokcancel(title='Hi', message=self.userNameInputStr.get()):
        self.loginInput.config(state="disabled")
        # self.playCurPageInput.config(state="disabled")
        if self.isLogin==1:#如果是已登陆的状态,就播放当前打开的页面,而不是lessonUrlInputStr
          self.playCurPage()
        else :
          self.pfCatcher=PFPageCatcher(self.userNameInputStr.get(),self.userPwdInputStr.get())
          self.pfCatcher.login()
          self.isLogin=1
        
          html=self.pfCatcher.getHtml()
          lessonPage=self.pfCatcher.getPage(self.lessonUrlInputStr.get())      
          self.pageInput.insert(1.0,html)
          self.lessonInput.insert(1.0,lessonPage)

          if self.startAfterLoginInt.get()==1:            
            self.playCurPage()
          else:
            self.loginInput.config(state='normal',text='开始学习')


if __name__=='__main__':
    form=PfCatcherForm()
