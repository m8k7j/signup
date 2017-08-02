from selenium.webdriver.common.by import By


id_email = (By.ID, "id_email")
id_password1 = (By.ID, "id_password1")
id_password2 = (By.ID, "id_password2")
submit = (By.XPATH, "//button[@type='submit']")
mail_error = (By.XPATH, "//li[@ng-show='register_valid_form.email.$error.pattern']")
mail_remind = (By.XPATH, "//li[@ng-show='register_valid_form.email.$error.required']")
password1_error = (By.XPATH, "//li[@ng-show='register_valid_form.password1.$error.minlength']")
password2_error = (By.XPATH, "//li[@ng-show='register_valid_form.password2.$error.minlength']")
password1_remind = (By.XPATH, "//li[@ng-show='register_valid_form.password1.$error.required']")
password2_remind = (By.XPATH, "//li[@ng-show='register_valid_form.password2.$error.required']")


def set_email(driver,email):
    driver.find_element(*id_email).send_keys(email)


def set_password1(driver,password1):
    driver.find_element(*id_password1).send_keys(password1)


def set_password2(driver,password2):
    driver.find_element(*id_password2).send_keys(password2)


def submit_result(driver):
    driver.find_element(*submit).click()


def clear_mail(driver):
    driver.find_element(*id_email).clear()


def clear_password1(driver):
    driver.find_element(*id_password1).clear()


def clear_password2(driver):
    driver.find_element(*id_password2).clear()
