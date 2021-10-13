import re

import self as self
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# Page Convert Hindi to English
custom_options = webdriver.ChromeOptions()
prefs = {
    "translate_whitelists": {"hi": "en"},
    "translate": {"enabled": "true"}
}
custom_options.add_experimental_option("prefs", prefs)
driver: WebDriver = webdriver.Chrome(executable_path="../driver/chromedriver.exe", options=custom_options)

driver.maximize_window()

driver.get("http://demowebshop.tricentis.com/")

print(driver.title)
# print(driver.page_source)
print(driver.current_url)

# verify facebook logo is visible
logo = driver.find_element_by_xpath("//img[contains(@src,'logo.png')]")
if 'logo' in logo.get_attribute('src'):
    print("Web shop logo is visible on UI")
else:
    print('Web Shop Logo Not Visible On UI')

# verify create account button and click on

regiser = driver.find_element_by_xpath("//a[contains(@href,'/register')]")
if 'ico-register' in regiser.get_attribute('class'):
    print("Register Button Is Visible")
    regiser.click()
    print("Click Success!")
else:
    print("Register Button Is Not Visible")

# verify signup details

# title = driver.find_element_by_xpath("//div[@class='page-title']//h1[text()='Register']")
# text = 'Register'
# if text in h1:
#     print("Title is Register")

content = driver.page_source
abc = content.find('Register')
print("text is present in the webpage", abc)

