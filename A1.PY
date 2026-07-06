sp=int(input("Enter sale price of a product:"))
cp=int(input("Enter cost price of a product:"))
if sp > cp:
    profit=sp -cp
    print (F"The profit is {product} ")
else:
    loss= cp - sp
    print(F"The loss is {loss}")
    