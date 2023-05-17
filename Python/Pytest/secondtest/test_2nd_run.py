from selenium import webdriver
from selenium.webdriver.common.by import By

class AssertionTest():
    pass

def test_lamdatest_radio_buton_demo_value():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
    driver.find_element(By.XPATH,
       "//h4[contains(text(),'Gender')]"
       "//following::input[@value='Male']").click()
    driver.find_element(By.XPATH,
       "//h4[contains(text(),'Age Group')]"
       "//following::input[@value='15 - 50']").click()
    driver.find_element(By.XPATH,
       "//button[text()='Get values']").click()
    gender = driver.find_element(By.CSS_SELECTOR,
        ".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR,
        ".groupradiobutton").text
    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Male"))
    assert gender == "Male", "Gender is not correct"
    assert driver.title.__contains__("Selenium Grid Online")
    assert "15 - 50" in age_group, "Age Group Is Not Correct"
