from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Use in case select any value like dropdown
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")

print(driver.title)

create_account = driver.find_element(By.XPATH, "//a[text()='Create New Account']")

print(create_account.click(), "register_button working successfully")
#
# pop_header_signup = driver.find_element(By.XPATH, "//div[contains(@class,'_52lr fsm fwn fcg')]")
# print("SignUp Visible on UI is ", pop_header_signup.is_displayed())
#
# popup_tagline = driver.find_element(By.XPATH, "//div[contains(@class,'_52lr fsm fwn fcg')]")
# print("'It's quick and easy.' is visible", popup_tagline.is_displayed())
#
# firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
# firstname.send_keys("Mohit")
#
# surname = driver.find_element(By.XPATH, "//input[@name='lastname']")
# surname.send_keys("Jangra")
#
# mobile_email = driver.find_element(By.XPATH, "//input[@name='reg_email__']")
# mobile_email.send_keys("7015103223")
#
# new_password = driver.find_element(By.XPATH, "//input[@name='reg_passwd__']")
# new_password.send_keys("Mohit123")
#
# female_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Female']")
# male_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Male']")
# male_label.click()
#
# custom_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Custom']")
#
# signup_button = driver.find_element(By.XPATH, "//button[@name='websubmit']")
# signup_button.click()
