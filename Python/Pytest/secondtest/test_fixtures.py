from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def setup_teardown():
    driver. get("https://ecommerce-playground.lambdatest.io/index.php?route-account/login")


    
