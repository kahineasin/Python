import urllib.request
from http import cookiejar

def main():
    #loginUrl = "http://hi.baidu.com/motionhouse"
    #https://perfect.zhixueyun.com/#/study/subject/detail/a785316d-1f4d-4a8c-b187-cd745d5e62d3
    
    loginUrl = "https://perfect.zhixueyun.com/#/study/subject/detail/a785316d-1f4d-4a8c-b187-cd745d5e62d3"
    cj = cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)
    resp = urllib.request.urlopen(loginUrl) 

    for index, cookie in enumerate(cj):
        print ('[',index, ']',cookie)

if __name__ == '__main__':
    main()