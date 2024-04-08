# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90,100,110,120,130,140,150,160,170,180,190,200,210,220,230]
# result = []
# index = 0

# coins = ['1', 'Bitcoin', 'BTC', '$65,836.05', '0.34% 0.44% 6.02%', '$1,295,975,513,216', '$41,367,391,150', '628,665 BTC', '19,672,012 BTC', '2', 'Ethereum', 'ETH', '$3,307.39', '0.35% 0.11% 7.38%', '$397,367,890,422', '$19,109,947,055', '5,781,798 ETH', '120,069,288 ETH', '3', 'Tether USDt', 'USDT', '$1.00', '0.01% 0.07% 0.05%', '$105,308,278,961', '$80,968,377,526', '80,922,308,511 USDT', '105,280,728,306 USDT']


# # # Iterate over the list until the last index is reached
# # while index < len(coins):
# #     # Add the first two indices
# #     result.extend(coins[index:index+2])
# #     # Move the index pointer by 3 positions
# #     index += 9

# # print(result)

# result_dict = {}

# # Iterate over the list in steps of 2
# for i in range(0, len(coins), 9):
#     key = int(coins[i])
#     value = coins[i + 1]
#     result_dict[key] = value

# print(result_dict)


from selenium import webdriver
from selenium.webdriver.common.by import By
import threading

twitter_urls_list = [""] * 10
# Function to check if Twitter link exists on the given site_url
def check_twitter_exist(site_url, indx):
    try:
        # Launch a headless Chrome browser using Selenium
        # option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        # option.add_argument("--no-sandbox")
        # driver = webdriver.Chrome(options=option)
        # driver.set_window_size(2000, 800)

        driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))

        driver.get(site_url)
        socials_elements = driver.find_elements(By.CLASS_NAME, "sc-f70bb44c-0.sc-7f0f401-0.jSheWZ")
        social_href = ""
        for social_element in socials_elements:
            social_text = social_element.text.split("\n")[-1]
            if social_text == "Twitter":
                social_href = social_element.find_element(By.TAG_NAME, 'a').get_attribute("href")
                break
        twitter_urls_list.insert(indx, social_href)
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

# URLs to check
urls = ['https://coinmarketcap.com/currencies/bitcoin/', 'https://coinmarketcap.com/currencies/ethereum/', 'https://coinmarketcap.com/currencies/tether/', 'https://coinmarketcap.com/currencies/bnb/', 'https://coinmarketcap.com/currencies/solana/', 'https://coinmarketcap.com/currencies/xrp/', 'https://coinmarketcap.com/currencies/cardano/']

# List to store threads
threads = []

# Create and start a thread for each URL
for i in range(0, len(urls)):
    thread = threading.Thread(target=check_twitter_exist, args=(urls[i], i))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()


# Print the list of Twitter URLs
print(twitter_urls_list)

