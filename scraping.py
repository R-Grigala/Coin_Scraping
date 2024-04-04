from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# driver = webdriver.Chrome()

# Function to slowly scroll down the page
def slow_scroll(driver):
    current_scroll_position = 0
    while True:
        # Scroll down a small amount
        driver.execute_script("window.scrollTo(0, " + str(current_scroll_position) + ");")
        current_scroll_position += 200  # Adjust the scroll speed by changing this value
        # Check if the bottom of the page is reached
        if current_scroll_position >= driver.execute_script("return document.body.scrollHeight"):
            break

# Launch a headless Chrome browser using Selenium
option = webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=option)
driver.set_window_size(2000,800)

# Fetch the HTML using Selenium
site_url = os.getenv("SITE_URL")
driver.get(site_url)

# Slowly scroll down the page
slow_scroll(driver)

# Find elements with the specified class name
# coin_name_elements = driver.find_elements(By.CLASS_NAME, "sc-4984dd93-0.kKpPOn")

# Find div elements with the specified class name
urls = []
full_table = []
table = driver.find_elements(By.TAG_NAME, "tbody")
urls_elements = driver.find_elements(By.CSS_SELECTOR, ".sc-aef7b723-0.LCOyB")

table_text = table[0].text.split("\n")
for i in range(0,len(urls_elements)):
    href_value = urls_elements[i].find_element(By.CSS_SELECTOR, "a").get_attribute("href").split("\n")
    urls.extend(href_value)

for j in range(0, len(table_text)):
   full_table.append(table_text[j])

coin_dict = {}
result_dict = {}
# Iterate over the list in steps of 2
for i in range(0, len(full_table), 9):
    key = int(full_table[i])
    value = full_table[i + 1]
    coin_dict[key] = value

# Iterate over the keys and values in the coin_dict
for key, value in coin_dict.items():
    # Check if the key is within the range of the urls list
    if 1 <= key <= len(urls):
        # Add the value from the coin_dict and the corresponding URL from the urls list to the result_dict
        result_dict[key] = [value, urls[key-1]]

print(result_dict)


# Quit the browser
driver.quit()
