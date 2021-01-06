from selenium.webdriver import Chrome, ChromeOptions
import time
import sys
import concurrent.futures

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
        driver = Chrome(executable_path='./chromedriver.exe', options=options)
        driver.get(url)
        time.sleep(duration)
    except:
        pass
    driver.quit()

# executing start() parallelly
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getViews, proxies)
