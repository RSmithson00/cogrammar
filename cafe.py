#brief: to calculate and print total_stock price - loop through lists and dicts
# items as keys to access stock and price
# item_value = stock value x price value
# item_value = (stock[items] * [price[items]])

#menu of 4 items
menu = ["cake", "coffee", "chai", "sandwich"]
# stock value for each menu item in dict

stock_dict = {"cake": 12,
         "coffee": 50,
         "chai": 90,
         "sandwich": 5,
         }

# price dictionary - price for each menu item

prices_dict = {"cake": 3,
         "coffee": 2,
         "chai": 1.5,
         "sandwich": 3.5,
         }

#create two lists, one for prices, one for stock, to make accessing values easier

stock_list = []
prices_list = []

for element in menu:
    stock_list.append(stock_dict.get(element))
    prices_list.append(prices_dict.get(element))

#print(stock_list)
#print(prices_list) - both used during development to test operation of above code

#multiplying the values from the stock_dict, now in stock_list, by the prices_dict values, now in prices_list

item_value_list = []

for i in range(len(stock_list)):
    item_value = stock_list[i] * prices_list[i]
    item_value_list.append(item_value)

# print(item_value_list) - used during development to test operation of above code

#sum the totals of each item (stored in item_value_list)

total_stock = 0

for i in range(len(item_value_list)):
    total_stock = sum(item_value_list)


print(f"The total stock value of the cafe is: £{total_stock:.2f}.")

# NB: I feel that the above (copying to lists, then performing the sum from there) is rather clunky / not efficient.
# but after several attempts to streamline the code I can't seem to make it more efficient! Any advice would be hugely welcome please.