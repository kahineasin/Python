[git]
git push --set-upstream https://github.com/kahineasin/Python.git master
git push --set-upstream https://gitee.com/sellgirl/Python.git master
https://github.com/kahineasin/Python.git
https://gitee.com/sellgirl/Python.git


当前看到课程第7页

改可选列表样式2:
https://perfect.zhixueyun.com/#/study/course/index

一些常用命令:
  pyi-makespec catchPageApp.py
  pyinstaller .\catchPageApp.spec  

代码来自:
https://www.jianshu.com/p/aa258a81f5da

捕抓动态网页

cmd安装依赖:
pip install requests 
pip install lxml-4.5.0-cp37-cp37m-win_amd64.whl
pip3 install selenium

需要下载浏览器驱动:
https://www.selenium.dev/
https://pypi.org/project/selenium/
http://npm.taobao.org/mirrors/chromedriver/

Firefox-full-latest-win64_v76.0.1.zip  对应  geckodriver-v0.26.0-win64.zip

电脑浏览器版本为 83.0.4103.61（正式版本） （64 位） 时，如果使用 chromedriver_win32_83.0.4103.39 ,偶尔会报错：
[0525/134338.359:ERROR:gl_surface_egl.cc(750)] EGL Driver message (Error) eglQue
ryDeviceAttribEXT: Bad attribute.
但似乎不影响程序的运行

运行:
python catchPage.py
python getCookie.py

待尝试的方法：
1.用webdriver.Firefox()打开页面，手动find_element_by_xpath("xxx").click()登陆

登陆:
https://zxy9.zhixueyun.com/oauth/api/v1/auth
key=oZImo5zozQggF2BymfTc090trJ3N6xyWfo18%2F8Lp7jTh8l2v5iCDg5phuOMsAthCWpnEJqsiMBtxMaMJ%2B1oBvaY4o9ONCHnNuQ636V9wYD3w6DpxbQojzwTJTXvO5A4naQToc6WyGn%2FZQzVCfTb%2FZHbE9n1fYt0vYI4VFwXKaTA6Tat8KQgvApOL69rDME2r0039DIBeJco3Us0l2I422FpNXnwkg0YZvW25RuSKKJ0%3D&
organization_id=MhWc4Po8qmaJpjBZTtZV%2FvzWDNrS6%2Bm%2B38Rn3E8jigd6vnra%2BL4edfeKJL6eB2BL&
login_method=JZNm%2B1f9txtGtiE0oRMJ1g%3D%3D&
username=6NDtwKSc8%2FmSvJ577UxTsA%3D%3D&
pword=W1tl9ctj1QpoN%2F0oArzwSQ%3D%3D&
captcha=&
remember=U5odry%2BhxJVf%2FJHFehA%2FoA%3D%3D

响应
{"access_token":"0e13604ea8b60621a53a10eff7d57e65","state":"/home","redirect_uri":"https://perfect.zhixueyun.com","token_type":"Bearer","expires_in":3600}


查询课程的时间:
https://perfect.zhixueyun.com/api/v1/course-study/course-front/info/736fb57d-b2fd-4177-8423-95ced6a667c5?type=6&_=1589876644500

响应
{addType: 1, avgScore: 80, businessType: 0, courseAttachments: [],…}
addType: 1
avgScore: 80
businessType: 0
courseAttachments: []
courseChapters: [{courseChapterSections: [{attachmentId: "9ab1aed5-cabe-4fb8-ab1a-f4584e1247c1",…}],…}]
courseHour: 0.11
cover: "0edcd022-0cf7-4ee1-bd16-e5983416d608"
coverPath: "default/M00/00/13/Ci7mTVqRB5yAXvyZAAFL83e5qSE761.jpg"
credit: 1
description: "【课程简介】在工作中，人们往往感到时间不够用，因而产生了时间上的压力感。本课程主要介绍如何利用时间压力。"
id: "736fb57d-b2fd-4177-8423-95ced6a667c5"
learnSequence: 0
lecturer: ""
name: "利用时间压力"
publishClient: 0
releaseOrg: {id: "1cd955e1-ed84-47b8-9333-91e7838fa904", name: "完美知行学院"}
shelveTime: 1576808282978
source: 8
studyProgress: {currentResourceId: "9ab1aed5-cabe-4fb8-ab1a-f4584e1247c1",…}

登陆页的cookie:
            cookie.Add(new Cookie("acw_tc", "781bad2915898671495572963e5494d49834d8d8a728eac2b6a269bbe3b732","/", ".zhixueyun.com"));
            cookie.Add(new Cookie("captcha","adb64d17-f87a-44cb-af7c-ee2c97648909", "/", ".zhixueyun.com"));

[更新进度的api]
似乎是:https://perfect.zhixueyun.com/api/v1/course-study/course-front/course-section-progress
resourceIds: b0164c5a-7200-4866-8396-ac7e6664ca87
courseId: 5bb639fc-8583-41fb-81ad-6008c4b5e5ea
从上面看不出怎么可以一下完成课程