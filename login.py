import crifanLib;
import urllib.request
from http import cookiejar

def main():
    crifanLib.initAutoHandleCookies()
    #loginUrl = "http://hi.baidu.com/motionhouse"
    #https://perfect.zhixueyun.com/#/study/subject/detail/a785316d-1f4d-4a8c-b187-cd745d5e62d3
    baiduSpaceEntryUrl ="https://zxy9.zhixueyun.com/oauth/#login/cmVzcG9uc2VfdHlwZT10b2tlbiZjbGllbnRfaWQ9OTk5JnJlZGlyZWN0X3VyaT1odHRwcyUzQSUyRiUyRnBlcmZlY3QuemhpeHVleXVuLmNvbSZzdGF0ZT0lMkZob21lJmxhbmca9Y24mY2FuY2VsUmVtZW1iZXJTdGF0ZT0w";
    loginUrl = "https://zxy9.zhixueyun.com/oauth/api/v1/auth"
    #loginUrl = "http://localhost:38201/python/postcode"
    #loginUrl = "https://pay.sellgirl.com:44303/posttestbycode?code=ben" #ok
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(baiduSpaceEntryUrl) 

    postDict = {
      'code':"benjamin 吴肖均",            
            'key'  : "oZImo5zozQggF2BymfTc090trJ3N6xyWfo18%2F8Lp7jTh8l2v5iCDg5phuOMsAthCWpnEJqsiMBtxMaMJ%2B1oBvaY4o9ONCHnNuQ636V9wYD3w6DpxbQojzwTJTXvO5A4naQToc6WyGn%2FZQzVCfTb%2FZHbE9n1fYt0vYI4VFwXKaTA6Tat8KQgvApOL69rDME2r0039DIBeJco3Us0l2I422FpNXnwkg0YZvW25RuSKKJ0%3D",
            'organization_id'  : "MhWc4Po8qmaJpjBZTtZV%2FvzWDNrS6%2Bm%2B38Rn3E8jigd6vnra%2BL4edfeKJL6eB2BL",
            'login_method'  : 'JZNm%2B1f9txtGtiE0oRMJ1g%3D%3D',
            'username'  : '6NDtwKSc8%2FmSvJ577UxTsA%3D%3D',
            'pword'  : 'W1tl9ctj1QpoN%2F0oArzwSQ%3D%3D',
            'captcha'  : '',
            'remember'  : 'U5odry%2BhxJVf%2FJHFehA%2FoA%3D%3D',

        #     'username'  : "username",
        #     'password'  : password,
            'mem_pass'  : 'on',
            
            'charset'   : "UTF-8",
            'isPhone'   : "false",
            'index'     : "0",
            'safeflag'  : "0",
            #'staticpage': "http://hi.baidu.com/com/show/proxy?parent=parent&fun=callback.login.submited",
            'loginType' : "1",
            'tpl'       : "qing"
        #     'token'     : loginToken,
            }

    headerDict = {
      'Accept':"*/*",  
      'Content-Type':"application/x-www-form-urlencoded; charset=UTF-8",  
      'Referer':"https://zxy9.zhixueyun.com/oauth/",  
      'Accept-Language':"zh-CN",  
      'Accept-Encoding':"gzip, deflate",  
      'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",  
      'Host':"zxy9.zhixueyun.com",  
      'Content-Length':"513",  
      'DNT':"1",  
      'Connection':"Keep-Alive",  
      'Cache-Control':"no-cache",  
      'Cookie':"acw_tc=76b20f4315899662000366714e8c5255149d81af72ecbbdc8b45d5c6637dbd; captcha=92efb6c3-275a-4e59-9cd5-9fad762d6ee6"  

            }

    try:
      resp = crifanLib.getUrlResponse(loginUrl, postDict,headerDict)
      data = resp.read()
      print (data.decode('utf8'))
    except urllib.request.HTTPError as e:
      print (e.code,"\r\n")
      print (e.reason,"\r\n")
      print (e)
    except urllib.request.URLError as e:  
      print (e.reason,"\r\n")
      print (e)
#     print (data)
#     for index, cookie in enumerate(cj):
#         print ('[',index, ']',cookie)

if __name__ == '__main__':
    main()