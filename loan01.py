# Create initial balance for user 1 and user 2. 
# This is hard coded. Of course, it should be read and calculated directly....
bal_user1 = 21.82233503
bal_user2 = 5.27438039

# Calculate percentage of capital for each user
# Formula is 100 * bal_user2 / ( bal_user1 + bal_user2)
percent_capi_user2 = 100 * bal_user2 / ( bal_user1 + bal_user2)
percent_capi_user1 = 100 - percent_capi_user2
print("User 1 as " + str(percent_capi_user1) + (" % of the capital"))
print("User 2 as " + str(percent_capi_user2) + (" % of the capital"))

# The current profit. Later on this should be a user input, 
# then should be read from the exchange directly ....
current_profit = 0.00169001

# Calculate profit of user1 in function of ownership percentage of the capital
# formula is : current_profit * (percent_capi_user1 / 100)
user1_profit = current_profit * (percent_capi_user1 / 100)
print("User 1 as just made a profit of " + str(user1_profit) + (" ETH"))

# Calculate profit of user2 in function of ownership percentage of the capital, before fees¶
# formula is : current_profit - user1_profit
user2_profit_brut = current_profit - user1_profit
print("Before a 5% fees, User 2 as made a profit of " + str(user2_profit_brut) + (" ETH"))

# Calculate profit of user2, after 5% fees
fees = (user2_profit_brut) * 5/100 
user2_profit_net = user2_profit_brut - fees
print("After 5% fees, User 2 as made a profit of " + str(user2_profit_net) + (" ETH"))

# Calculate the updated balances for users
new_bal_user1 = bal_user1 + fees + user1_profit
new_bal_user2 = bal_user2 + user2_profit_net
print("User 1 as a capital of " + str(new_bal_user1))
print("User 2 as a capital of " + str(new_bal_user2))

