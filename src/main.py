"""
Handle login to get auth
"""
from get_driver import FIREFOX_DRIVER, get_url
from selenium.webdriver.common.by import By

driver = FIREFOX_DRIVER()
driver.get(get_url("login"))

wrapper_outer = driver.find_element(By.TAG_NAME, 'div')
wrapper_inner = wrapper_outer.find_element(By.TAG_NAME, 'div')
form = wrapper_inner.find_element(By.TAG_NAME, 'form')
fields = form.find_elements(By.TAG_NAME, 'div')


values = ["comand.alvin@gmail.com", "helloworld"]

for i in range(2):
    input_ = fields[i].find_element(By.TAG_NAME, 'input')
    input_.send_keys(values[i])


form.find_element(By.TAG_NAME, "button").click()



driver.get(get_url("main_page"))
wrapper_outer = driver.find_element(By.CLASS_NAME, "wrapper")
wrapper_inner = driver.find_element(By.CLASS_NAME, "content-wrapper")

print(wrapper_inner.get_attribute("class"))