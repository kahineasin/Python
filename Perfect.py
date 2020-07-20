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
import os
import urllib
import urllib.request
import winreg
import re
import sys
import zipfile

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
  @staticmethod
  def unzip_single(src_file, dest_dir, password=None):
    if password:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        raise OSError('Occurred an exception while extracting zip file. ')
    zf.close()
  @staticmethod
  def DownloadDriverForChrome(currentFullChromeVersion):    
    DriverVersions = {
        '73':'2.46',
        '72':'2.46',
        '71':'2.46',
        '70':'2.45',
        '69':'2.44',
        '68':'2.42',
        '67':'2.41',
        '66':'2.40',
        '65':'2.38',
        '64':'2.37',
        '63':'2.36',
        '62':'2.35',
        '61':'2.34',
        '60':'2.33',
        '59':'2.32',
        '58':'2.31',
        '57':'2.29',
        '56':'2.29',
        '55':'2.28',
        '54':'2.27',
        '53':'2.26',
        '52':'2.24',
        '51':'2.23',
        '50':'2.22',
        '49':'2.22',
        '48':'2.21',
        '47':'2.21',
        '46':'2.21',
        '45':'2.20',
        '44':'2.20',
        '43':'2.20',
        '42':'2.16',
        '41':'2.15',
        '40':'2.15',
        '39':'2.14',
        '38':'2.13',
        '37':'2.12',
        '36':'2.12',
        '35':'2.10',
        '34':'2.10',
        '33':'2.10',
        '32':'2.9',
        '31':'2.9',
        '30':'2.8',
        '29':'2.7'
    }

    FullChromeVersion=''
    try:
      FullChromeVersion = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'),'DisplayVersion')[0]
    except BaseException as e:
      try:
        FullChromeVersion = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER,'Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'),'DisplayVersion')[0]
      except BaseException as e1:
        print(e1)

    if FullChromeVersion==currentFullChromeVersion:
      return currentFullChromeVersion
    ChromeVersion = int(FullChromeVersion.split('.')[0])
    print('Chrome version: '+FullChromeVersion)
    if ChromeVersion <= 73:
        if not str(ChromeVersion) in DriverVersions:
            raise KeyError('There isn\'t a chromedriver that supports your Chrome version. ')
        try:
            urllib.request.urlretrieve('https://npm.taobao.org/mirrors/chromedriver/'+DriverVersions[str(ChromeVersion)]+'/chromedriver_win32.zip','chromedriver_win32.zip')
        except:
            print('Can\'t connect to the server! ')
            raise ConnectionError('Can\'t connect to the server')
        else:
            print('Extracting file... ')
            PFDataHelper.unzip_single('chromedriver_win32.zip','')
            print('Download successfully. ')
    else:
        AvailableVersions = {}
        try:
            urlRead = urllib.request.urlopen(urllib.request.Request('https://npm.taobao.org/mirrors/chromedriver/')).read().decode()
        except:
            print('Can\'t connect to the server! ')
            raise ConnectionError('Can\'t connect to the server')
        else:
            for i in re.findall('<a href="/mirrors/chromedriver/(.*?)</a>',urlRead):
                if i[0] in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' or 'RELEASE' in i or int(i.split('.')[0]) <= 72:
                    continue
                if not i.split('.')[0] in AvailableVersions:
                    AvailableVersions[i.split('.')[0]] = i.split('/">')[0]
            if not str(ChromeVersion) in AvailableVersions:
                raise KeyError('There isn\'t has a chromedriver that supports your Chrome version. ')
            try:
                print('Downloading... \nURL:https://npm.taobao.org/mirrors/chromedriver/'+AvailableVersions[str(ChromeVersion)]+'/chromedriver_win32.zip')
                urllib.request.urlretrieve('https://npm.taobao.org/mirrors/chromedriver/'+AvailableVersions[str(ChromeVersion)]+'/chromedriver_win32.zip','chromedriver_win32.zip')
            except:
                print('Download failed. ')
            else:
                print('Extracting file... ')
                PFDataHelper.unzip_single('chromedriver_win32.zip','')
                print('Download successfully. ')
    return FullChromeVersion

