# -*- coding: cp1252 -*-

def getnumber():
    try:
        num=int(input("Give a number: "))
        print("The input was suitable!")
    except Exception:
        print("The input was malformed.")

def main():
    getnumber()

if __name__=="__main__":
    main()
