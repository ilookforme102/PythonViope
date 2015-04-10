num1=input("Give a number: ")
num2=input("Give another number: ")
num1=int(num1)
num2=int(num2)
evencnt=0
if num1%2==0:
    evencnt+=1
if num2%2==0:
    evencnt+=1
if evencnt==0:
    print("Both numbers are odd.")
if evencnt==1:
    print("One of the numbers is even.")
if evencnt==2:
    print("Both numbers are even.")
