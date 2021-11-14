from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Using Chrome to access the internet
def run_chrome() :
    ser = Service(ChromeDriverManager().install())
    opt = Options()
    driver = webdriver.Chrome(service = ser, options=opt)

# checks if product in given webpage is in stock
def check_stock(webpage) :
    # open the webpage in chrome
    run_chrome()
    driver.get(f"https://{webpage}.com")
    driver.implicitly_wait(2)

    # check which website we are on


    # search for the graphics card
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    driver.implicitly_wait(2)
    search_bar.send_keys("RTX 3060")
    search_bar.send_keys(Keys.RETURN)

    # click on all the results and as soon as one is found
    # print to discord

    result = driver.find_element(By.PARTIAL_LINK_TEXT, 'GeForce RTX 3060')
    result.click()
    driver.implicitly_wait(10)
