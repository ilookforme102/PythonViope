import random

def coinflip():
    """ Takes nothing, Print out "Tails!" or "Heads!" randomly."""
    flip=random.randint(0,1)
    if flip == 0:
        print("Tails!")
    else:
        print("Heads!")

def main():
    coinflip()

if __name__=="__main__":
    main()
