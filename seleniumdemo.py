from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import proxynet_spider
import random


def selenium_getdata(url):
    # proxy_list = proxynet_spider.get_proxy()
    # proxy_random = random.choice(proxy_list)
    proxy_random = "113.108.13.120:4433"

    # 设置代理
    proxy = proxy_random
    print("使用的代理地址为： " + proxy)
    capabilities = DesiredCapabilities.EDGE.copy()
    capabilities['proxy'] = {
        'proxyType': 'MANUAL',
        'httpProxy': proxy,
        'sslProxy': proxy,
    }

    # 使用 WebDriver Manager 自动下载并配置 msedgedriver
    driver = webdriver.Edge(executable_path=r'D:\anaconda\envs\env36\Lib\msedgedriver.exe', capabilities=capabilities)

    # 打开网页
    driver.get(url)
    driver.set_page_load_timeout(30)
    html_data = driver.page_source
    print("html_data:" + str(html_data))
    # 关闭浏览器
    driver.quit()
    return html_data