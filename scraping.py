from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

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
url = 'https://coinmarketcap.com'
driver.get(url)

# Slowly scroll down the page
slow_scroll(driver)

# Find elements with the specified class name
# coin_name_elements = driver.find_elements(By.CLASS_NAME, "sc-4984dd93-0.kKpPOn")
# coin_position_number = driver.find_elements(By.CLASS_NAME, "sc-4984dd93-0.iWSjWE")

table = driver.find_elements(By.TAG_NAME, "tbody")
full_table = []
table_text = table[0].text.split("\n")
for text in table_text:
    full_table.append(text)

result_dict = {}
# Iterate over the list in steps of 2
for i in range(0, len(full_table), 9):
    key = int(full_table[i])
    value = full_table[i + 1]
    result_dict[key] = value

print(result_dict)


# Quit the browser
driver.quit()
