hours=int(input("Enter working hours:"))
if hours ==8:
    wage = 250
    print("wage = Rs.",wage)
elif hours > 8 and hours <= 10:
    wage = 250 + (hours - 8)*50
    print("wage = Rs.",wage) 
elif hours > 10 and hours <= 12:
    wage = 250 + (2 * 50) + (hours - 10)*75
    print("wage = Rs.",wage)
elif hours > 12 and hours <= 14:
    wage = 250 + (2 * 50) + (2 * 75) + (hours - 12) * 100
    print("wage = Rs.",wage)
else:
    print("Invalid working hour")