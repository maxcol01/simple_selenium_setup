from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from action import Action

# Set up the Chrome driver (ensure chromedriver is in your PATH)
driver = webdriver.Chrome()

# Open Google
URL = "https://the-internet.herokuapp.com/"
driver.get(URL)
driver.maximize_window()
  
window = Action()
window.stay_open()



