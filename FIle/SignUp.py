from selenium import webdriver
from selenium.webdriver.common.keys import Keys

custom_options = webdriver.ChromeOptions()
prefs = {
    "translate_whitelists": {"hi": "en"},
    "translate": {"enabled": "true"}
}
custom_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe", options=custom_options)
# driver = webdriver.Edge(executable_path="../driver///chromedriver.exe")
driver.maximize_window()
driver.get("https://www.facebook.com/")

print(driver.title)

print(driver.page_source)
print(driver.current_url)
