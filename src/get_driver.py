from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



# with webdriver.Firefox() as driver:

#     driver.get("http://google.com/ncr")
#     wait = WebDriverWait(driver, 10)
#     driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
#     wait.until(presence_of_element_located((By.XPATH, '//*[@id="rcnt"]')))
#     results = driver.find_elements(By.XPATH, "//a[@href]")

#     for i, elem in enumerate(results):
#         print(f'#{i} {elem.text} ({elem.get_attribute("href")})')


URLS = {
    "base_url" : "https://belajarbertahap.com/",
    "login" : "auth/login",
    "main_page" : "latihanskd"
}

FIREFOX_DRIVER = webdriver.Firefox
CRHOME_DRIVER = webdriver.Chrome
EXPLORER_DRIVER = webdriver.Ie
EDGE_DRIVER = webdriver.Edge


def get_url(room):
    return "".join((URLS["base_url"], URLS[room]))


