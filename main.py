from selenium import webdriver
from time import sleep

from selenium.webdriver.remote.webelement import WebElement


DRIVER_PATH = '../chromedriver.exe'
SITE_URL = 'https://flippybitandtheattackofthehexadecimalsfrombase16.com/'



def getEnemyNumbers():
  enemies = []

  while len(enemies) == 0:
    # print('test')
    enemies = container.find_elements_by_class_name('enemy')
    # print(enemies)
    killed = container.find_elements_by_class_name('under-attack')

    if enemies != None:
      i: WebElement
      for i in enemies:
        # print(i.text)
        if i in killed:
          enemies.remove(i)

    # print(enemies)
  return enemies


def hexToBinary(hexNum):
  return "{0:08b}".format(int(hexNum, 16))

def reset():
  elements = container.find_elements_by_class_name('selected')

  i: WebElement
  for i in elements:
    i.click()



driver = webdriver.Chrome(DRIVER_PATH)
driver.get(SITE_URL)

sleep(5)
container = driver.find_element_by_xpath('//*[@id="game-container"]')
container.click()

buttons = driver.find_elements_by_class_name('tapper')

sleep(0.5)

while True:
  enemies = getEnemyNumbers()
  # buttons[0].click()

  enemy: WebElement
  for enemy in enemies:
    try:
      converted = hexToBinary(enemy.text)[::-1]

      print(enemy.text, converted)
      reset()
      for button, binary in zip(buttons, converted):

        if int(binary):
          button.click()

      # sleep(0.1)
    except:
      pass