x = "roshani"
for i in x:
    print (i, end=", ")
    
colors = ["\n", "red", "blue", "pink"]
for color in colors:
    print(color)
    for i in color:
        print(i,"\n") 

for k in range(5): #range is a built in class
    print(k, end=", ") #result -> 0, 1, 2, 3, 4,
print()

for k in range(5): #range is a built in class
    print(k+1, end=", ") #result ->  1, 2, 3, 4,5,
print()

for r in range(2,7):
    print(r, end=", ")