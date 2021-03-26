"""
Program goals:
1. Add items to a list (ints)
2. Offer the user a choice of actions
3. Pull the values stored at specific indexes
4. Convert input to INTs
5. Put all action in a while loop
6. Add an exit option

"""
import random
myList = []
unique_list = []
def mainProgram():
    #build our while loop 
    while True:
        print("hello, there! Let's work with lists!")
        print("please choose from the following options. Type the number of the choice")
        choice = input("""1. Add to a list,
2. Return a valuea at a list,
3. Add a bunch of numbers!
4. Random Search
5. Linear seaarch
6. Sort list
7. Quit   """)
        if choice == "1":
           addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            addABunch()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            sortList(myList)
        elif choice == "7":
            printlists()
        else:
            break

def addToList():
    print("adding to a list! Great Choice!")
    newIteam = input("type an integer here!  ")
    myList.append(int(newIteam))
    #we need to think about errors!

def addAvunch():
    print ("we're going to add a bunch of numbers to your list!")
    numToAdd = input("how many new integers would you like to add?  ")
    numRang = input("And how high would you like these numbers to go?  ")
    for x in range(0,int(numToAdd)):
        myList.append(random.ranint(0,  int(numrange)))
    print("Your list is complete!")


def sortList(myList):
    #"miList" is the ARGUMENT this function takes.
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe =  input("Wanna see your new, sorted list?  y/n")
    if showMe.lower() =="Y":
        print(unique_list)


def randomSearch ():
    print("oH, iM sO rAnDoM!!!")
    print(myList[random.randint(0,  len(myList)-1)])


def linearearch():
    print("We're going to go through this list one item at a time!")
    searchValue = input(" What are you looking for?  ")
    for x in range (len(myList)):
        if myList[x] == int(searchValue):
            print(" Your itam is at index position {}".format (x))


def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low)// 2
        if unique_list[mid] == x:
            print("Your number is at index position{}".capitalize.format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid-1, x)
        else:
            return recursiveBinarySearch(unique_list, mid +1, high, x)
    else:
        print("Your number isn't here!")
    
        
def indexValues():
    print("At what index position do you  want to search?")
    indexPos = input( "Type an index position here:    ")
    print(myList[int(indexPos)])



def printList ():
    if len(unique_list)[== 0:
           print(myList)
    else:
        wichOne = input("Wich listdo you want to see? Sorted or un-sorted ?  ")
        if wichOne.lower() == "sorted"
             print (unique_list)
 


if __name__ == "__main__":
    mainProgram()

