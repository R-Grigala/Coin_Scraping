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

# URLs to check
urls = ['https://coinmarketcap.com/currencies/bitcoin/', 'https://coinmarketcap.com/currencies/ethereum/', 'https://coinmarketcap.com/currencies/tether/', 'https://coinmarketcap.com/currencies/bnb/', 'https://coinmarketcap.com/currencies/solana/', 
        'https://coinmarketcap.com/currencies/xrp/', 'https://coinmarketcap.com/currencies/usd-coin/', 'https://coinmarketcap.com/currencies/dogecoin/', 'https://coinmarketcap.com/currencies/toncoin/', 'https://coinmarketcap.com/currencies/cardano/', 
        'https://coinmarketcap.com/currencies/avalanche/', 'https://coinmarketcap.com/currencies/shiba-inu/', 'https://coinmarketcap.com/currencies/bitcoin-cash/', 'https://coinmarketcap.com/currencies/polkadot-new/', 'https://coinmarketcap.com/currencies/tron/', 
        'https://coinmarketcap.com/currencies/chainlink/', 'https://coinmarketcap.com/currencies/polygon/', 'https://coinmarketcap.com/currencies/near-protocol/', 'https://coinmarketcap.com/currencies/internet-computer/', 'https://coinmarketcap.com/currencies/litecoin/', 
        'https://coinmarketcap.com/currencies/uniswap/', 'https://coinmarketcap.com/currencies/aptos/', 'https://coinmarketcap.com/currencies/unus-sed-leo/', 'https://coinmarketcap.com/currencies/multi-collateral-dai/', 'https://coinmarketcap.com/currencies/ethereum-classic/', 
        'https://coinmarketcap.com/currencies/filecoin/', 'https://coinmarketcap.com/currencies/stacks/', 'https://coinmarketcap.com/currencies/mantle/', 'https://coinmarketcap.com/currencies/cosmos/', 'https://coinmarketcap.com/currencies/arbitrum/', 
        'https://coinmarketcap.com/currencies/cronos/', 'https://coinmarketcap.com/currencies/dogwifhat/', 'https://coinmarketcap.com/currencies/immutable-x/', 'https://coinmarketcap.com/currencies/stellar/', 'https://coinmarketcap.com/currencies/bittensor/', 
        'https://coinmarketcap.com/currencies/render/', 'https://coinmarketcap.com/currencies/hedera/', 'https://coinmarketcap.com/currencies/okb/', 'https://coinmarketcap.com/currencies/first-digital-usd/', 'https://coinmarketcap.com/currencies/vechain/', 
        'https://coinmarketcap.com/currencies/maker/', 'https://coinmarketcap.com/currencies/kaspa/', 'https://coinmarketcap.com/currencies/the-graph/', 'https://coinmarketcap.com/currencies/optimism-ethereum/', 'https://coinmarketcap.com/currencies/injective/', 
        'https://coinmarketcap.com/currencies/pepe/', 'https://coinmarketcap.com/currencies/theta-network/', 'https://coinmarketcap.com/currencies/fantom/', 'https://coinmarketcap.com/currencies/lido-dao/', 'https://coinmarketcap.com/currencies/thorchain/', 
        'https://coinmarketcap.com/currencies/monero/', 'https://coinmarketcap.com/currencies/fetch/', 'https://coinmarketcap.com/currencies/arweave/', 'https://coinmarketcap.com/currencies/core-dao/', 'https://coinmarketcap.com/currencies/celestia/', 
        'https://coinmarketcap.com/currencies/sui/', 'https://coinmarketcap.com/currencies/gala/', 'https://coinmarketcap.com/currencies/algorand/', 'https://coinmarketcap.com/currencies/floki-inu/', 'https://coinmarketcap.com/currencies/aave/', 
        'https://coinmarketcap.com/currencies/flow/', 'https://coinmarketcap.com/currencies/bitcoin-sv/', 'https://coinmarketcap.com/currencies/sei/', 'https://coinmarketcap.com/currencies/bitget-token-new/', 'https://coinmarketcap.com/currencies/ethena/', 
        'https://coinmarketcap.com/currencies/jupiter-ag/', 'https://coinmarketcap.com/currencies/onbeam/', 'https://coinmarketcap.com/currencies/wormhole/', 'https://coinmarketcap.com/currencies/bonk1/', 'https://coinmarketcap.com/currencies/multiversx-egld/', 
        'https://coinmarketcap.com/currencies/pendle/', 'https://coinmarketcap.com/currencies/bittorrent-new/', 'https://coinmarketcap.com/currencies/flare/', 'https://coinmarketcap.com/currencies/ordi/', 'https://coinmarketcap.com/currencies/axie-infinity/', 
        'https://coinmarketcap.com/currencies/dydx-chain/', 'https://coinmarketcap.com/currencies/ecash/', 'https://coinmarketcap.com/currencies/the-sandbox/', 'https://coinmarketcap.com/currencies/quant/', 'https://coinmarketcap.com/currencies/starknet-token/', 
        'https://coinmarketcap.com/currencies/neo/', 'https://coinmarketcap.com/currencies/singularitynet/', 'https://coinmarketcap.com/currencies/nervos-network/', 'https://coinmarketcap.com/currencies/chiliz/', 'https://coinmarketcap.com/currencies/conflux-network/', 
        'https://coinmarketcap.com/currencies/synthetix/', 'https://coinmarketcap.com/currencies/tezos/', 'https://coinmarketcap.com/currencies/worldcoin-org/', 'https://coinmarketcap.com/currencies/eos/', 'https://coinmarketcap.com/currencies/ronin/', 
        'https://coinmarketcap.com/currencies/pyth-network/', 'https://coinmarketcap.com/currencies/decentraland/', 'https://coinmarketcap.com/currencies/mina/', 'https://coinmarketcap.com/currencies/ondo-finance/', 'https://coinmarketcap.com/currencies/kava/', 
        'https://coinmarketcap.com/currencies/apecoin-ape/', 'https://coinmarketcap.com/currencies/jasmy/', 'https://coinmarketcap.com/currencies/sats/', 'https://coinmarketcap.com/currencies/iota/', 'https://coinmarketcap.com/currencies/kucoin-token/'
        ]


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
    twitter_urls_list = [''] * len(urls)  # Initialize result list
    batch_size = 20  # Number of URLs to process in each batch

    num_batches = len(urls) // batch_size  # Calculate the number of batches
    for i in range(num_batches):
        start_index = i * batch_size
        end_index = (i + 1) * batch_size
        threading_urls(start_index, end_index, urls, twitter_urls_list)
        print(f"Batch {i + 1} processing completed.")

    # Print the list of Twitter URLs
    print(twitter_urls_list)

if __name__ == "__main__":
    main()