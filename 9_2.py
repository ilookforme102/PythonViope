'''
In the second exercise the idea is to create a small grocery shopping list
with the list datastructure. In short, create a program that allows the user
to (1) add products to the list, (2) remove items and (3) print the list and
quit.

If the user adds something to the list, the program asks "What will be added?: "
and saves it as the last item in the list. If the user decides to remove
something, the program informs the user about how many items there are on the
list (There are [number] items in the list.") and prompts the user for the
removed item ("Which item is deleted?: "). If the user selects 0, the first item
is removed. When the user quits, the final list is printed for the user
"The following items remain in the list:" followed by the remaining
items one per line. If the user selects anything outside the options,
including when deleting items, the program responds "Incorrect selection.".
'''

def selection():
    try:
        selection=int(input("Would you like to \n(1)Add or \n(2)Remove items or\n(3)Quit?:"))
        return selection
    except Exception:
        return "wrong"
        
def secondaction(selection, memo):
    if selection == 1:
        memo.append(input("What will be added?: "))
    elif selection == 2:
        print("There are", len(memo),"items in the list.")
        target=int(input("Which item is deleted?: "))
        try:
            memo.pop(target)
        except Exception:
            print("Incorrect selection.")
    elif selection == 3:
        print("The following items remain in the list:")
        for i in memo:
            print(i)
        return "end"
    else:
        print("Incorrect selection.")

def main():
    memo = []
    while True:
        if secondaction(selection(), memo) == "end":
            break

if __name__== "__main__":
    main()
