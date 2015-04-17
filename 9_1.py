# -*- coding: cp1252 -*-

'''
The exercise in the 9th chapter focuses on one of the most powerful
tools in the Python language, the datatype list, and the first assignment
is a simple exercise to create. Define a list which has four items, strings
"Blue","Red","Yellow" and "Green". After this, make a slice from the list
which contains only the first item of the list (list place 0),
and print out all of the items with one for-structure.
'''

def main():
    list=["Blue","Red","Yellow","Green"]
    print("The first item in the list is:", list[0])
    print("The entire list printed one item a time:")
    for i in list:
        print(i)

if __name__ == "__main__":
    main()
