'''
The third exercise also revolves around list methods,
this time doing data manipulation. In the same folder as
the source code, there is a file named "words.txt",
which has a randomly selected set of words. Build a program,
which reads all of the words from the file, sorts them in
alphabetic order and prints out the list with
the statement "Words in an alphabetical order:"
'''
def readfile(name):
    try:
        readfile = open(name,"r")
        words = []
        while True:
            content = readfile.readline()
            if content == "":
                break
            else:
                words.append(content)
        readfile.close()
        return words
    except IOError:
        emptyfile(name)

def emptyfile(name):
    try:
        emptyfile = open(name,'w')
        emptyfile.close()
    except IOError:
        return False

def main():
    filename = "words.txt"
    sortedwords = readfile(filename)
    sortedwords.sort()
    print("Words in an alphabetical order:")
    for i in sortedwords:
        print(i, end="")

if __name__ == "__main__":
    main()
