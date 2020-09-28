from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome("./drivers/chromedriver")
url = "https://the-internet.herokuapp.com/challenging_dom"
timeout = 2  # seconds
# Just a little offset so it wouldn't click on the actual href
offset = 2  # x-axis

driver.get(url)


def highlight_for(path: str, seconds: int = timeout):
    action = ActionChains(driver)
    element = driver.find_element_by_xpath(path)
    width = element.size["width"]
    # move_to_element_by_offset didn't seem to properly place the cursor
    action.move_to_element(element).move_by_offset(
        -width / 2 - offset, 0
    ).click_and_hold().move_by_offset(
        width + offset, 0
    ).release().pause(seconds).perform()


def double_click_for(path: str, seconds: int = timeout):
    action = ActionChains(driver)
    element = driver.find_element_by_xpath(path)
    action.double_click(element).pause(seconds).perform()


# I can think of 2 ways to achieve this,
# find all elements in certain tag and iterate with a condition,
# or traversing purely with xpath
# I'll be taking the xpath approach, because I assume that's what you want to see
# The only reason why I put these actions in functions is for readability
# and to properly organize individual tasks
def diceret(column: str, row: int):
    double_click_for(
        f"//tbody/tr[{row}]/td[count(//thead/tr/" +
        f"th[text()='{column}']/preceding-sibling::th)+1]"
    )


def apeirian(content: str, text: str):
    column = "Action"
    highlight_for(
        f"//tbody/tr[td//text()[contains(., '{content}')]]" +
        f"/td[count(//thead/tr/th[text()='{column}']/" +
        f"preceding-sibling::th)+1]/a[text()='{text}']"
    )


def definiebas_iuvaret(text: str):
    # 2nd option is 3 columns to the left
    # I assume you wanted me to find the 2nd relative to 1st
    definiebas = f"//tbody/tr[td//text()[contains" + \
        f"(., '{text}')]]/td[text()='{text}']"
    double_click_for(definiebas)
    double_click_for(definiebas + "/preceding-sibling::td[3]")


diceret("Diceret", 3)
apeirian("Apeirian7", "delete")
apeirian("Apeirian2", "edit")
definiebas_iuvaret("Definiebas7")

driver.find_element_by_xpath("//*[@class='button success']").click()
