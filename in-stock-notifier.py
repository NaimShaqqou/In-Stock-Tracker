from selenium import webdriver

# Using Chrome to access the internet
driver = webdriver.Chrome("./chromedriver.exe")

# open the webpage in question
driver.get("https://www.google.com/")
