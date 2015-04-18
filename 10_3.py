'''
In the third exercise we make one final adjustment to the class by adding initialization data
and a docstring. First add a docstring "Player-class: stores data on team colors and points."
After this, add an initializing method __init__ to the class, and make it prompt the user
for a new player color with the message"What color do I get?: ".


Edit the main function to first create two player objects from the class, player1 and player2.
After this, make the program call player1's method "goal" twice and player2's goal once.
After this, call both objects with the method "tellscore". 
'''

# -*- coding: cp1252 -*-
class Player:
    """Player-class: stores data on team colors and points."""
    teamcolor = "Blue"
    __points = 0

    def __init__(self):
        self.teamcolor=input("What color do I get?: ")
    def tellscore(self):
        print("I am", self.teamcolor+", we have", self.__points, "points!")
    def goal(self):
        self.__points += 1        
    def printout(self):
        print("The", self.teamcolor,"contender has", self.__points,"points!")

def main():
    player1 = Player()
    player2 = Player()
    player1.goal()
    player1.goal()
    player2.goal()
    player1.tellscore()
    player2.tellscore()

if __name__=="__main__":
    main()
