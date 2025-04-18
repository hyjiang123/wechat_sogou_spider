import urllib.request
import re
from bs4 import BeautifulSoup

def get_proxy():
    pattern1 = r'<table id="proxylister-table" class="m-0" border="1">.*?<div id="proxylister-info" class="float-end mt-3">'
    url = "https://proxycompass.com/cn/free-proxy/"
    headers = {"User-Agent",
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    html = opener.open(url).read()
    table = re.findall(pattern1, str(html))
    table = table[0]

    # soup1 = BeautifulSoup(table, 'html.parser')
    # thead_elements = [th.get_text() for th in soup1.find_all('th')]
    # print(thead_elements)

    soup2 = BeautifulSoup(table, 'html.parser')
    tbody = soup2.find_all('tbody')[0]
    trs = tbody.find_all('tr')
    result = []
    for tr in trs:
        tds = tr.find_all('td')
        elements = []
        for td in tds:
            element = td.get_text().strip()
            elements.append(element)
        result.append(elements)

    urlList = []

    for item in result:
        ele = item[0] + ":" + item[1]
        urlList.append(ele)

    return urlList

# get_proxy()