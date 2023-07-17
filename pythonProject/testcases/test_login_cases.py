import time

import pytest
from Identifiers import loginidentifiers
from Identifiers import homepageidentifiers
from selenium.webdriver.common.by import By
from core_folder import core_logic
from testdata import urls


def test_blankusername():
    core_logic.openpage(urls.homepage)
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.username_txt_id).send_keys("")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.password_txt_id).send_keys("secret_sauce")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.login_btn_id).click()
    text = core_logic.driver.find_element(by=By.XPATH, value=loginidentifiers.error_msdbox).text
    assert text == 'Epic sadface: Username is required'


def test_validlogin():
    core_logic.openpage(urls.homepage)
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.username_txt_id).send_keys("standard_user")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.password_txt_id).send_keys("secret_sauce")
    core_logic.driver.find_element(by=By.ID, value=loginidentifiers.login_btn_id).click()
    time.sleep(5)

    title_page = core_logic.driver.find_element(by=By.XPATH, value=homepageidentifiers.homepage_title).text
    assert title_page == 'Swag Labs'
