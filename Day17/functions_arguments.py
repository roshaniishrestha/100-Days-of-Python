def numb(a=6, b=2):
    print("The addition:", a+b)

numb(a=4)#output 4+2 = 6

numb(3,4) #output The addition: 7


def average(*numbers):
    print(type(numbers))
    sum = 0 
    for i in numbers:
        sum = sum + i 
    # print("Average is: ", sum / len(numbers))
    # return 7
    return sum/len(numbers)

c = average(1,2,3) # c is calling function which gets the value from return 
print(c)
print(type(c))