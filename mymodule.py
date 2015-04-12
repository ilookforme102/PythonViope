''' The third exercise of this chapter goes back
from game programming to a more serious line, and discusses
the creation of self-made modules. Unlike other exercises,
in this exercise the idea is not to create a full program,
but only to write a module for existing software.

The objective is to implement this mymodule-module
applied in the exercise. Create a module,
which has a function printme, which prints
the given parameter with the disclaimer "I got:"
and after that, "The parameter was [length] characters long."
When the module is implemented correctly,
the program prints out the following: '''

def printme(string):
    print("I got: ", string)
    print("The parameter was", len(string), "characters long.")
