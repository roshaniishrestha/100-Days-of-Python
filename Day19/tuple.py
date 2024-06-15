tup = (1,2,3,4,3,5)
sets = {1,2,3,4,3,5}
list = [1,2,3,4,3,5]
print(type(tup))
print(type(set))
print(type(list))
#**********************tuple******
a = (1,2,44,3,2,6)
print(type(a), a)
print(a[1]) #tuple indexing simiar to list
print(a[:])
print(a[2])
if 44 in a:
    print("present")
b = a[3:6]
print(b)
#tuble cannot be changed, append or remove if you need to do so you need to convert the tuple into list first.
print(b.count(3)) #works to read
# print(b.append(55)) #doesnot work 

