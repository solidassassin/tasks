import time

from datetime import date
from typing import Union

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import (
    TimeoutException,
    ElementNotInteractableException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException
)


driver = webdriver.Chrome("./drivers/chromedriver")
timeout = 5  # seconds
url = "https://www.tiketa.lt/EN/search"
driver.get(url)


# EC builtins did not seem to help much, so custom it is
class TillClickable:
    def __init__(self, locator: tuple):
        self.locator = locator

    def __call__(self, brow: webdriver.Chrome):
        try:
            element = brow.find_element(*self.locator)
            element.click()
            return element
        except (
            ElementNotInteractableException,
            NoSuchElementException,
            ElementClickInterceptedException,
            StaleElementReferenceException
        ):
            time.sleep(0.1)
            return False


def wait_click(seconds: int, by: str, path: str) -> WebElement:
    try:
        item = WebDriverWait(driver, seconds).until(
            TillClickable((by, path))
        )
    except TimeoutException:
        print("Page loading time was exceeded")
        exit()
    return item


# Some helper methods
def click(by: str, path: str) -> WebElement:
    """
    Click the element provided by path and return it.
    """
    element = driver.find_element(by, path)
    element.click()
    return element


def send_keys(by: str, path: str, *keys: Union[str, Keys]) -> WebElement:
    """
    Sends keys to the element provided by path and return it.
    """
    element = driver.find_element(by, path)
    element.send_keys(*keys)
    return element


def login(username: str, password: str):
    click(By.ID, "OnlyLogin")
    send_keys(By.ID, "txtLoginName", username)
    send_keys(By.ID, "txtLoginPsw", password, Keys.ENTER)


# Since the date in the task isn't available anymore I use the current date
def search(event_name: str, city_name: str, till: date):
    wait_click(timeout, By.XPATH, "//input[@name='sf_TextFilter']")
    send_keys(By.XPATH, "//input[@name='sf_TextFilter']", event_name, Keys.TAB)
    click(By.ID, "dropdownMenu3")
    click(By.XPATH, f"//a[@role='menuitem' and text()='{city_name}']")
    send_keys(
        By.XPATH,
        "//input[@name='sf_DateFrom']",
        date.today().strftime("%Y-%m-%d")
    )
    send_keys(By.XPATH, "//input[@name='sf_DateTo']", till.strftime("%Y-%m-%d"))
    click(By.XPATH, "//*[@id='advSearchForm']/div[4]/button")


def buy():
    wait_click(timeout, By.ID, "btnBuy-23125")
    # Considering that the xpath from id is quite long and volitiale
    # Finding by href is more reliable in my opinion
    click(By.XPATH, "//a[@href='/EN/Purchase/23125/111185']")
    wait_click(timeout, By.XPATH, "//label[@for='rb_Price252067']")
    wait_click(timeout, By.XPATH, "//label[@for='rb_Sector578392']")


# Change to your login info:
login("user", "pass")
search("Forum", "Kaunas", date(2020, 12, 31))
buy()
