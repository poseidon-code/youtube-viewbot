# proxy scraping for https://freeproxylists.net/
import concurrent.futures
from os import system
from platform import system as cos

from selenium.webdriver import Chrome, ChromeOptions


def clear():
    if cos() == 'Windows': system('cls')
    else: system('clear')

# www.freeproxylists.com proxy list URLs
urls = ['http://www.freeproxylists.net/?s=rs', 'http://www.freeproxylists.net/?pr=HTTPS&s=rs', 'http://www.freeproxylists.net/?pr=HTTPS&s=u', 'http://www.freeproxylists.net/?pr=HTTPS&s=ts', 'http://www.freeproxylists.net/?c=&pt=&pr=HTTPS&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0']


# setting webdriver options
options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.headless=True


# getting all proxies
proxies = []
def getProxy(url):
    driver = Chrome(executable_path='./chromedriver.exe', options=options)
    driver.get(url)
    l = len(driver.find_elements_by_xpath(f'/html/body/div[1]/div[2]/table/tbody/tr'))
    for i in range(2,l):
        try:
            host = driver.find_elements_by_xpath(f'/html/body/div[1]/div[2]/table/tbody/tr[{i}]/td[1]/a')[0]
            port = driver.find_elements_by_xpath(f'/html/body/div[1]/div[2]/table/tbody/tr[{i}]/td[2]')[0]
            proxies.append(':'.join([host.text,port.text]))
        except:
            pass
    driver.quit()



clear()
print('[...]\tGetting Proxies from www.freeproxylists.net')
# executing getProxy() parallelly
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getProxy, urls)
clear()
print('[DONE]\tGetting Proxies from www.freeproxylists.net')


# removing duplicate proxies
proxies = list(set(proxies))
print('[***]\tTotal Proxies Found :', len(proxies))


# writing proxies to file
with open('proxy-list.txt', 'w+') as f:
    for i in range(len(proxies)):
        f.write(proxies[i]+'\n')
print('[DONE]\tGenerated "proxy-list.txt"')
