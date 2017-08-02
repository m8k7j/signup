"""
Written by : Ding Huan
Versin : 0.1
Date: Aug 2nd 2017
"""

from signup.driver import driver_browser
from signup import signup_case
import pytest

@pytest.fixture(scope="function")
def set_up():

    driver = driver_browser('Chrome')
    base_url = "http://www.fenby.com"
    driver.implicitly_wait(30)
    driver.get(base_url+'/register')
    yield driver
    driver.quit()


def test_signup_null(set_up):
    signup_case.test_signup_null(set_up)


def test_signup_success(set_up):
    signup_case.test_signup_success(set_up)


def test_signup_email_error(set_up):
    signup_case.test_signup_email_error(set_up)


def test_signup_password1_error(set_up):
    signup_case.test_signup_password1_error(set_up)


def test_signup_password2_error(set_up):
    signup_case.test_signup_password2_error(set_up)


def test_password1_not_password2(set_up):
    signup_case.test_password1_not_password2(set_up)
if __name__ == '__main__':
    pytest.main("-s --html=report.html")

