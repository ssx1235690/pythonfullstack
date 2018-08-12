
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 17:46
# @Author  : sxsong
# @Site    : 
# @File    : 25-day截图.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 启动driver
def init_web_driver():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver_path = 'C:\Users\ronglian\Desktop\chromedriver.exe'  # 这里放的就是下载的driver本地路径
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_path)


# 关掉driver
def close_web_driver():
    driver.quit()


def get_data():
    # driver.get("http://www.cnblogs.com/yuanchenqi/articles/5976755.html")
    driver.get("http://www.baidu.com")


    driver.implicitly_wait(10)  # wait up to 10 seconds for the elements to become available
    # ======  网页中静态部分抓取，采用BeautifulSoup去解析
    html = driver.page_source  # 获取网页html
    html_soup = BeautifulSoup(html.text, "lxml")
    time.sleep(0.1)
    coin_list = html_soup.find(name='table', attrs={"class": "table maintable"})
    # 页面元素的提取请查看 BeautifulSoup的用法
    # ====== 网页中动态部分抓取，采用driver自带的方法
    # 下面展示的从调用百度搜索，在搜索框中输入"headless chrome"，然后获取结果。具体自行百度driver的用法
    text = driver.find_element_by_css_selector('#kw')
    search = driver.find_element_by_css_selector('#su')
    text.send_keys('headless chrome')
    # search
    search.click()
    driver.get_screenshot_as_file('C:\Users\ronglian\Desktop\search-result.png')
    results = driver.find_elements_by_xpath('//div[@class="result c-container "]')
    for result in results:
        res = result.find_element_by_css_selector('a')
        title = res.text
        link = res.get_attribute('href')
        print('Title: %s \nLink: %s\n' % (title, link))

if __name__ == '__main__':
    init_web_driver()
    get_data()
    close_web_driver()