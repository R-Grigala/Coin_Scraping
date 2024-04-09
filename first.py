# items = list(range(1, 101))  # Creating a list of 100 items for demonstration

# print(items)
# # Printing in five parts
# part_size = 4

# for i in range(0, len(items), part_size):
#     print("Part:")
#     for j in range(part_size):
#         index = i + j
#         if index < len(items):
#             print(index)

twitter_urls_list = ['', 'https://twitter.com/ethereum', 'https://twitter.com/tether_to', 'https://twitter.com/bnbchain', 'https://twitter.com/solana', 'https://twitter.com/Ripple', 'https://twitter.com/circle', 'https://twitter.com/dogecoin', 'https://twitter.com/ton_blockchain', 'https://twitter.com/cardano']

result_dict = {1: ['Bitcoin', 'https://coinmarketcap.com/currencies/bitcoin/'], 2: ['Ethereum', 'https://coinmarketcap.com/currencies/ethereum/'], 3: ['Tether USDt', 'https://coinmarketcap.com/currencies/tether/'], 4: ['BNB', 'https://coinmarketcap.com/currencies/bnb/'], 5: ['Solana', 'https://coinmarketcap.com/currencies/solana/'], 6: ['XRP', 'https://coinmarketcap.com/currencies/xrp/'], 7: ['USDC', 'https://coinmarketcap.com/currencies/usd-coin/'], 8: ['Dogecoin', 'https://coinmarketcap.com/currencies/dogecoin/'], 9: ['Toncoin', 'https://coinmarketcap.com/currencies/toncoin/'], 10: ['Cardano', 'https://coinmarketcap.com/currencies/cardano/']}

# Create a new dictionary containing the merged information with Twitter URLs
full_result_dict = {}
for key, value in result_dict.items():
    if 1 <= key <= len(twitter_urls_list):
        full_result_dict[key] = [value[0], value[1], twitter_urls_list[key - 1]]

print(full_result_dict)