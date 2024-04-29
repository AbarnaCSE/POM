
from Data import data
from Locators import locator

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait  

class imdb:

   def __init__(self):
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

   def boot(self):
       self.driver.get(data.WebData().url)
       self.driver.maximize_window()
       self.wait = WebDriverWait(self.driver, 10)

   def quit(self):
       self.driver.quit()

   def imdb1(self):

    try:
       self.boot()
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().buttonlocator)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().NameLocator, data.WebData().Name)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().BirthLocator, data.WebData().Birth)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().resultlocator)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().menulocator)
       WebDriverWait(self.driver, 10)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().clearlocator)
       WebDriverWait(self.driver, 10)
       locator.WebLocators().enterText(self.driver, locator.WebLocators().SearchLocator, data.WebData().Search)
       locator.WebLocators().clickButton(self.driver, locator.WebLocators().enterlocator)
    except NoSuchElementException as e:
        print("Error!")        
    finally:
        self.quit()         
    
obj = imdb()
obj.imdb1()













































