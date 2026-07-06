a=int(input("enter first number:"))
b=int(input("enter second number:"))
print(F"A is biggest") if a>b else print(f"B is biggest")
biggest=a if a>b else b
print(F"biggest number is {biggest}")