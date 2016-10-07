from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


while True:
    #driver = webdriver.PhantomJS()
    driver = webdriver.PhantomJS(service_args=['--ssl-protocol=any'])
    driver.maximize_window()
    #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("https://www.betfair.com/exchange/football/event?id=27958484&exp=e")
    #driver.implicitly_wait(1)

    wait = WebDriverWait(driver, 1)
    elem = driver.find_element_by_class_name("new-total-matched").text
    print(elem)
    driver.quit()
