import time
from Base.driverIni import test_setup, test_teardown
from Pages.registration import registation
import pytest
from Data.data_generator import data_generator


@pytest.mark.parametrize('data',data_generator())
def test_validate_registration(data):

    driver = test_setup()
    reg = registation(driver)
    reg.test_userid(data[0])
    reg.test_email(data[1])
    reg.test_password(data[2])
    reg.test_confirm_password(data[3])
    time.sleep(5)
    driver1 = test_teardown()
