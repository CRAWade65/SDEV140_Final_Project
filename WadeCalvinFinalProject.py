"""
Author: Calvin Wade
Date Written: Started 9/26/2024, Finished 10/11/2024
Assignment: Module 8 Final Project
This program is a sandwich making application that utilizes a GUI for easier usage.
"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter import Tk



class subMaker(EasyFrame):
    """A GUI for making sub sandwiches"""
    root = Tk()
    def __init__(self):
        """Creates the many different aspecs of the sub sandwich maker, includes different types of buttons and labels for defining and selecting different parts of
        the sandwich making process."""
        EasyFrame.__init__(self, title= "Super Sammy's Super Sub Maker")
        # This section loads and inserts the images at the header and footer of the GUI.
        self.headerimage = PhotoImage(file= "SubSandwichProgramHeader.gif")
        self.footerImage = PhotoImage (file= "SubSandwichProgramFooter.png")
        headerLabel = self.addLabel(text="", row=0, column=0, columnspan=8)
        headerLabel ["image"] = self.headerimage
        footerLabel = self.addLabel(text="", row=6, column=0, columnspan=8)
        footerLabel ["image"] = self.footerImage
        # This section utilizes radio buttons to allow the user to select bread type.
        self.addLabel(text="Bread type", row=1, column=0)
        self.breadGroup = self.addRadiobuttonGroup(row=2, column=0, rowspan=4)
        defaultBread = self.breadGroup.addRadiobutton(text="Artisan Italian")
        self.breadGroup.setSelectedButton(defaultBread)
        self.breadGroup.addRadiobutton(text="Flatbread")
        self.breadGroup.addRadiobutton(text="Multigrain")
        self.breadGroup.addRadiobutton(text="Honey oat bread")
        # This section utilizes radio buttons to allow the user to select bread length.
        self.addLabel(text="Bread length", row=1, column=1)
        self.lengthGroup = self.addRadiobuttonGroup(row=2, column=1, rowspan=4)
        defaultLength = self.lengthGroup.addRadiobutton(text="4 Inches")
        self.lengthGroup.setSelectedButton(defaultLength)
        self.lengthGroup.addRadiobutton(text="6 Inches")
        self.lengthGroup.addRadiobutton(text="8 Inches")
        self.lengthGroup.addRadiobutton(text="10 Inches")
        self.lengthGroup.addRadiobutton(text="12 Inches")
        # This section utilizes radio buttons to allow the user to select bread toasted level.
        self.addLabel(text="Toasted level", row=1, column=2)
        self.toastedGroup = self.addRadiobuttonGroup(row=2, column=2, rowspan=4)
        defaultToast = self.toastedGroup.addRadiobutton(text="Untoasted")
        self.toastedGroup.setSelectedButton(defaultToast)
        self.toastedGroup.addRadiobutton(text="Lightly toasted")
        self.toastedGroup.addRadiobutton(text="Toasted")
        self.toastedGroup.addRadiobutton(text="Well toasted")
        # This section utilizes check buttons to allow the user to select as many meat toppings as the want.
        self.addLabel(text="Meat toppings", row=1, column=3)
        self.meatRBCB = self.addCheckbutton(text="Roast beef", row=2, column= 3)
        self.meatHCB = self.addCheckbutton(text="Ham", row=3, column=3)
        self.meatCCB = self.addCheckbutton(text="Chicken", row=4, column=3)
        self.meatTCB =  self.addCheckbutton(text="Turkey", row=5, column=3)
        # This section utilizes check buttons to allow the user to select as many cheese toppings as the want.
        self.addLabel(text="Cheese toppings", row=1, column=4)
        self.cheesePCB = self.addCheckbutton(text="Provolone", row=2, column=4)
        self.cheeseCCB = self.addCheckbutton(text="Chedder", row=3, column=4)
        self.cheeseSCB = self.addCheckbutton(text="Swiss", row=4, column=4)
        self.cheeseACB = self.addCheckbutton(text="American", row=5, column=4)
        # This section utilizes check buttons to allow the user to select as many vegetable toppings as the want.
        self.addLabel(text="Vegetable toppings", row=1, column=5)
        self.veggieLCB = self.addCheckbutton(text="Lettuce", row=2, column=5)
        self.veggieTCB = self.addCheckbutton(text="Tomato", row=3, column=5)
        self.veggieSCB = self.addCheckbutton(text="Spinach", row=4, column=5)
        self.veggieCCB = self.addCheckbutton(text="Cucumber", row=5, column=5)
        # This section utilizes check buttons to allow the user to select as many sauce toppings as the want.
        self.addLabel(text="Sauce toppings", row=1, column=6)
        self.sauceMayoCB = self.addCheckbutton(text="Mayonaise", row=2, column=6)
        self.sauceMusCB = self.addCheckbutton(text="Mustard", row=3, column=6)
        self.sauceRCB = self.addCheckbutton(text="Ranch", row=4, column=6)
        self.sauceSCB = self.addCheckbutton(text="Siracha", row=5, column=6)
        finishButton = self.addButton(text="Finish your sandwich", row=1, column=7,rowspan=8, command= self.finishOrder)

    

    
    def finishOrder(self):
        """Check all the selected buttons and displays the completed sandwich."""
        self.workingOrder = "Your order is a \n" # Initialization of the variable that will contain the user's selections.
        # This section collects and inserts the bread type, bread length, and bread toasted level into the workingOrder variable.
        self.workingOrder += self.breadGroup.getSelectedButton() ["text"] + ", "
        self.workingOrder += self.lengthGroup.getSelectedButton() ["text"] + ", "
        self.workingOrder += self.toastedGroup.getSelectedButton() ["text"] + ", \n"
        # This section analyzes all of the different topping fields and adds the ones that are checked to workingOrder.
        if self.meatRBCB.isChecked():
            self.workingOrder += "Roast beef, "
        if self.meatHCB.isChecked():
            self.workingOrder += "Ham, "
        if self.meatTCB.isChecked():
            self.workingOrder += "Turkey, "
        if self.meatCCB.isChecked():
            self.workingOrder += "Chicken, "
        self.workingOrder += "\n"
        if self.cheeseACB.isChecked():
            self.workingOrder += "American cheese, "
        if self.cheesePCB.isChecked():
            self.workingOrder += "Provolone cheese, "
        if self.cheeseCCB.isChecked():
            self.workingOrder += "Chedder cheese, "
        if self.cheeseSCB.isChecked():
            self.workingOrder += "Swiss cheese, "
        self.workingOrder += "\n"
        if self.veggieCCB.isChecked():
            self.workingOrder += "Cucumber, "
        if self.veggieLCB.isChecked():
            self.workingOrder += "Lettuce, "
        if self.veggieSCB.isChecked():
            self.workingOrder += "Spinach, "
        if self.veggieTCB.isChecked():
            self.workingOrder += "Tomato, "
        self.workingOrder += "\n"
        if self.sauceMayoCB.isChecked():
            self.workingOrder += "Mayonaise, "
        if self.sauceMusCB.isChecked():
            self.workingOrder += "Mustard, "
        if self.sauceRCB.isChecked():
            self.workingOrder += "Ranch, "
        if self.sauceSCB.isChecked():
            self.workingOrder += "Siracha, "
        self.workingOrder += "Sandwich"
        self.finalOrder = self.messageBox(message=self.workingOrder) # Displays the user's order in a message box.
    

def main():
    subMaker().mainloop()
if __name__ == "__main__":
    main()