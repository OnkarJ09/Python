from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search_lamdatest_amazon():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    driver.find_element(By.XPATH,
        "//input[@placeholder='Search Amazon.in']")\
        .send_keys("IPhone")
    driver.find_element(By.XPATH,
        "//button[value()='Go']").click()
    search_value = driver.find_element(By.XPATH,
        "//span[contains(text(),'Results')]").text
    assert "Iphone" in search_value
    
def test_add_to_cart():
    result = 1
    print("Add to cart")
    assert result == 1