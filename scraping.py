from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

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
driver.set_window_size(2000, 800)

# Fetch the HTML using Selenium
site_url = os.getenv("SITE_URL")
driver.get(site_url)

# Slowly scroll down the page
slow_scroll(driver)

# Find div elements with the specified class name
urls_elements = driver.find_elements(By.CSS_SELECTOR, ".sc-aef7b723-0.LCOyB")

# Extract URLs
urls = [element.find_element(By.CSS_SELECTOR, "a").get_attribute("href") for element in urls_elements]

# Find table elements
table = driver.find_elements(By.TAG_NAME, "tbody")
table_text = table[0].text.split("\n")

# Construct coin dictionary
coin_dict = {}
for i in range(0, len(table_text), 9):
    key = int(table_text[i])
    value = table_text[i + 1]
    coin_dict[key] = value

# Combine coin dictionary with URLs
result_dict = {}
for key, value in coin_dict.items():
    if 1 <= key <= len(urls):
        result_dict[key] = [value, urls[key - 1]]

print(result_dict)

# Quit the browser
driver.quit()
