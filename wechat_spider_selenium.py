import re
import urllib.request
import time
import urllib.error
import seleniumdemo
import random
from time import sleep


listurl = []

def url_decode(r):
    url = 'https://weixin.sogou.com' + r
    b = random.randint(0, 99)
    a = url.index('url=')
    a = url[a + 30 + b:a + 31 + b:]
    url += '&k=' + str(b) + '&h=' + a
    return url

def getlisturl(key, pagestart, pageend):
    try:
        page = pagestart
        keycode = urllib.request.quote(key)
        # pagecode = urllib.request.quote("&page=")
        pagecode = "&page="
        for page in range(pagestart, pageend + 1):
            url = "http://weixin.sogou.com/weixin?type=2&query=" + keycode + pagecode + str(page)
            data1 = seleniumdemo.selenium_getdata(url)
            listurlpat = '<div class="txt-box">.*?</li>'
            print("匹配到的信息： " + str(re.compile(listurlpat, re.S).findall(data1)))
            listurl.append(re.compile(listurlpat, re.S).findall(data1))
        print("共获取到 " + str(len(listurl)) + " 页")
        return listurl
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:" + str(e))
        time.sleep(1)

def getcontent(listurl):
    i = 0
    html1 = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8"> <!-- 设置字符编码为 UTF-8 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- 响应式设计 -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- 兼容性设置 -->
    <title>微信文章首页</title> <!-- 页面标题 -->
</head>
<body>'''
    fh = open("3.html", "wb")
    fh.write(html1.encode('utf-8'))
    fh.close()

    fh = open("3.html", "ab")
    for i in range(0, len(listurl)):
        for j in range(0, len(listurl[i])):
            try:
                url = listurl[i][j]
                # url = url.replace("amp;","")
                # data = seleniumdemo.selenium_getdata(url)
                data = url
                titlepat = '<em>(.*?)<\/a>'
                contentpat = 'href="([^"]+)"'
                title = re.compile(titlepat).findall(data)
                content = re.compile(contentpat).findall(data)

                thistitle = "此次没有获取到"
                thiscontent = "此次没有获取到"
                if(title != []):
                    thistitle = title[0]

                if(content != []):
                    thiscontent = content[0]
                    thiscontent = url_decode(thiscontent)

                dataall = "<p>标题为 :" + thistitle + "</p><p>" + "<a href=" + thiscontent + ">文章链接</a>" + "</p><br>"
                fh.write(dataall.encode('utf-8'))
                print("第" + str(i) + " 个网页第" + str(j) + " 次处理")
            except urllib.error.URLError as e:
                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print("exception:" + str(e))
                time.sleep(1)
    fh.close()
    html2 = '''</body>
</html>'''
    fh = open("3.html", "ab")
    fh.write(html2.encode('utf-8'))
    fh.close()

key = "物联网"
pagestart = 1
pageend = 3
listurl = getlisturl(key, pagestart, pageend)
getcontent(listurl)

