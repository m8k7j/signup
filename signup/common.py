from selenium import webdriver


def switch_to_non_current_window(driver):

    driver.switch_to.default_content()
    all_handle = driver.window_handles
    current_handle = driver.current_window_handle
    for handle in all_handle:
        if handle != current_handle:
            driver.switch_to.window(handle)



