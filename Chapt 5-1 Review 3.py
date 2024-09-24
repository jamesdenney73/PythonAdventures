n = 1
while True:
    result = 2 ** n
    print (f"{n}")
    if result == float('inf'):
        break
    n -= 5e400

print(f"The smallest n for which 2 ** n returns infinity is: {n}")
