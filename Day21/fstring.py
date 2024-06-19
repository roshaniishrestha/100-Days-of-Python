#3.6feature of python -fstrings
# what is string formatting?
letter = "Hey my name is {} and i am from {}"
country ="Nepal"
name = "Roshani"
print(letter.format(name,country)) #Hey my name is Roshani and i am from Nepal
# if this was written mistakely as then it will print wrong sentence. 
letterr = "Hey my name is {1} and i am from {0}"
print(letterr.format(country,name)) #Hey my name is Roshani and i am from Nepal
print(letterr.format(name,country)) #Hey my name is Nepal and i am from Roshani

# Here the problem is we have to write long code and remamber the number at which at parameter need to be set

#fstring solves this problem
#example1
print(f"Hey my name is {name} and i am from {country}") #Hey my name is Roshani and i am from Nepal
#if you want to print {name} as it is
print(f"Hey my name is {{name}} and i am from {{country}}") #Hey my name is {name} and i am from {country}

#example2
orange = "price of orange is {price:.3f} rupees" #.3f means .667
print(orange.format(price = 250.6666667890)) #price of orange is 250.667 rupees
orangetoday = orange.format(price = 400.89999)
orangeyesterday = orange.format(price=500.88899)
print(orangetoday) #price of orange is 400.900 rupees
print(orangeyesterday) #price of orange is 500.889 

#example3
print(f"{3*60}")
print(type(f"3*60"))