from selenium import webdriver
from time import sleep
import threading

from selenium.webdriver.remote.webelement import WebElement


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

if __name__ == '__main__':
  # sleep(2)
  
  def main():
    while True:
      sleep(1)
      # buttons[6].click()
      enemies = driver.find_elements_by_class_name('enemy')
      # print(enemies)
      killed = driver.find_elements_by_class_name('under-attack')

      if enemies:
        i: WebElement
        for i in enemies:
          # print(i.text)
          if i not in killed:
            try:
              sendBinary(hexToBinary(i.text))
            except Exception as e:
              print(e)

  thread = threading.Thread(None, main())
  thread.start()

  sleep(0.5)

  main()