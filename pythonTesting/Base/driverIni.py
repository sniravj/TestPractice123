from selenium import webdriver
from Library.configreader import conf_reader

def test_setup():
    global driver
    browser = conf_reader("Details", "Browser")
    if browser == "Chrome":
        driver = webdriver.Chrome()
    elif browser == "Firefox":
        driver = webdriver.Firefox()
    elif browser == "IE":
        driver = webdriver.Ie()


    url = conf_reader("Details", "Application_URL")
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver

def test_teardown():
    driver.close()
    driver.quit()
    print("Test Completed")