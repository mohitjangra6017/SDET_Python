from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

driver = None

@allure.severity(allure.severity_level.NORMAL)
@pytest.fixture(scope='module')

@allure.severity(allure.severity_level.MINOR)
def init_driver():
    global driver
    print("--------------------setup---------------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")
    logo = driver.find_element_by_xpath('//*[@id="gb"]/div/div[1]/div/div[1]/a').is_displayed()
    if logo == True:
        assert True
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Test", attachment_type=AttachmentType.png)
        assert False

    yield
    print("--------------------tear down---------------")
    driver.quit()


@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"


@pytest.mark.usefixtures("init_driver")
def test_google_url():
    assert driver.current_url == "https://www.google.com/?gws_rd=ssl"
