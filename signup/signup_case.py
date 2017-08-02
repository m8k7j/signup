#coding:utf-8
import time
from selenium.webdriver.support import expected_conditions as EC
from sign_up_function import sign_up
from common import switch_to_non_current_window
import sign_elements


def test_signup_null(driver):
    sign_up(driver, '', '', '')
    time.sleep(10)
    result = driver.find_element(*sign_elements.submit)
    if result.get_attribute('disabled'):
        assert True
    else:
        assert False


def test_signup_email_error(driver):
    sign_elements.set_email(driver,'abc')
    assert driver.find_element(*sign_elements.mail_error).text == u'邮箱地址无效或重复'
    time.sleep(3)
    sign_elements.clear_mail(driver)
    time.sleep(3)
    assert driver.find_element(*sign_elements.mail_remind).text == u'这个字段是必填项。'
    time.sleep(3)
    sign_elements.set_email(driver,'a@3.d')
    time.sleep(3)
    assert driver.find_element(*sign_elements.mail_error).text == u'邮箱地址无效或重复'


def test_signup_password1_error(driver):
    sign_elements.set_password1(driver, '11')
    time.sleep(3)
    assert driver.find_element(*sign_elements.password1_error).text == 'Ensure this value has at least 3 characters'
    sign_elements.clear_password1(driver)
    time.sleep(3)
    assert driver.find_element(*sign_elements.password1_remind).text == u'这个字段是必填项。'


def test_signup_password2_error(driver):
    sign_elements.set_password2(driver, '11')
    time.sleep(3)
    assert driver.find_element(*sign_elements.password2_error).text == 'Ensure this value has at least 3 characters'
    sign_elements.clear_password2(driver)
    time.sleep(3)
    assert driver.find_element(*sign_elements.password2_remind).text == u'这个字段是必填项。'


def test_password1_not_password2(driver):
    sign_elements.set_password1(driver,'1111')
    sign_elements.set_password2(driver,'1112')
    result = driver.find_element(*sign_elements.submit)
    if result.get_attribute('disabled'):
        assert True
    else:
        assert False


def test_signup_success(driver):
    sign_up(driver, 'a@8.d', '1111', '1111')
    sign_elements.submit_result(driver)
    time.sleep(10)
    switch_to_non_current_window(driver)
    assert driver.title == u'Fenby | 专业面向初学者的在线互动编程学习的平台'





