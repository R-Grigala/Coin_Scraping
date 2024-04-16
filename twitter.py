from selenium import webdriver
from selenium.webdriver.common.by import By



# Function to check if Twitter link exists on the given site_url
def check_twitter_exist(site_url, twitter_urls_list):
    try:
        # Launch a headless Chrome browser using Selenium
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=option)
        driver.set_window_size(2000, 800)

        # driver = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument("--headless"))

        driver.get(site_url)
        # socials_elements = driver.find_elements(By.CLASS_NAME, "sc-f70bb44c-0.sc-7f0f401-0.jSheWZ")
        social_href = ""

        twitter_urls_list  = social_href
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

# URLs to check
twitter_urls = ['', 'https://twitter.com/ethereum', 'https://twitter.com/tether_to']



def main():
    twitter_urls_list = []
    # twitter_urls =   # Initialize result list
    print(twitter_urls)
    check_twitter_exist('https://twitter.com/ethereum', twitter_urls_list)

if __name__ == "__main__":
    main()