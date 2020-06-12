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
    #测试时间
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d');
    print(nowtime)
    print(nowtime==datetime.datetime.now().strftime('%Y-%m-%d'))

if __name__=='__main__':
    form=PfCatcherForm()
