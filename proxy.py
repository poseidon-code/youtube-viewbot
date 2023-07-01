# proxy scraping for/from https://free-proxy.cz/

import concurrent.futures
from os import system
from platform import system as current_os

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By


def clear():
    if current_os() == 'Windows': system('cls')
    else: system('clear')

# www.free-proxy.cz proxy list URLs
urls = [
    'http://free-proxy.cz/en/proxylist/country/all/https/ping/all',
    'http://free-proxy.cz/en/proxylist/country/all/https/uptime/all',
    'http://free-proxy.cz/en/proxylist/country/all/https/speed/all'
]

# setting webdriver options
options = ChromeOptions()
options.add_argument('-headless')


# getting all proxies
proxies = []
def getProxy(url):
    service = ChromeService(executable_path='./chromedriver.exe')
    driver = Chrome(options=options, service=service)
    
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="clickexport"]').click()
    proxylist = driver.find_element(By.XPATH, '//*[@id="zkzk"]')
    
    global proxies
    proxies.extend(proxylist.text.splitlines())

    driver.quit()



clear()
print('[...]\tGetting Proxies from www.free-proxy.cz')
# executing getProxy() parallelly
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getProxy, urls)
clear()
print('[DONE]\tGetting Proxies from www.free-proxy.cz')


# removing duplicate proxies
proxies = list(set(proxies))
print('[***]\tTotal Proxies Found :', len(proxies))


# writing proxies to file
with open('proxy-list.txt', 'w+') as f:
    for i in range(len(proxies)):
        f.write(proxies[i]+'\n')
print('[DONE]\tGenerated "proxy-list.txt"')
