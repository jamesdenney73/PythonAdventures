prompt1 = input("Enter a number: ")
prompt2 = input("Enter another number: ")
dif = float(prompt1) - float(prompt2)
print (f"The differnece between {prompt1} and {prompt2} is an integer? {dif.is_integer()}!")