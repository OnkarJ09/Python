from selenium import webdriver
from selenium.webdriver.common.by import By

def test_lamdatest_simple_frm_demo():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    driver.find_element(By.XPATH,
        "//input[@id='user-message']")\
            .send_keys("Pytest is a test framework")
    driver.find_element(By.ID, "showInput").click()
    message = driver.find_element(By.ID, "message").text
    assert message == "Pytest is a test framework"