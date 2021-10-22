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

driver.get("https://iframe-auth.arkoselabs.com/2F1CD804-FE45-F12B-9723-240962EBA6F8/index.html?data=ObBPVSppKfLiIF7aQL3OXg%3D%3D.ztxvUiFtpH7fRRaDhsoeGVFn8UQF5v%2BdglwF7PYsOEagsqefBl9%2Fs%2BqZgeIXjgdayMlIcd6XXmMDhr0I1my8CCtbn%2BvRGAwkvNdyK0%2F%2FURfQwmAbofZdLharQqCT%2BzVQdYKiShTQ8iKxewLJDUAyxpLbOUk%3D&mkt=en-US")

print(driver.title)
# print(driver.page_source)
print(driver.current_url)


# verify create account button and click on

register = driver.find_element_by_xpath("//span[@class='fc_meta_audio_btn']")
if 'home_children_button' in register.get_attribute('id'):
    print("Register Button Is Visible")
    register.click()
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

