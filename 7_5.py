'''
This exercise expands on the calculator, which was made in chapter 4,
exercise 4. In this exercise, add sin() and cos() -calculations
from the library module math to the calculator. Add these actions
as selections 5 and 6, simultaneously moving the "change numbers"
feature to 7 and "Quit" to 8. When the user calls either of the new features,
the first number is the divident and second the divider like this:
sin(number_1/number2).
When correctly implemented, the program prints the following:
'''
import math

print("Calculator")
num1=input("Give the first number: ")
num2=input("Give the second number: ")
num1=int(num1) #type conversion
num2=int(num2) #type conversion
while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\
\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
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
        result=math.sin(num1/num2)
        print("The result is:",result)
    elif op=="6":
        result=math.cos(num1/num2)
        print("The result is:",result)
    elif op=="7":
        num1=int(input("Give the first number: "))
        num2=int(input("Give the second number: "))
    elif op=="8":
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")
