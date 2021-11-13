from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Using Chrome to access the internet
ser = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = ser)

# open the webpage in question
driver.get("https://www.google.com/")
