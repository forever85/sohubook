from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup
import requests
import time
'''
# 设置滚动高度 创建滚动函数*

def scroll(page):
    page.evaluate('window.scrollBy(0, 2000)')


# 创建核心函数，递归向下滚动直到页面加载完全部内容
def scrollDownUntilEnd(page):
    prevHeight = page.evaluate('document.body.clientHeight')
    print(prevHeight)
    scroll(page)
    page.wait_for_timeout(5000)
    newHeight = page.evaluate('document.body.clientHeight')
    print(newHeight)
    if (newHeight > prevHeight):

#    // 如果页面高度发生改变，则继续递归滚动
        scrollDownUntilEnd(page)
  


#// 调用滚动函数，滚动特定次数
def scrollDownMultipleTimes(page, times) {
  for (let i = 0; i < times; i++) {
    await scroll(page);
    await page.waitForTimeout(1000);
  }
}'''



#// 调用函数，向下滚动特定次数
#await scrollDownMultipleTimes(page, 5);

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.sohu.com/a/684486017_121708522")
    
    page.mouse.wheel(0,17000)
    page.wait_for_timeout(20000)
#// 调用函数，滚动至底部
    #scrollDownUntilEnd(page)
    
    res = page.content()
    beau = BeautifulSoup(res,'lxml')
    images = beau.select(".ql-align-center img")
    urls =[]
    for img in images:
        urls.append(img['src'])
        print(img['src'])
    page.close()
    context.close()
    browser.close()
    getdown(urls)
def getdown(urls):
    
    he ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    for page,url in enumerate(urls):
        if len(str(page)) == 1:
            page = '00' + str(page)
        elif len(str(page)) == 2:
            page = '0' + str(page)
        else:
            page = str(page)
        print('正在下载第' + str(urls.index(url)) +"张图书！")
        re = requests.get('https:'+ url,headers = he)
        if re.status_code == 200:
            with open("d:/temp/" + page + ".jpg",'wb') as fs:
                fs.write(re.content)
        time.sleep(1)
    print("------------------OK-------------------")

with sync_playwright() as playwright:
    run(playwright)


