def tester(givenstring="Too short"):
    if givenstring.find("X") == -1:
        print(givenstring)
    else:
        print(givenstring)
        print("X spotted!")
    
def main():
    while True:
        string=input("Write something (quit ends):")
        if string=="quit":
            break
        elif len(string)<10:
            tester()
        else:
            tester(string)

if __name__ == "__main__":
    main()
