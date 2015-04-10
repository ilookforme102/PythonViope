# -*- coding: cp1252 -*-


handle = open("strings.txt","r")

line = ""
while True:
    line = handle.readline()
    if line == "":
        break
    line = line[:-1]
    if line.isalnum() == False:
        print(line, "was invalid.")
    else:
        print(line, "was ok.")

handle.close()
