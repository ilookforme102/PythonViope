# -*- coding: cp1252 -*-
fname=input("Give a file name: ")
userinput=input("Write something: ")
readfile=open(fname, "w")
readfile.write(userinput)
readfile.close()
print("Wrote", userinput, "to the file", fname+".")
