'''
Also the other continuous project, the notebook,
has relied on user actions in the sense that it would have broken down
if the user had decided to read the file without writing anything to it.
In this exercise we fix this, and add the possiblity of changing the used notebook file
while the program is running.

First of all, make the program start by checking if there
is a file "notebook.txt" and create one if there is none.
If this has to be done, also inform the user with the warning
"No default notebook was found, created one.".

When this feature works, add a fourth selection to the notebook,
"(4) Change the notebook". If the user selects this option,
the user is prompted for a new file "Give the name of the new file: ".
If there is an existing file, it is opened and loaded into the notebook program,
while the old notebook file is closed. If the new notebook file does not exist,
the system informs the user "No notebook with that name detected, created one."
and makes a new file. Also add a note of the used notebook file to the main menu,
"Now using file [filename]".
'''

import time

def readfile(name):
    while True:
        try:
            readfile = open(name,'r')
            content = readfile.read()
            readfile.close()
            return content
        except IOError:
            emptyfile(name)
            if name == "notebook.txt":
                print("No default notebook was found, created one.")
            else:
                print("No notebook with that name detected, created one.")
                
def writefile(name, uinput):
    try:
        uinput = uinput+":::"
        uinput += time.strftime("%X %x")
        addfile = open(name,'a')
        addfile.write(uinput+"\n")
        addfile.close()
    except IOError:
        return False
    
def emptyfile(name):
    try:
        emptyfile = open(name,'w')
        emptyfile.close()
    except IOError:
        return False 

def main():
    filename="notebook.txt"
    readfile(filename)
    while True:
        print("Now using file", filename)
        selection=input('''(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: ''')
        if selection=='1':
            content=readfile(filename)
            print(content)
        elif selection=='2':
            uinput=input("Write a new note: ")
            writefile(filename, uinput)
        elif selection=='3':
            emptyfile(filename)
            print("Notes deleted.")
        elif selection=='4':
            filename=input("Give the name of the new file: ")
            readfile(filename)
        elif selection=='5':
            print("Notebook shutting down, thank you.")
            break

if __name__ == "__main__":
    main()
