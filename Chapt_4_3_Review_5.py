string1 = "Becomes"
string1 = string1.lower()
string2 = "becomes"
string2 = string2.lower()
string3 = "BEAR"
string3 = string3.lower()
string4 = "     Beautiful"
string4 = string4.lstrip()
string4 = string4.lower()
print ("Does " + string1 + " start with be?") 
print (string1.startswith("be"))
print ("Does " + string2 + " start with be?") 
print (string2.startswith("be"))
print ("Does " + string3 + " start with be?") 
print (string3.startswith("be"))
print ("Does " + string4 + " start with be?") 
print (string4.startswith("be"))