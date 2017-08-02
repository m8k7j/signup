import sign_elements


def sign_up(driver, email, password1, password2):
    sign_elements.set_email(driver,email)
    sign_elements.set_password1(driver, password1)
    sign_elements.set_password2(driver, password2)


