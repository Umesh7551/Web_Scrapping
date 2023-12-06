import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# print("HI")
username = driver.find_element(By.NAME, "username")
# username = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']")
# username = driver.find_element(By.CLASS_NAME, "oxd-input oxd-input--active")
username.clear()
username.send_keys("Admin")
# password = driver.find_element(By.NAME, "password")
# password = driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']")
password = driver.find_element(By.CLASS_NAME, "oxd-input oxd-input--active")
password.clear()
password.send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()
# driver.find_element(By.CLASS_NAME, "oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.quit()