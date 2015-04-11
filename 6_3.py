def tester(givenstring="Too short"):
    print(givenstring)
    
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
