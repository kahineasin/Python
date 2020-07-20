# coding:utf-8
from selenium import webdriver
 
driver = webdriver.Chrome()
driver.get("https://www.taobao.com/")
# 淘宝首页handle
handle = driver.current_window_handle
driver.find_element_by_link_text("女装").click()
# 获取所有handle
handles = driver.window_handles

driver.close()
# 切换到淘宝首页
driver.switch_to.window(handles[0])
 
# for i in handles:
#     if i != handle:
#         # 切换到淘宝首页
#         driver.switch_to.window(handle)
driver.quit()