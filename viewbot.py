import concurrent.futures
import sys
import time

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By


# takes YouTube video URL & duration of watching (playing) the video (:in seconds)
url, duration = str(sys.argv[1]), int(sys.argv[2])

# checks & reads the proxy-list.txt
proxies=[]
try:
    with open('proxy-list.txt', 'r') as f:
        proxies=f.readlines()
except:
    print('[ERROR]\t"proxy-list.txt" file NOT FOUND !!')
    exit()
print('[***]\tTotal Proxies :',len(proxies))


# starting YouTube video using different proxies
def getViews(proxy):
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--proxy-server=%s' %proxy)
    options.add_argument('--window-size=640,480')

    try:
        service = ChromeService(executable_path='./chromedriver.exe')
        driver = Chrome(options=options, service=service)
        driver.get(url)
        time.sleep(duration)
    except:
        pass

    driver.quit()

# executing start() parallelly
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getViews, proxies)
