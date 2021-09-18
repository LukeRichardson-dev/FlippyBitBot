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

def getCurrentBinary():
  return ''.join(dock.text.split('\n')) 

def reset():
  for index, value in enumerate(getCurrentBinary()):
    if value == '1':
      buttons[index].click()


def hexToBinary(hexNum):
  return "{0:08b}".format(int(hexNum, 16))

def sendBinary(binary):
  current = getCurrentBinary()

  for index, letter in enumerate(binary[::-1]):
    
    if letter != current[index]:
      buttons[index].click()
    

###

INTERVAL = 1.75

def main():
  
  sleep(INTERVAL)

  while True:
    

    enemies = driver.find_elements_by_class_name('enemy')
    count = len(enemies)

    for i in enemies:
      try:
        sendBinary(hexToBinary(i.text))
      except:
        pass

    # if count < 40: #! EXPERIMENT
    #   sleep(INTERVAL)
    
      

if __name__ == '__main__':
  THREAD_COUNT = 1
      
  if THREAD_COUNT > 1:
    for _ in range(THREAD_COUNT):
      thread = Thread(None, main)

      thread.start()
      sleep(INTERVAL / THREAD_COUNT)
  else:
    main()
