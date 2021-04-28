def pricechange(profit: float, lotsize:float) -> float:
    return print("The price will need to increase by",((profit/(lotsize*100000))/0.0001), "pips in order to achieve your profit.")


x = float(input("Enter the desired profit in USD:"))
y = float(input("Enter the lotsize:"))

pricechange(x, y)