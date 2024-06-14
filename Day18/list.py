marks = [1,6,3,4,5,"science"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[3])
print(marks[5-2])
#same case
print (marks[len(marks)-3]) #positive index
print (marks[-3]) #negetive index

if "science" in marks:
    print("yes") #yes
     
if "roshani" in marks:
    print("yes")
else:
    print("no")  #yes

#sam thing applies for strings as well 
if "sc" in "shrestha":
    print("ok")
else: 
    print("not ok") #not ok
    
#range in list
print(marks[:])#[1, 6, 3, 4, 5, 'science']
print(marks[:-1]) # [1, 6, 3, 4, 5]
print(marks[1:3]) #[6, 3]
print(marks[1:7]) #[6, 3, 4, 5, 'science'] 
print(marks[1:6:2]) #[6, 4, 'science']
# if you dont know the numbers of value in the list 
print(marks[0:len(marks)])
print(marks[0:])
print(marks[:])


#list comprehension
#generating list
lst = [i for i in range(10)]
print(lst) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst = [i for i in range(10) if i%2==0]
print(lst) #[0, 2, 4, 6, 8]



