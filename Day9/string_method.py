a = "strings"
b = "STRINGS"
c = "string!!!"
d = "this is a String"
e = "RoShaNI"
print(len(a)) #-> 7
print(a.upper()) #-> STRINGS
print(b.lower()) #-> strings
print(e.capitalize()) #-> Roshani
print(c.strip("!")) #->string 
print(a.replace("string", "roshani")) #->roshanis
print(d.split(" ")) #->['this', 'is', 'a', 'String']
print(c.count("!")) #->3
print(d.find("a")) #->8 
print(d.find("aa")) #->-1 (if not found returns -1)
print(d.startswith("String"))#-> false 
print(d.startswith("this")) #->true (this is starting word)
print(e.swapcase()) #-> rOsHAni
f = "roshani\n shrestha"
print(f.isprintable()) #->false
g = "   "
print(g.isspace()) #-> true
print(a.islower())#-> true
print(b.isalnum()) #-> true (returns true only if strings contains A-Z, a-z 0-9)
h= "This is rosh"
i= "This Is Rosh"
print(h.istitle())#->false
print(i.istitle())#->true
print(h.title()) #->This Is Rosh