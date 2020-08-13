#更换桌面壁纸的程序
import requests
import json
import random
import os
from requests.exceptions import RequestException
import win32api, win32gui, win32con
import time
import configparser
#存放Ajax图片地址数据 
img_url_dict={}
#创建图片tmp文件夹
if not os.path.exists('image'):
  os.mkdir('image')
#爬取图片url地址
def getImgurl(root_url,sn):
  params={
    'ch': 'wallpaper',
    't1': 157,
    'sn': sn,
    'listtype': 'new',
    'temp': 1
  }
  headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko)Chrome/62.0 3202.62 Safari / 537.36'
  }
  try:
    response=requests.get(root_url,params=params,headers=headers)
  except RequestException:
    return None
  data=json.loads(response.text).get('list')
  img_url_list=[]
  for item in data:
    img_url_list.append(item.get('cover_imgurl'))
  img_url_dict[sn]=img_url_list
#下载图片
def download_image(name,image_url):
  try:
    response=requests.get(image_url)
  except RequestException:
    return "图像请求出错"
  file_name='{}/{}.{}'.format('image',name,'bmp');
  with open(file_name,'wb') as file:
    file.write(response.content)
#获取随机url地址并下载至image文件夹
def get_img():
  sn=30*random.randint(1,15)
  try:
    img_url_dict[sn]
  except KeyError:
    getImgurl('http://image.so.com/zj',sn) #此url已不能找到图片
    #getImgurl('https://image.so.com/z?ch=wallpaper#/',sn) #http://image.so.com/zj
  index=random.randint(0,len(img_url_dict[sn])-1)
  url=img_url_dict[sn][index]
  download_image('wallpaper',url)


def setWallPaper(pic):
  # open register
  regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
  win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
  win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
  # refresh screen
  win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)

if __name__=='__main__':
  config = configparser.ConfigParser()
  conf_file = open("changePcBackgroundImg_config.ini")
  config.read_file(conf_file)

  currentPcDeskImg=config.get("sysInfo","currentPcDeskImg")
  pcDeskImgUpdateTime=config.get("sysInfo","pcDeskImgUpdateTime")
  conf_file.close()

  responseTest=requests.get('https://pay.sellgirl.com:44303/getpcdeskimgname').text
  newestPcDeskImgJson=json.loads(responseTest)
  newestPcDeskImg=newestPcDeskImgJson.get('data').get('imgName')
  lastModified=newestPcDeskImgJson.get('data').get('lastModified')
  if newestPcDeskImg!=currentPcDeskImg or str(lastModified)!=pcDeskImgUpdateTime:
    #开机时换一次
    # download_image('wallpaper','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1597297112077&di=9869dc1ad502363bfbdeba6b72b259be&imgtype=0&src=http%3A%2F%2Ft8.baidu.com%2Fit%2Fu%3D1484500186%2C1503043093%26fm%3D79%26app%3D86%26f%3DJPEG%3Fw%3D1280%26h%3D853')
    download_image('wallpaper','https://pay.sellgirl.com:44303/pcdeskimg.jpg')
    
    # pic='your_path/image/wallpaper.bmp'#写绝对路径
    pic='image/wallpaper.bmp'#可用相对路径
    setWallPaper(pic)

    config = configparser.ConfigParser()
    conf_file = open("changePcBackgroundImg_config.ini")
    config.read_file(conf_file)
    conf_file.close()
    config.set("sysInfo","currentPcDeskImg",newestPcDeskImg)
    config.set("sysInfo","pcDeskImgUpdateTime",str(lastModified))

    file_write = open("changePcBackgroundImg_config.ini","w")
    config.write(file_write) 
    file_write.close()


  #定时换
  # while True:
  #   get_img()
  #   pic='your_path/image/wallpaper.bmp'#写绝对路径
  #   setWallPaper(pic)
  #   time.sleep(6)#6s切换一次壁纸