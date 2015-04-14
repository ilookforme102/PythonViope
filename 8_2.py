# -*- coding: cp1252 -*-

'''
The second exercise combines several normal error scenarios into one program.
In this exercise, create a program which prompts the user for a file name.
Based on user input, open the given file and read the contents into one big string.
Then convert this string to an integer and divides the number 1000 with the number.
Finally, print out the result from the division.

The idea here is that no matter what the user input is, the program works.
If the file cannot be found, the program prints "There seems to be no file
with that name.", if the conversion fails, "The file contents are unsuitable.",
in other errors "There was a problem with the program." or if everything went
correctly, "The result was [result].". In any case (besides KeyboardInterruption
with Ctrl-C),
the program should be impossible to break with user input.
'''

def openfile():
    fname=input("Give the file name: ")
    try:
        sourcefile = open(fname, 'r')
        content = sourcefile.read()
        sourcefile.close()
        return content
    except IOError:
        return False

def conversion(fcontent):
    try:
        fcontent=int(fcontent)
        return fcontent
    except Exception:
        return False

def main():
    result=openfile()
    if result == False:
        print("There seems to be no file with that name.")
    elif conversion(result) == False:
        print("The file contents were unsuitable.")
    else:
        print("The result was", 1000/conversion(result))

if __name__=="__main__":
    main()
