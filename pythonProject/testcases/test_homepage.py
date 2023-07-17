from Identifiers import loginidentifiers
from Identifiers import homepageidentifiers
from selenium.webdriver.common.by import By
from core_folder import core_logic
from testdata import urls
import time


def test_homepage_label():
    core_logic.openpage(urls.homepage)
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.username_txt_id).send_keys("standard_user")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.password_txt_id).send_keys("secret_sauce")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.login_btn_id).click()
    hp_label = core_logic.driver.find_element(by=By.XPATH, value=homepageidentifiers.homepage_label).text
    assert hp_label == 'Products'

    time.sleep(5)
