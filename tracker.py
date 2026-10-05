# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 190,
    "MSFT": 420
}

total_investment = 0

print("===================================")
print("      STOCK PORTFOLIO TRACKER")
print("===================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

# Number of stocks
number_of_stocks = int(input("\nHow many different stocks do you want to add? "))

portfolio = []

# Take user input
for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    price = stock_prices[stock_name]
    investment = price * quantity

    total_investment += investment

    portfolio.append({
        "stock": stock_name,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

# Display portfolio
print("\n===================================")
print("          YOUR PORTFOLIO")
print("===================================")

for item in portfolio:
    print(
        f"{item['stock']} | "
        f"Quantity: {item['quantity']} | "
        f"Price: ${item['price']} | "
        f"Value: ${item['investment']}"
    )

print("-----------------------------------")
print(f"Total Investment: ${total_investment}")
print("===================================")