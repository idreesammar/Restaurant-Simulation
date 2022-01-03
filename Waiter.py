# Ammar Idrees, idrees@usc.edu
# ITP 115, Fall 2020
# Professor Miller, MW 10-11:20am
# Final Project
# Function: This class will represent the restaurant’s waiter. who maintains a list of the diners it is
# currently taking care of, and progresses them through the different stages of the restaurant.

# import appropriate classes
from Menu import Menu
from Diner import Diner

class Waiter:
    # constructor to instantiate the class
    def __init__(self, menu):
        self.diners = []
        self.menu = menu

    # function to add new diner to list of diners
    def addDiner(self, newDiner):
        self.diners.append(newDiner)

    # function to determine number of diners currently in list
    def getNumDiners(self):
        return len(self.diners) # output the length of the list

    # function to print current diner statuses (loop through each status and outputs diner in each status)
    def printDinerStatuses(self):
        for status in range(0,5):
            currentStatusList = [] # contains all diners in the current index of status
            for diner in self.diners:
                if diner.getStatus() == Diner.STATUSES[status]: # if current diner is in current phase/status
                    currentStatusList.append(diner)
            print("Diners who are", Diner.STATUSES[status] + ":")
            for customer in currentStatusList:
                print("\t " + str(customer) + "." )


    # function that loops through list of diners, looking for "ordering" diners; then loops through each
    # menu category, printing out the entries; asks diner for one selection from each category
    def takeOrders(self):
        for diner in self.diners:
            if diner.getStatus() == Diner.STATUSES[1]: # looking for "ordering" diners
                print() # newline for neatness
                for index in range(0,len(Menu.MENU_ITEM_TYPES)):
                    menuType = self.menu.MENU_ITEM_TYPES[index] # each category (e.g. appetizer, drink, etc)
                    self.menu.printMenuItemsByType(menuType) # print options for category of menu
                    # obtain user input for choice
                    print(str(diner.name) + ", please select a " + str(menuType) + " menu item number.")
                    choice = int(input("> "))
                    # use while loop for error checking (need appropriate index)
                    while choice < 0 or choice >= self.menu.getNumMenuItemsByType(menuType):
                        choice = int(input("> "))
                    # once choice of integer is appropriate, add dish to the diner
                    diner.addToOrder(self.menu.getMenuItem(menuType,choice))
                    print() # newline for neatness

                # once the diner has ordered one of each dish
                diner.printOrder()

    # function checking for "paying" diners and outputting their order cost
    def ringUpDiners(self):
        for diner in self.diners:
            if diner.getStatus() == "paying":
                cost = diner.calculateMealCost()
                print("\n" + diner.name + ", your meal cost $" + str(cost))

    # function looking for "leaving" diners and outputting appropriate farewell message and removing them
    # from diner list
    def removeDoneDiners(self):
        # use loop to find leaving diners and say goodbye
        for diner in self.diners:
            if diner.getStatus() == "leaving":
                print("\n" + diner.name + ", thank you for dining with us! Come again soon!")
                print() # newline for neatness
        # use backward for loop to remove the diners who have left from the diners list
        for dinerIndex in range(self.getNumDiners()-1,-1,-1):
            if self.diners[dinerIndex].getStatus() == "leaving":
                self.diners.remove(self.diners[dinerIndex]) # remove diner from list

    # function allowing waiters to  attend to the diners at their various
    # stages as well as move each diner on to the next stage
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        # update the status of each diner currently in diner list
        for diner in self.diners:
            diner.updateStatus()









