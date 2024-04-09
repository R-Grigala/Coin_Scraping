from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
import threading

# Load environment variables from .env file
load_dotenv()

def coin_urls(site_url):
    # Launch a headless Chrome browser using Selenium
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=option)
    driver.set_window_size(2000, 800)

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

    # Quit the browser
    driver.quit()
    return result_dict, urls
    
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

# Function to check if Twitter link exists on the given site_url
def check_twitter_exist(site_url, index, twitter_urls_list):
    try:
        # Launch a headless Chrome browser using Selenium
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=option)
        driver.set_window_size(2000, 800)

        # driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))

        driver.get(site_url)
        socials_elements = driver.find_elements(By.CLASS_NAME, "sc-f70bb44c-0.sc-7f0f401-0.jSheWZ")
        social_href = ""
        for social_element in socials_elements:
            social_text = social_element.text.split("\n")[-1]
            if social_text == "Twitter":
                social_href = social_element.find_element(By.TAG_NAME, 'a').get_attribute("href")
                break
        twitter_urls_list[index]  = social_href
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

def threading_urls(start_index, end_index, urls, twitter_urls_list):
    # List to store threads
    threads = []
    
    # Create and start a thread for each URL in the batch
    for index in range(start_index, end_index):
        thread = threading.Thread(target=check_twitter_exist, args=(urls[index], index, twitter_urls_list))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


def main():
    # Fetch the HTML using Selenium
    site_url = os.getenv("SITE_URL")
    result_dict, urls = coin_urls(site_url)
    print("Coin Urls:  ", result_dict)

    # Initialize result list
    twitter_urls_list = [''] * len(urls)  
    batch_size = 20  # Number of URLs to process in each batch

    num_batches = len(urls) // batch_size  # Calculate the number of batches
    # for i in range(num_batches):
    #     start_index = i * batch_size
    #     end_index = (i + 1) * batch_size
    #     threading_urls(start_index, end_index, urls, twitter_urls_list)
    #     print(f"Batch {i + 1} processing completed.")

    # # Print the list of Twitter URLs
    # print("Twitter links: ", twitter_urls_list)

    # Combine coin dictionary with URLs
    # full_result_dict = {}
    # for key, value in result_dict.items():
    #     if 1 <= key <= len(twitter_urls_list):
    #         full_result_dict[key] = [value, twitter_urls_list[key - 1]]



if __name__ == "__main__":
    main()