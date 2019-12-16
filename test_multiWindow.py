from selenium.webdriver import Chrome
import pytest
import time


@pytest.fixture()
def environment_setup():
    global driver
    driver = Chrome()
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
    yield
    driver.close()


def test_verify_registration(environment_setup):
    mainWin=''
    driver.find_element_by_xpath("//label[text() = 'Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys("test")
    driver.find_element_by_name("_txtPassword").send_keys("test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
    driver.find_element_by_xpath("//a[contains(text(), 'My Account')]").click()
    driver.find_element_by_xpath("//a[contains(text(), 'Update')]").click()
    time.sleep(10)
    allwindows = driver.window_handles

    for win in allwindows:
        driver.switch_to.window(win)
        if driver.current_url == "https://www.thetestingworld.com/testings/manage_customer.php":
            driver.find_element_by_xpath("//button[text() = 'Start Download']").click()
            time.sleep(5)
            driver.close()
        elif driver.current_url == 'https://www.thetestingworld.com/testings/manage_customer.php/dashboard.php':
            mainWin = win

    driver.switch_to.window(mainWin)






