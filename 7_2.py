'''
The second exercise in this chapter continues
with random selection. In this exercise the objective
is to develop a game called nuke-foot-cockroach, which is
pretty similar to the more popular variant, paper-rock-scissors.
The rules are simple: both players select either nuke,
foot or cockroach, and the winner is determined in the following way:
Foot beats cockroach, nuke beats foot and cockroach beats nuke.
If both the player and the AI select the same, it's a tie,
except if both choose nuke, then both lose.

Implement the game so that the other player is computer controlled,
and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2).
Also implement a feature which keeps the score, calculating both rounds
the player won, and ties. If the player wins, print "You WIN!", if they loose "You LOSE!".
If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on
if the tie was caused by a nuke or not. If the player selects "quit",
the game ends and the final score is given. When the game works correctly,
it prints the following:
'''

# -*- coding: cp1252 -*-

import random

def win():
    print("You WIN!")
    result = 1
    return result

def lose():
    print("You LOSE!")
    result = 3
    return result

def choiceDisplay(user, AI):
    print("You chose:", user)
    print("Computer chose:", AI)

def play(user):
    """ Takes user choice. Select AI's choice randomly. And decide who wins."""
    play=random.randint(1,3)
    if play == 1:
        AI="Foot"
    elif play == 2:
        AI="Nuke"
    elif play == 3:
        AI="Cockroach"

    if (AI==user) and (AI != "Nuke"):
        choiceDisplay(user, AI)
        print("it is a tie!")
        result = 2
        return result
    elif (AI==user) and (AI == "Nuke"):
        choiceDisplay(user, AI)
        print("Both LOSE!")
        result = 3
        return result
    elif user == "Foot":
        choiceDisplay(user, AI)
        if play == 2:
            return lose()
        elif play == 3:
            return win()
    elif user == "Nuke":
        choiceDisplay(user, AI)
        if play == 1:
            return win()
        elif play == 3:
            return lose()
    elif user == "Cockroach":
        choiceDisplay(user, AI)
        if play == 1:
            return lose()
        elif play == 2:
            return win()
    else:
        print("Incorrect selection.")
        return 4
    
def main():
    rounds = 0
    wonrounds = 0
    tierounds = 0
    while True:
        user=input("Foot, Nuke or Cockroach? (Quit ends):")
        if user == "Quit":
            print("You played", rounds, "rounds, and won", wonrounds,\
"rounds, playing tie in", tierounds, "rounds.")
            break
        else:
            result = play(user)
            if result == 1: # When you win
                rounds += 1
                wonrounds += 1
            elif result == 2: # When it's a tie
                rounds += 1
                tierounds += 1
            elif result == 3: # When you lose
                rounds += 1

if __name__=="__main__":
    main()
