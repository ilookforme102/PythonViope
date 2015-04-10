# -*- coding: cp1252 -*-


handle = open("strings.txt","r")

for aline in handle:
    aline = aline[:-1]
    if (aline.isalnum()) or (aline.isalpha()):
        print(aline+" was ok.")
    else:
        print(aline+" was invalid.")
