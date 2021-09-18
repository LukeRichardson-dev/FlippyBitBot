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

def hexToBinary(hexNum):
  return "{0:08b}".format(int(hexNum, 16))

def sendBinary(binary):
  reset()

  for index, letter in enumerate(binary[::-1]):
    if letter == '1':
      buttons[index].click()

def reset():
  elements = container.find_elements_by_class_name('in-dock')

  for index, element in enumerate(elements):
    if 'selected' in element.get_attribute('class'):
      i = int(element.get_attribute('data-index'))
     
      buttons[i].click()

###

INTERVAL = 2.5

def main():

    while True:
        sleep(INTERVAL)

        enemies = driver.find_elements_by_class_name('enemy')

        for i in enemies:
            try:
                sendBinary(hexToBinary(i.text))
            except:
                pass
    

if __name__ == '__main__':
    THREAD_COUNT = 3
    
    for _ in range(THREAD_COUNT):
        thread = Thread(None, main)

        thread.start()
        sleep(INTERVAL / THREAD_COUNT)
