# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.
neg = int(input("enter a number that is negative: "))
while neg < 0:
    print (neg)
    break
else:
    print("enter a negative number") 

