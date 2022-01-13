import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://demowebshop.tricentis.com/")

reg_btn = driver.find_element_by_class_name("ico-register")
reg_btn.click()

reg_title = driver.find_element_by_class_name("page-title")
# reg_title.is_displayed()/
print(reg_title.is_displayed())

time.sleep(5)
driver.close()
driver.quit()
print("Test Success")
