from selenium import webdriver

def test_lamdatest_playground():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com/watch?v=_CJ-vJFnAWQ&list=PLZMWkkQEwOPkFsyal6Uq3RvAGsBbLCfZV&index=3")
    print("Title: ", driver.title)

def test_lamdatest_hii():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    print("Title: ", driver.title)