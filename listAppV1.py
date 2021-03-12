"""
Program goals:
1. Add items to a list (ints)
2. Offer the user a choice of actions
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop
6. Add an exit option

"""

myList = []
def mainProgram():
    #build our while loop
    while True:
        print("hello, there! Let's work with lists!")
        print("please choose from the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a valuea at a list,
3.Random Search
4.Quit   """)
        if choice == "1";
           addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        else:
            break

def addToList():
    print("adding to a list! Great Choice!")
    newIteam = input("type an integer here!  ")
    myList.append(int(newIteam))
    #we need to think about errors!


def randomSearch ():
    print("oH, iM sO rAnDoM!!!")
    print(myList[random.randint(0,  len(myList)-1)])


def indexValues():
    print("At what index position do you  want to search?")
    indexPos = input( "Type an index position here:    ")
    print(myList[int(indexPos)])
    



if __name__ == "__main__":
    mainProgram()

