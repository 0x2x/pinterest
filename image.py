"""
    This pinterest tool is my first project with pyppeteer i dont have much to say but if you decide to use it please dont:
        1. sell the free tool
        2. claim it as yours and give me proper credits
"""

import asyncio
from aiohttp import ClientSession
from colorama import Fore
from pyppeteer import launch
import re 

file = open("imgs.js")

EMAIL = 'EMAIL@wtc.com' # Change with your EMAIL
password = 'password' # Change with your PASSWORD

def design(session:str=None):
    if session is None:
        return f"""
            Created by saturn#1111, This is my first project with pyppeteer
                # first time using pyppeteer
            {Fore.BLUE}
                                    .;;,
            .,.               .,;;;;;,{Fore.RESET}
            {Fore.WHITE};;;;;;;,,        ,;;%%%%%;;{Fore.RESET}
            {Fore.RED}`;;;%%%%;;,.  ,;;%%;;%%%;;{Fore.RESET}
            {Fore.CYAN}`;%%;;%%%;;,;;%%%%%%%;;'{Fore.RESET}
                `;;%%;;%:,;%%%%%;;%%;;,
                    `;;%%%,;%%%%%%%%%;;;
                    `;:%%%%%%;;%%;;;'
                        .:::::::.
                            s.
        """ 
    return f"""
        {Fore.BLUE}FINISHED SAVING{Fore.RESET}
        Created by saturn#1111
            # first time using pyppeteer
                                .;;,
        .,.               .,;;;;;,
        ;;;;;;;,,        ,;;%%%%%;;
        `;;;%%%%;;,.  ,;;%%;;%%%;;
        `;%%;;%%%;;,;;%%%%%%%;;'
            `;;%%;;%:,;%%%%%;;%%;;,
                `;;%%%,;%%%%%%%%%;;;
                `;:%%%%%%;;%%;;;'
                    .:::::::.
                        s.
        @Pinterest session: {session}
    """

def readJSfile():
    file_lines = file.readlines()
    txt = ''
    for i in file_lines:
        txt += i
    return str(txt)


async def main(show_browser:bool=False):
    count = 0
    urls = []
    print(design())
    
    browser = await launch(headless=show_browser)
    page = await browser.newPage()
    await page.goto('https://pinterest.com/login')
    await page.type('input[id=email]', EMAIL)
    await page.type('input[id=password]', password)
    await asyncio.sleep(2)
    await page.keyboard.type('\n')
    await page.waitForNavigation()
    dimensions = await page.evaluate(readJSfile())

    for i in dimensions.get('images'):
        if i.startswith('https://i.pinimg.com/'):
            main_x = i.split('/')[3]
            if str(main_x).lower() != '75x75_RS'.lower():
                if int(main_x.split('x')[0]):
                    urls.append(i) 

    for y in urls:
        count += 1
        async with ClientSession() as session:
            fmt = str(y).split('.')[-1]
            res = await session.get(y)
            with open(f'{count}.{fmt}', "wb") as out_file:
                out_file.write(await res.read())
    print(design('no sesion yet'))
    await browser.close()
    
    
asyncio.run(main(show_browser=False))
