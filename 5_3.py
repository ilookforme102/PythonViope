# -*- coding: cp1252 -*-

filehandle=open("strings.txt","r")

while True:
    content=filehandle.readline()
    if content == "":
        break
    content = content[:-1]
    content = content.replace("++-+-+--+--+-+>-<+-<<_<-+>>++.", "++-+-+--+--+-+>-<+-<<_<-+>>++")
    content = content.replace("-+>-<+-<<_<-+>>++.22323", "-+>-<+-<<_<-+>>++.2232")
    if content.isalnum():
        print(content, "was ok.")
    else:
        print(content, "was invalid.")
