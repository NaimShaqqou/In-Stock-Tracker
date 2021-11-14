from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os

# Using Chrome to access the internet
def run_chrome() :
    ser = Service(ChromeDriverManager().install())
    opt = Options()
    opt.headless=True
    driver = webdriver.Chrome(service=ser, options=opt)
    return driver

# checks if product in given webpage is in stock
def check_stock(webpage, search) :
    # open the webpage in chrome
    webpage = webpage.lower()
    driver = run_chrome()
    driver.get(f"https://{webpage}.com")
    driver.implicitly_wait(2)

    # search for product and return result
    if webpage in 'amazon':
        return search_amazon(search, driver)
    elif webpage in 'newegg':
        return search_newegg(search, driver)
    else:
        return search_bestbuy(search, driver)

# searches for 'search' in newegg.com
# returns whether the product is in stock or no
def search_newegg(search, driver):
    # search for the product
    search_bar = driver.find_element(By.CSS_SELECTOR, "input[type='search']")
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)

    # click on listing
    try:
        result = driver.find_element(By.PARTIAL_LINK_TEXT, search)
        result.click()
        driver.implicitly_wait(2)
    except NoSuchElementException:
        return f'{search} was not found on Newegg.com'

    # check if in stock
    try:
        button = driver.find_element(By.XPATH, '//button[text()="Add to cart "]')
        return f'Item currently in stock!{os.linesep}{driver.current_url}'
    except NoSuchElementException:
        return f'Item currently out of stock!{os.linesep}{driver.current_url}'

# searches for 'search' in amazon.com
# returns whether the product is in stock or no
def search_amazon(search, driver):
    # search for the product
    search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)

    # click on listing
    try:
        result = driver.find_element(By.CSS_SELECTOR, "img[class='s-image']")
        result.click()
        driver.implicitly_wait(2)
    except NoSuchElementException:
        return f'{search} was not found on Amazon.com'

    # check if in stock
    try:
        button = driver.find_element(By.ID, 'add-to-cart-button')
        return f'Item currently in stock!{os.linesep}{driver.current_url}'
    except NoSuchElementException:
        return f'Item currently out of stock!{os.linesep}{driver.current_url}'

# searches for 'search' in bestbuy.com
# returns whether the product is in stock or no
def search_bestbuy(search, driver):
    # check if there is a popup and close it
    try:
        popup = driver.find_element(By.CSS_SELECTOR, "svg[class='c-close-icon-svg']")
        driver.execute_script("""
            var l = document.getElementsByClassName("c-overlay-fullscreen")[0];
            l.parentNode.removeChild(l);
        """)
    except NoSuchElementException:
        pass

    #search for the product
    search_bar = driver.find_element(By.ID, "gh-search-input")
    search_bar.send_keys(search)
    search_bar.send_keys(Keys.RETURN)
    driver.implicitly_wait(2)

    # click on listing
    try:
        result = driver.find_element(By.CSS_SELECTOR, "img[class='product-image']")
        result.click()
        driver.implicitly_wait(2)
    except NoSuchElementException:
        return f'{search} was not found on Bestbuy.com'


    # check if in stock
    try:
        button = driver.find_element(By.CSS_SELECTOR, "button[class='c-button c-button-primary c-button-lg c-button-block c-button-icon c-button-icon-leading add-to-cart-button']")
        return f'Item currently in stock!{os.linesep}{driver.current_url}'
    except NoSuchElementException:
        return f'Item currently out of stock!{os.linesep}{driver.current_url}'
