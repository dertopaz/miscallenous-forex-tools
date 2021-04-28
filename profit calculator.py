def positionprofit (pipchange: float, lotsize: float) -> float:
    return print((pipchange*0.0001)*(100000*lotsize), "USD")

x = float(input("Enter the estimated profit or loss in pips:"))
y = float(input("Enter the size of the lot (1 lot = 100k units):"))

positionprofit(x, y)



