from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PFPageCatcher:
    'Perfect爬虫类'
    def __init__(self, name, salary):
      self.name = name
      self.salary = salary

def main():
    #driver = webdriver.Firefox()
    #driver = webdriver.Chrome()

    #https需要
    profile=webdriver.FirefoxProfile()
    profile.accept_untrusted_certs=True
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_page_load_timeout(5000)
    #尝试登陆:https://www.cnblogs.com/andy9468/p/10901608.html
    loginUrl="https://zxy9.zhixueyun.com/oauth/#login/cmVzcG9uc2VfdHlwZT10b2tlbiZjbGllbnRfaWQ9OTk5JnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRnBlcmZlY3QuemhpeHVleXVuLmNvbSZzdGF0ZT0lMkZob21lJmxhbmc9Y24mY2FuY2VsUmVtZW1iZXJTdGF0ZT0w"
    #loginUrl="http://192.168.0.26:28102/User/Login?ReturnUrl=%2f"
    driver.get(loginUrl)
    #driver.get(u'https://zxy9.zhixueyun.com/oauth/#login/cmVzcG9uc2VfdHlwZT10b2tlbiZjbGllbnRfaWQ9OTk5JnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRnBlcmZlY3QuemhpeHVleXVuLmNvbSZzdGF0ZT0lMkZob21lJmxhbmc9Y24mY2FuY2VsUmVtZW1iZXJTdGF0ZT0w')    
    #soup = BeautifulSoup(driver.page_source, 'lxml')
    print('打开了页面')

    time.sleep(5) #driver.get之后要等待页面加载完(有的情况下get会自动等待加载完)--benjamin
#     # 点击账号和密码登录
    #input_username = driver.find_element_by_xpath("//input[@name='userid']")
    # input_password = driver.find_element_by_xpath("//input[@name='password']")
    # input_box0 = driver.find_element_by_xpath("//input[@class='btn']")
    
    input_username = driver.find_element_by_xpath("//input[@name='username']")
    #input_username = driver.find_element_by_xpath("//input[@id='D37username']")
    input_password = driver.find_element_by_xpath("//input[@name='pword']")
    input_box0 = driver.find_element_by_xpath("//button[@class='btn-login']")

    input_username.send_keys(u"1712002")
    input_password.send_keys(u"123456a")
    # # input_username.__setattr__("value","aaaa")
    # # input_username.value="aaa"
    input_box0.click()

    print('点击了登陆按钮')
    time.sleep(5)
    #捕抓页面
#     #driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
#     driver.get('https://perfect.zhixueyun.com/#/study/subject/detail/a785316d-1f4d-4a8c-b187-cd745d5e62d3')
    
    #print(driver.page_source)

    # print(soup)
    #time.sleep(5)
    #soup = BeautifulSoup(driver.page_source, 'lxml')
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print('BeautifulSoup')
    # for img_tag in soup.body.select('input[name]'):
    #     print(img_tag.attrs['name'])
#     for img_tag in soup.body.select('img[src]'):
#         print(img_tag.attrs['src'])


    # #捉视频列表
    videoListUrl="https://perfect.zhixueyun.com/#/study/subject/detail/a4068ba4-891e-4b04-8aca-c1365bd68fb2"
    driver.get(videoListUrl)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    print(soup.body)
    # print('BeautifulSoup')
    # for img_tag in soup.body.select('li[class=list-item] a'):
    #   print(img_tag.attrs['href'])
    
    # soup = BeautifulSoup(driver.page_source, 'lxml')
    # # print('BeautifulSoup')
    # for img_tag in soup.body.select('div[class=list-bar] a'):
    #   print(img_tag.attrs['href'])

if __name__ == '__main__':
    main()