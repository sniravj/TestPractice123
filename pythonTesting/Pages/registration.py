from selenium.webdriver.common.by import By
import Base.driverIni

class registation:

    def __init__(self, obj):
        global driver
        driver = obj

    def test_userid(self,username):
        driver.find_element(By.XPATH, "//input[@name='fld_username']").send_keys(username)

    def test_email(self,email):
        driver.find_element(By.XPATH, "//input[@name='fld_email']").send_keys(email)

    def test_password(self,password):
        driver.find_element(By.XPATH, "//input[@name='fld_password']").send_keys(password)

    def test_confirm_password(self,confirm_password):
        driver.find_element(By.XPATH, "//input[@name='fld_cpassword']").send_keys(confirm_password)
