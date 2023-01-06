from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time
class Test_Manoj:
url = "https://opensource-demo.orangehrmlive.com"
# Booting Method for running the Python Tests
@pytest.fixture
def booting_function(self):
self.driver = webdriver.Chrome()
yield
self.driver.close()
def test_get_title(self, booting_function):self.driver.get(self.url)
assert self.driver.title == 'Manoj'
print("SUCCESS # Web Title Captured Successfully")
def test_login(self, booting_function):self.driver.get(self.url)
time.sleep(5)
self.driver.find_element(by=By.NAME,
value=data.Manoj_Selectors.input_box_username).send_keys(data.Manoj_Data.username)
self.driver.find_element(by=By.NAME,value=data.Manoj_Selectors.input_box_password).send_keys(data.Manoj_Data.password)
self.driver.find_element(by=By.XPATH,value=data.Manoj_Selectors.login_xpath).click()
assert self.driver.title == 'OrangeHRM'
print("SUCCESS # LOGGED IN WITH USERNAME {username} and PASSWORD{password}".format(username=data.Manoj_Data.username,password=data.Manoj_Data.password))


#search box
self.driver.find_element(By.XPATH,value= '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input').click()
self.driver.find_element()