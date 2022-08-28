import asyncio
import sys
import time 
import subprocess
from curses import wrapper
import aiohttp
from aiohttp.client import ClientSession

f = ['https://youtu.be/', 'https://mega.nz/file/', 'https://mega.nz/folder/', 'https://imgur.com/gallery/', 'https://imgur.com/a/', 'https://www.instagram.com/p/', 'https://discord.gg/', 'https://www.instagram.com/', 'https://pin.it/','https://www.youtube.com/watch?v=','https://drive.google.com/file/d']
r_t = ["""\nif result > 500000:\n    x = 1\n""","""\nif result >= 2216:\n    x = 1\n""","""\nif result >= 2228:\n    x = 1\n""","""\nif result != 6167:\n    x = 1\n""","""\nif result != 6167:\n    x = 1\n""", """\nif result >= 220000:\n    x = 1\n""","""\nif result >= 6000:\n    x = 1\n""","""\nif result <= 300000:\n    x = 1\n""","""\nif result >= 190000:\n    x = 1\n""","""\nif result >= 600000:\n    x = 1\n""","""\nif not result <= 3100:\n    x = 1\n"""]
url_list = ["https://bit.ly/","https://pastebin.com/","https://imgur.com/a/","https://imgur.com/gallery/","https://imgflip.com/i/","https://youtu.be/","https://tinyurl.com/","https://goo.gl/","https://www.mediafire.com/","https://mega.nz/file/","https://mega.nz/folder/","https://gyazo.com/","https://www.dailymotion.com/video/","https://www.facebook.com/","https://www.reddit.com/","https://discord.gg/","https://www.imdb.com/title/","https://pin.it/","https://drive.google.com/file/d/","https://docs.google.com/document/d/","https://forms.gle/","https://docs.google.com/prensentation/d/","https://clyp.it/","https://www.instagram.com/","https://www.instagram.com/p/","https://isbnsearch.org/isbn/","https://far-breeze-72b.notion.site/","https://u.teknik.io/"]
backlink = input("Enter Backlink ")
f = [x+backlink for x in f]
url_list = [x+backlink for x in url_list]
mainf = []
mainstr = ''
newf = ''
x = 0
result = ''

async def download_link(url:str,session:ClientSession):
    async with session.get(url) as response:
        if url in f and response.status != 404:
            global result, x
            result = len(await response.text())
            exec(r_t[f.index(url)],globals())
            mainf.append(url if x == 1 else "")
            # print(result, r_t[f.index(url)])
            x = 0  
        else:  
            if response.status == 200:
                mainf.append(url)
async def download_all(urls:list):
    my_conn = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=my_conn) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(download_link(url=url,session=session))
            tasks.append(task)
        await asyncio.gather(*tasks,return_exceptions=True) 

def ping():
    global mainf,mainstr,newf
    start = time.time()
    #if len(backlink) >= 5:
    asyncio.run(download_all(url_list))
    end = time.time()
    newf = [str([x for x in mainf if x!=""].index(x))+") "+x+"\n" for x in [x for x in mainf if x!=""]]
    print(mainf)
    for x in newf:
        mainstr+=str(x)
    print(mainstr)
    print(f'Pinged {len(url_list)} links in {end - start} seconds')

def main(stdscr):
    stdscr.addstr(mainstr)
    stdscr.addstr('a for all and q for quit ')
    while True:
        key = stdscr.getkey()
        if key.isdigit() and int(key) < len(newf):
            subprocess.run(["powershell","-Command","start '"+str([x for x in mainf if x!=""][int(key)])+"'"])
        elif key == 'a':
            for x in range(len(newf)):
                subprocess.run(["powershell","-Command","start '"+str([x for x in mainf if x!=""][x])+"'"])
        elif key == 'q':
            sys.exit()

if __name__ == '__main__':
    ping()
    wrapper(main)
