'''
The first exercise is related to basic class definition.
Create a program which has a class Player, which has two attributes,
teamcolor and points. Then create a main function which creates
an object from this class, gives its attributes values "Blue" and "300".
After this, make the program print the object data in the form
"The [color] contender has [points] points!" like this:
'''
# -*- coding: cp1252 -*-

class Player:
    teamcolor = "Blue"
    points = "300"

    def printout(self):
        print("The", self.teamcolor,"contender has", self.points,"points!")

def main():
    bigman = Player()
    bigman.teamcolor = "Blue"
    bigman.points = 300
    bigman.printout()

if __name__=="__main__":
    main()
