from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement
from threading import Thread


DRIVER_PATH = '../chromedriver.exe'
SITE_URL = 'https://flippybitandtheattackofthehexadecimalsfrombase16.com/'

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(SITE_URL)

sleep(5)
container: WebElement = driver.find_element_by_xpath('//*[@id="game-container"]')
container.click()

buttons = driver.find_elements_by_class_name('tapper')
docks = driver.find_elements_by_class_name('in-dock')

dock: WebElement = container.find_element_by_id('dock')
print(dock.text)