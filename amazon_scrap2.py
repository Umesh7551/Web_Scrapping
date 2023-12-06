import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the Chrome WebDriver
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("mobiles")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, "//span[text()='Vivo']").click()

# Find all product elements
products = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

product_info = []

for product in products:
    try:
        # Extract product name
        name_element = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
        product_name = name_element.text.strip()

        # Extract product price
        price_element = product.find_element(By.XPATH, ".//span[@class='a-price-whole']")
        product_price = price_element.text.strip()

        # Extract number of reviews
        reviews_element = product.find_element(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
        product_reviews = reviews_element.text.strip()

        # Extract product image URL
        image_element = product.find_element(By.XPATH, ".//img[@srcset]")
        product_image_url = image_element.get_attribute("srcset").split(", ")[-1].split(" ")[0]

        product_info.append({
            "Product Name": product_name,
            "Product Price": product_price,
            "Number of Reviews": product_reviews,
            "Product Image URL": product_image_url,
        })
    except Exception as e:
        print(f"Error processing product: {str(e)}")

# Print or save product_info as needed
for info in product_info:
    print(info)

# import pandas as pd
# output_directory = os.path.expanduser("~") + "/Downloads/"
# df = pd.DataFrame(zip(product_name, product_price, product_reviews, product_image_url), columns=['Product Name', 'Product Price', 'Product Reviews', 'Product Image Url'])
# file_path = output_directory + "Product_Info.xlsx"
# df.to_excel(file_path, index=False)


# Close the WebDriver
driver.quit()
