num = int(input("Enter your price: "))
appleprice = 250
if (appleprice-num > 0):
    print("The apple's price is reasonable. You will save", appleprice-num)
elif (appleprice - num == 0):
    print("Today, no discount")
elif (appleprice - num >= -20):
    print("YOu will need to add less than 20, i.e", -(appleprice-num), "rupees")
else:
    print("No enough money. you will need extra", -(appleprice - (num)), "money")