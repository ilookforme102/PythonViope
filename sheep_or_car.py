"""
There's a TV show. In the show, there are 3 doors. There's a ship behind 2 doors, and a car behind the other door.
Contestant choose one door, then the emcee will show a door that a sheep is behind it. Then the contestant changes
the choice. If there was a car behind the chosen door, the contestant will win a car. What will be the chance of 
winning the car. Will it be better than just sticking to the first choice(which is 1/3 chance)?
(The theoretical chance is 2/3 chance.)
"""

import random

def tv_show(freecar):
    car = random.randint(0,2)
    choice = random.randint(0,2)
    while True:
        show_ship = random.randint(0,2)
        if (show_ship != choice) and (show_ship != car):
            print ("car is", car)
            print ("choice is", choice)
            print ("showship is", show_ship)
            break
    while True:
        second_choice = random.randint(0,2)
        if (second_choice != choice) and (second_choice != show_ship):
            print ("second choice is", second_choice)
            break
    if second_choice == car:
        freecar = freecar + 1
        print ("You won " + str(freecar) + "cars.")
        return freecar 
    else:
        print ("You did not won the car.")
        return freecar 

def main():
    freecar = 0
    i = 0
    while i < 100:
        freecar = tv_show(freecar)
        i = i + 1
        print ("This is tv show number " + str(i) + "\n")
    print("Chance to win a car is " + str(100*(freecar/i))+"%")

if __name__=="__main__":
    main()
