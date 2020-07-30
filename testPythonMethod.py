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
from Perfect import PFDataHelper 

class PfCatcherForm:
  def __init__(self):
    add=lambda x, y: x+y
    PFDataHelper.GetPage(None,None,add)
    # #测试时间
    # nowtime = datetime.datetime.now().strftime('%Y-%m-%d');
    # print(nowtime)
    # print(nowtime==datetime.datetime.now().strftime('%Y-%m-%d'))

if __name__=='__main__':
    form=PfCatcherForm()
