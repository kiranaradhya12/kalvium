def calculate_min_coins(coins, amount):
    # Sort the coins in descending order
    coins = sorted(coins, reverse=True)

    # Initialize the result list with zeros
    result = [0] * len(coins)

    # Loop through each coin denomination
    for i in range(len(coins)):
        # Calculate the maximum number of coins of this denomination
        max_coins = amount // coins[i]

        # Add the maximum number of coins to the result list
        result[i] = max_coins

        # Update the remaining amount
        amount -= max_coins * coins[i]

    return result

coins = input("Enter the coin denominations (separated by commas): ")
coins = list(map(int, coins.split(",")))
amount = int(input("Enter the amount of change to be made: "))

# Calculate the minimum number of coins required
result = calculate_min_coins(coins, amount)

# Print the result
print("Minimum number of coins required:", result)