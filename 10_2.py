'''
This exercise continues with the code made in the last exercise.
In the last exercise one of the objectives was to create a class with two attributes,
teamcolor and points. Now, add two methods called "tellscore" and "goal".
When the method "tellscore" is called, the objects prints out "I am [teamcolor],
we have [points] points!", and if the method goal is called, the object adds
one point to the attribute points. Also make the attribute points a private
attribute, and to accommodate that change, make the neccessary changes to get
the class to work properly.


Then modify the program's main function so that instead of printing the data itself,
the main function first calls the method "goal" and then the method "tellscore".
'''

# -*- coding: cp1252 -*-
class Player:
    teamcolor = "Blue"
    __points = 0

    def tellscore(self):
        print("I am", self.teamcolor+", we have", self.__points, "points!")
    def goal(self):
        self.__points += 1        
    def printout(self):
        print("The", self.teamcolor,"contender has", self.__points,"points!")

def main():
    bigman = Player()
    bigman.goal()
    bigman.tellscore()

if __name__=="__main__":
    main()
