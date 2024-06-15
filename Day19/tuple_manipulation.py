nepal = ("pokhara", "Lamjung", "KTM")
convert = list(nepal) #tuple-> list conversion
print(type(nepal))
print(type(convert))
convert.append("222") #adds 222 at last
convert.pop(0) #removes oth index i.e pokhara
print(convert)
convert[2] = "Chitwan" #changes 2th index
print(type(convert), convert) 
nepal = tuple(convert) # list -> Tuple
print(type(nepal), nepal)



indexing = ("rosh",1,"shre",4,3,2,5,6,4,4,4,4,5)
countt= indexing.index(4, 5, -3) 

#-> 2,5,6,4,4,4 it searches for 4 values index no. 

print(countt)

