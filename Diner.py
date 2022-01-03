# Ammar Idrees, idrees@usc.edu
# ITP 115, Fall 2020
# Professor Miller, MW 10-11:20am
# Final Project
# Function: This class represents one of the diners at the restaurant and keeps tracks of
# their status and meal.

# import MenuItem class
from MenuItem import MenuItem

class Diner:
    #  list of strings containing the possible statuses a diner might have:
    STATUSES = ["seated","ordering","eating","paying","leaving"]

    # constructor to instantiate the class
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    # The getter methods (setter methods not needed for this class)
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self): # denotes the actual status action as seen in STATUSES list
        return self.STATUSES[self.status]

    def getStatusInt(self): # denotes index of the status position from STATUSES list
        return self.status

    # method to update the diner status by 1
    def updateStatus(self):
        self.status += 1

    # method to add item to list of menu items
    def addToOrder(self, menuItem):
        self.order.append(menuItem)

    # method to print a message containing all the menu items the diner ordered
    def printOrder(self):
        message = self.getName() + " ordered:" # obtain name of diner
        print("\n" + message)
        for entry in self.getOrder(): # output each entry in order list if not empty
            if not entry == None: # not empty
                print("-" + str(entry))

    # method to calculate the total cost of diner's meal as a float value
    def calculateMealCost(self):
        cost = 0  # the total cost
        for entry in self.getOrder():
            cost += float(entry.getPrice())
        return cost

    # method that outputs string containing the diner’s name and status
    def __str__(self):
        message = "Diner " + self.getName() + " is currently " + self.getStatus()
        return message


