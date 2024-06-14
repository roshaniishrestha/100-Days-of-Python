v = [1, 5, 3, 99, 55, 66, 77, 88, 5, 5]
print(v)

v.append(7) #adds the value at the end
print(v)

v.reverse() #decending order
print(v)  

v.sort(reverse =True) #decending order
print(v) 

v.sort() #accending order
print( v)

print(v.index(5))

print(v.count(5))

#not recommanded to do 
m = v 
m[0] = 0 #changes the first index value which is 1, into 0 
print(m) #prints after changing 1 into 0
print(v) #value in v also changes 

#recommended way to copy
copy = v.copy() 
print(copy)
copy[1] = 0
print(copy) # 1st index is changed to 0. 
print(v) #no alteration of value in v

v.insert(1,899) #changing the 1st index with 899
print(v)

#to extend
e = ["roshani", "shrestha"]
v.extend(e)
print(v)

#adding list with addition and extend
a = ["apple", "ball", "cat"]
b = ["dog", "elephant"]
c = a + b
print(c)
d = ["frog"]
c.extend(d)
print(c)
