print("Calculator")
num1=input("Give the first number: ")
num2=input("Give the second number: ")
num1=int(num1) #type conversion
num2=int(num2) #type conversion
while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
    print("Current numbers:",num1,num2)
    op=input("Please select something (1-6):")
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
    elif op=="5":
        num1=int(input("Give the first number: "))
        num2=int(input("Give the second number: "))
    elif op=="6":
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")
