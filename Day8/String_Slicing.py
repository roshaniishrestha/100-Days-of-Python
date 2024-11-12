name = "roshani, Shrestha"
print("total length of name:", len(name), name)
print(name[0:7]) #prints -> roshani
print(name[2:7]) #prints -> shani
print(name[-7: -2]) #17-7-> 10   17-2-> 15    10:15-> hrest  
print(name[2: -7]) #prints-> shani, S
print(name[8:17]) #prints ->  Shrestha
print(name[9:]) #prints -> Shrestha
print(name[:17]) #prints roshani, Shrestha
print(name[0:17])#prints roshani, Shrestha
print(name[0:-8])#prints roshani,
print(name[0:len(name)-10])#prints roshani
print(name[1::2])  #prints-> ohn,Srsh
print(name[::2])  #prints-> rsai heta
print(name[1::3]) #prints oa,hsa
print(name[-1:len(name)-10]) #-> [-1:7]
# The slicing name[-1:len(name)-10] does not work because the start index -1 (last character) is greater than the stop index 7 (len(name) - 10), resulting in an invalid range. In Python slicing, the start index must be less than the stop index to extract a substring correctly.