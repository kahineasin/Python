[git]
git push --set-upstream https://github.com/kahineasin/Python.git master
git push --set-upstream https://gitee.com/sellgirl/Python.git master
https://github.com/kahineasin/Python.git
https://gitee.com/sellgirl/Python.git


��ǰ�����γ̵�7ҳ

�Ŀ�ѡ�б���ʽ2:
https://perfect.zhixueyun.com/#/study/course/index

һЩ��������:
  pyi-makespec catchPageApp.py
  pyinstaller .\catchPageApp.spec  

��������:
https://www.jianshu.com/p/aa258a81f5da

��ץ��̬��ҳ

cmd��װ����:
pip install requests 
pip install lxml-4.5.0-cp37-cp37m-win_amd64.whl
pip3 install selenium

��Ҫ�������������:
https://www.selenium.dev/
https://pypi.org/project/selenium/
http://npm.taobao.org/mirrors/chromedriver/

Firefox-full-latest-win64_v76.0.1.zip  ��Ӧ  geckodriver-v0.26.0-win64.zip

����������汾Ϊ 83.0.4103.61����ʽ�汾�� ��64 λ�� ʱ�����ʹ�� chromedriver_win32_83.0.4103.39 ,ż���ᱨ��
[0525/134338.359:ERROR:gl_surface_egl.cc(750)] EGL Driver message (Error) eglQue
ryDeviceAttribEXT: Bad attribute.
���ƺ���Ӱ����������

����:
python catchPage.py
python getCookie.py

�����Եķ�����
1.��webdriver.Firefox()��ҳ�棬�ֶ�find_element_by_xpath("xxx").click()��½

��½:
https://zxy9.zhixueyun.com/oauth/api/v1/auth
key=oZImo5zozQggF2BymfTc090trJ3N6xyWfo18%2F8Lp7jTh8l2v5iCDg5phuOMsAthCWpnEJqsiMBtxMaMJ%2B1oBvaY4o9ONCHnNuQ636V9wYD3w6DpxbQojzwTJTXvO5A4naQToc6WyGn%2FZQzVCfTb%2FZHbE9n1fYt0vYI4VFwXKaTA6Tat8KQgvApOL69rDME2r0039DIBeJco3Us0l2I422FpNXnwkg0YZvW25RuSKKJ0%3D&
organization_id=MhWc4Po8qmaJpjBZTtZV%2FvzWDNrS6%2Bm%2B38Rn3E8jigd6vnra%2BL4edfeKJL6eB2BL&
login_method=JZNm%2B1f9txtGtiE0oRMJ1g%3D%3D&
username=6NDtwKSc8%2FmSvJ577UxTsA%3D%3D&
pword=W1tl9ctj1QpoN%2F0oArzwSQ%3D%3D&
captcha=&
remember=U5odry%2BhxJVf%2FJHFehA%2FoA%3D%3D

��Ӧ
{"access_token":"0e13604ea8b60621a53a10eff7d57e65","state":"/home","redirect_uri":"https://perfect.zhixueyun.com","token_type":"Bearer","expires_in":3600}


��ѯ�γ̵�ʱ��:
https://perfect.zhixueyun.com/api/v1/course-study/course-front/info/736fb57d-b2fd-4177-8423-95ced6a667c5?type=6&_=1589876644500

��Ӧ
{addType: 1, avgScore: 80, businessType: 0, courseAttachments: [],��}
addType: 1
avgScore: 80
businessType: 0
courseAttachments: []
courseChapters: [{courseChapterSections: [{attachmentId: "9ab1aed5-cabe-4fb8-ab1a-f4584e1247c1",��}],��}]
courseHour: 0.11
cover: "0edcd022-0cf7-4ee1-bd16-e5983416d608"
coverPath: "default/M00/00/13/Ci7mTVqRB5yAXvyZAAFL83e5qSE761.jpg"
credit: 1
description: "���γ̼�顿�ڹ����У����������е�ʱ�䲻���ã����������ʱ���ϵ�ѹ���С����γ���Ҫ�����������ʱ��ѹ����"
id: "736fb57d-b2fd-4177-8423-95ced6a667c5"
learnSequence: 0
lecturer: ""
name: "����ʱ��ѹ��"
publishClient: 0
releaseOrg: {id: "1cd955e1-ed84-47b8-9333-91e7838fa904", name: "����֪��ѧԺ"}
shelveTime: 1576808282978
source: 8
studyProgress: {currentResourceId: "9ab1aed5-cabe-4fb8-ab1a-f4584e1247c1",��}

��½ҳ��cookie:
            cookie.Add(new Cookie("acw_tc", "781bad2915898671495572963e5494d49834d8d8a728eac2b6a269bbe3b732","/", ".zhixueyun.com"));
            cookie.Add(new Cookie("captcha","adb64d17-f87a-44cb-af7c-ee2c97648909", "/", ".zhixueyun.com"));

[���½��ȵ�api]
�ƺ���:https://perfect.zhixueyun.com/api/v1/course-study/course-front/course-section-progress
resourceIds: b0164c5a-7200-4866-8396-ac7e6664ca87
courseId: 5bb639fc-8583-41fb-81ad-6008c4b5e5ea
�����濴������ô����һ����ɿγ�