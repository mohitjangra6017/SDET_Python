from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

# Page Convert Hindi to English
custom_options = webdriver.ChromeOptions()
prefs = {
    "translate_whitelists": {"hi": "en"},
    "translate": {"enabled": "true"}
}
custom_options.add_experimental_option("prefs", prefs)
driver: WebDriver = webdriver.Chrome(executable_path="../driver/chromedriver.exe", options=custom_options)

driver.maximize_window()

driver.get("https://www.facebook.com/")

print(driver.title)
# print(driver.page_source)
print(driver.current_url)


if(driver.getPageSource().contains("Facebook")):{
print("Facebook helps you connect and share with people.")
}
else:
    {
       print("Text is absent")
    }
