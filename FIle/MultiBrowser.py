from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="../driver/chromedriver.exe")
driver = webdriver.Edge(executable_path="../driver/msedgedriver.exe")
driver.get("https://www.google.com/")

print(driver.title)
print(driver.page_source)
print(driver.current_url)