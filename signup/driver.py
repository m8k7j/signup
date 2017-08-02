from selenium import webdriver


def driver_browser(br):
    if br == 'Chrome':
        return webdriver.Chrome()
    if br == 'Firefox':
        return webdriver.Firefox()
    if br == 'IE':
        return webdriver.Ie()



