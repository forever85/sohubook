
import asyncio
import time
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://www.sohu.com/a/522508635_121315445")
        page.wait_for_load_state('networkidle')
        await page.mouse.wheel(0,700000)
        time.sleep(20)
        html = await page.content()
        elements = await page.query_selector_all('#mp-editor > p > img')
        urls=[]
        for element in elements:
            urls.append(await element.get_attribute('src') )  
        #print(await page.title())
        print(urls)
        '''
        with open ('d:\\2.txt','w+',encoding='UTF-8') as f:
            
            await f.write(html)
        await browser.close()'''
asyncio.run(main())