# Stock Portfolio Tracker


# Dictionary containing stock prices

stock_prices = {
    "AAPL": 188,
    "TSLA": 250,
    "GOOGLE": 140,
    "MSFT": 420,
    "AMZN": 180
}


# Store total investment

total_investment = 0


# Store portfolio details

portfolio = []


print("===== STOCK PORTFOLIO TRACKER =====")


# Number of stocks user wants to enter

number = int(input("How many stocks do you want to add? "))


# Loop for taking input

for i in range(number):

    stock_name = input("\nEnter stock name: ").upper()

    quantity = int(input("Enter quantity: "))


    # Check stock availability

    if stock_name in stock_prices:

        price = stock_prices[stock_name]


        investment = price * quantity


        total_investment += investment


        portfolio.append(
            [stock_name, quantity, price, investment]
        )


    else:

        print("Stock not available!")



# Display portfolio

print("\n===== YOUR PORTFOLIO =====")


for stock in portfolio:

    print(
        stock[0],
        "- Quantity:",
        stock[1],
        "- Price:",
        stock[2],
        "- Value:",
        stock[3]
    )


print("\nTotal Investment Value = $", total_investment)



# Saving result into file

file = open("portfolio.txt","w")


file.write("Stock Portfolio Report\n")
file.write("---------------------\n")


for stock in portfolio:

    file.write(
        f"{stock[0]}  Quantity:{stock[1]}  Value:{stock[3]}\n"
    )


file.write(
    f"\nTotal Investment = {total_investment}"
)


file.close()


print("\nPortfolio saved successfully!")