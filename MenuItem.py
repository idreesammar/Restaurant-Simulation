# Ammar Idrees, idrees@usc.edu
# ITP 115, Fall 2020
# Professor Miller, MW 10-11:20am
# Final Project
# Function: This class will represent a single item that a diner can order from the restaurant’s
# menu.

class MenuItem:
    # constructor to instantiate a class for each menu item
    def __init__(self,name,type,price,description):
        self.name = name  # name of dish
        self.itemType = type  # type of dish; used itemType as name to avoid confusion with Python keyword
        self.price = float(price) # float used to match monetary values
        self.description = description # brief info about the dish

    # 4 getter and 4 setter methods for each characteristic of the dish
    def getName(self):
        return self.name

    def getType(self):
        return self.itemType

    def getPrice(self):
        return self.price

    def getDescription(self):
        return self.description

    def setName(self, inputName):
        self.name = inputName

    def setType(self, inputType):
        self.itemType = inputType

    def setPrice(self, inputPrice):
        self.price = inputPrice

    def setDescription(self, inputDescription):
        self.description = inputDescription

    # method that will construct a string message containing all 4 attributes
    def __str__(self):
        message = self.getName() + " (" + self.getType() + "): $" + str(self.getPrice())
        message += "\n\t" + self.getDescription()
        return message



