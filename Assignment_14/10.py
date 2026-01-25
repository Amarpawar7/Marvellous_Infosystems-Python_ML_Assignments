Largest= lambda a, b, c : a if ((a > b) and (a > c)) else (b if (b > c) else c)

Ret = Largest(11, 21, 51)

print("Largest number is : ",Ret)
