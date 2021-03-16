from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread, active_count
from time import sleep

chrome_opt = Options()
chrome_opt.add_argument("-headless")
browser = webdriver.WebDriver("chromedriver.exe", chrome_options=chrome_opt)
def get_view():
    browser.get("https://www.clickasnap.com/i/g4rxpjvczgoarves")

thr = int(input("Threads?: "))

while True:
    for _ in range(thr):
        t = Thread(target=get_view)
        t.start()
    
    sleep(3)