from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/")

print(driver.title)

create_account = driver.find_element(By.XPATH, "//a[text()='Create New Account']")

print(create_account.click(), "register_button working successfully")

pop_header_signup = driver.find_element(By.XPATH, "//div[contains(@class,'_52lr fsm fwn fcg')]")
print("SignUp Visible on UI is ", pop_header_signup.is_displayed())

popup_tagline = driver.find_element(By.XPATH, "//div[contains(@class,'_52lr fsm fwn fcg')]")
print("'It's quick and easy.' is visible", popup_tagline.is_displayed())

firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
surname = driver.find_element(By.XPATH, "//input[@name='lastname']")
mobile_email = driver.find_element(By.XPATH, "//input[@name='reg_email__']")
new_password = driver.find_element(By.XPATH, "//input[@name='reg_passwd__']")

female_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Female']")
male_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Male']")
custom_label = driver.find_element(By.XPATH, "//span[contains(@class,'_5k_2 _5dba')]//label[text()='Custom']")

