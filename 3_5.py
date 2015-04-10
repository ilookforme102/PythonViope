print("Calculator")
num1=input("Give the first number: ")
num2=input("Give the second number: ")
num1=int(num1) #type conversion
num2=int(num2) #type conversion
print("(1) +\n(2) -\n(3) *\n(4) /\n")
op=input("Please select something (1-4):")
if op=="1":
    result=num1+num2
    print("The result is:",result)
elif op=="2":
    result=num1-num2
    print("The result is:",result)
elif op=="3":
    result=num1*num2
    print("The result is:",result)
elif op=="4":
    result=num1/num2
    print("The result is:",result)
else:
    print("Selection was not correct.")
