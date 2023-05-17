import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
def test_lamdatest_ajax_form():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/ajax-form-submit-demo")
    driver.find_element(By.ID, "title")\
        .send_keys("Pytest tutorial")
    driver.find_element(By.ID, "description")\
        .send_keys("Lamdatest selenium playground")
    driver.find_element(By.ID, "btn-submit").click()
    request = driver.find_element(By.ID,
        "submit-control").text
    assert request.__contains__("Processing")


def test_e2e():
    print("End to end test")

@pytest.mark.smoke
def test_login():
    print("log into application")

@pytest.mark.smoke
def test_logout():
    print("log out the application")