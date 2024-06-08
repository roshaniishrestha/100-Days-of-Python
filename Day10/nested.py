num = int(input("Enter your price: "))
appleprice = 250
extramoney = appleprice-num
if (appleprice-num > 0):
    print("The apple's price is reasonable. You will save", appleprice-num)
elif (appleprice - num == 0):
    print("Today, no discount")
elif (appleprice - num <= 0):
    if(num- appleprice <= 5):
        print("you need to add less than ot equal to Rs5")
    elif(num -appleprice <=10):
        print("you need to add betweeen 5-10 rs", appleprice -num)
    elif(num - appleprice <= 20):
        print("you need to add between 10-20 rs i.e", appleprice-num)
    else:
        print("you dont have enough money. you will need extra", -(appleprice - (num)), "money")
else:
    print("Please give valid number")