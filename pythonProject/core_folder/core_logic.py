from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

driver = webdriver.Chrome()


def openpage(link,tt="Hello"):
    driver.get(link)
    print(tt)
