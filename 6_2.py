def poweroftwo(num=0):
    result = 2**num
    return result

def main():
    parameter=int(input("Give a number:"))
    print("The result is", poweroftwo(parameter))

if __name__== "__main__":
    main()
