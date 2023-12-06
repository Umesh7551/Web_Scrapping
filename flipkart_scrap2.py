import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

search_term = input("Enter the Search Term: ")

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com")
driver.maximize_window()

try:
    driver.find_element(By.XPATH, "//span[@class='_30XB9F']").click()
except:
    pass

driver.find_element(By.XPATH, "//input[@name='q']").send_keys(search_term)
driver.find_element(By.XPATH, "//button[@class='_2iLD__']").click()
# driver.find_element(By.XPATH, "//label[@class='_2iDkf8 t0pPfW']").click()

all_products = driver.find_elements(By.XPATH, "//div[@class='_13oc-S']")
print(len(all_products))
# Find multiple elements using a locator (e.g., CSS selector)
# all_products = driver.find_elements(By.CSS_SELECTOR, "._13oc-S")
product_name = []
product_price = []
product_reviews = []
product_mrp = []
discount = []
sellername = []
final_list = []

for product in all_products:
    product.click()
    driver.switch_to.window(driver.window_handles[1])

    product_name = driver.find_element(By.XPATH, "//span[@class='B_NuCI']").text
    product_price = driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']").text
    try:
        product_mrp = driver.find_element(By.XPATH, "//div[@class='_3I9_wc _2p6lqe']").text
        discount = driver.find_element(By.XPATH, "//div[@class='_3Ay6Sb _31Dcoz']").text
        sellername = driver.find_element(By.ID, "sellerName").text
    except:
        pass



    print(f"Product Name - {product_name}")
    print(f"Product Price - {product_price}")
    try:
        print(f"Product MRP - {product_mrp}")
        print(f"Discount - {discount}")
        print(f"Seller Name- {sellername}")
    except:
        pass

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
import pandas as pd
output_directory = os.path.expanduser("~") + "/Downloads/"
df = pd.DataFrame(zip(product_name, product_price, product_mrp, discount, sellername), columns=['Product Name', 'Product Price', 'Product MRP', 'Discount', 'Seller Name'])
file_path = output_directory + "Product_info.xlsx"
df.to_excel(file_path, index=False)
driver.quit()