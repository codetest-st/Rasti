n1=int(input("Enter the marks Hindi:"))
n2=int(input("Enter the marks English:"))
n3=int(input("Enter the marks Sst:"))
n4=int(input("Enter the marks Maths"))
n5=int(input("Enter the marks Science"))
total=n1+n2+n3+n4+n5
percentage=total/5
print(f"The total marks of 5 subjects is {total}")
print(f"The percentage of 5 subjects is {percentage}")

if percentage >= 95:
    print ("first divison")
elif percentage >=80:
    print ("second division")
elif percentage >=70:
    print ("third division")
elif percentage >=90:
    print("merit")
else:
    print("fail")
