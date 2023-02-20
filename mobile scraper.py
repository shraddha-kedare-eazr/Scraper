from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install()) #'/home/sanket/chromedriver_linux64/chromedriver'

driver.get("https://www.recycledevice.com/sell-mobile")

brand = driver.find_elements_by_xpath('//*[@id="categories"]/div/div/div[2]/div/div')



