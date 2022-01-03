# Ammar Idrees, idrees@usc.edu
# ITP 115, Fall 2020
# Professor Miller, MW 10-11:20am
# Final Project
# Function: This class represents the restaurant’s menu which contains four different categories of
# menu items diners can order from

# import MenuItem class
from MenuItem import MenuItem

class Menu:
    # The  4 different types of items on the menu
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    # constructor to instantiate the class
    def __init__(self,fileName):
        inputFile = open(fileName, 'r') # open the csv file to read

        # will create a dictionary to hold menu items for extra credit
        # keys are strings representing type of the items
        # values are lists of MenuItem objects depending on the key
        self.menuItemDictionary = {} # initialize the dictionary
        input = inputFile.readlines() # to neatly/easily read each line of the input file
        for line in input:
            splitLine = line.split(',') # split each line to get each 4 characteristics
            tempItem = MenuItem(splitLine[0], splitLine[1], splitLine[2], splitLine[3])
            if splitLine[1] in self.menuItemDictionary.keys(): # add to each type
                self.menuItemDictionary[splitLine[1]].append(tempItem)
            else: # create new entry if not already made in dictionary
                self.menuItemDictionary[splitLine[1]] = [tempItem]

        inputFile.close()

    # method to get specific menu item
    def getMenuItem(self, menuItem, intIndex):
        return self.menuItemDictionary[menuItem][intIndex]

    # method to output menu items categorized by types
    def printMenuItemsByType(self,menuType):
        message = "-----" + menuType.upper() + "-----\n"
        counter = 0 # represents number of dish of this type (beginning with 0 like the example)
        for item in self.menuItemDictionary.get(menuType):
            message += str(counter) + ") " + str(item)
            counter += 1
        print(message)

    # method to obtain number of items of a certain type
    def getNumMenuItemsByType(self, menuType):
        return len(self.menuItemDictionary.get(menuType))





