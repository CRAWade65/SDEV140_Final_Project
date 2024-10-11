"""
Author: Calvin Wade
Date Written: Started 9/26/2024, still ongoing
Assignment: Module 8 Final Project
This program is a sandwich making application that utilizes a GUI for easier usage.
"""
from breezypythongui import EasyFrame


class subMaker(EasyFrame):
    """A GUI for making sub sandwiches"""
    def __init__(self):
        """Creates the many different aspecs of the sub sandwich maker, includes different types of buttons and labels for defining and selecting different parts of
        the sandwich making process."""
        EasyFrame.__init__(self, title= "Super Sammy's Super Sub Maker")
        self.addLabel(text="Bread type", row=0, column=0)
        self.breadGroup = self.addRadiobuttonGroup(row=1, column=0, rowspan=2)
        defaultBread = self.breadGroup.addRadiobutton(text="Artisan Italian")
        self.breadGroup.setSelectedButton(defaultBread)
        self.breadGroup.addRadiobutton(text="Flatbread")
        self.breadGroup.addRadiobutton(text="Multigrain")
        self.breadGroup.addRadiobutton(text="Honey oat bread")
        self.addLabel(text="Bread length", row=0, column=1)
        self.lengthGroup = self.addRadiobuttonGroup(row=1, column=1, rowspan=2)
        defaultLength = self.lengthGroup.addRadiobutton(text="4 Inches")
        self.lengthGroup.setSelectedButton(defaultLength)
        self.lengthGroup.addRadiobutton(text="6 Inches")
        self.lengthGroup.addRadiobutton(text="8 Inches")
        self.lengthGroup.addRadiobutton(text="10 Inches")
        self.lengthGroup.addRadiobutton(text="12 Inches")
        self.addLabel(text="Toasted level", row=0, column=2)
        self.toastedGroup = self.addRadiobuttonGroup(row=1, column=2, rowspan=2)
        defaultToast = self.toastedGroup.addRadiobutton(text="Untoasted")
        self.toastedGroup.setSelectedButton(defaultToast)
        self.toastedGroup.addRadiobutton(text="Lightly toasted")
        self.toastedGroup.addRadiobutton(text="Toasted")
        self.toastedGroup.addRadiobutton(text="Well toasted")
        self.addLabel(text="Meat toppings", row=0, column=3)
        self.addCheckbutton(text="Roast beef", row=1, column= 3)
        self.addCheckbutton(text="Ham", row=2, column=3)
        self.addCheckbutton(text="Chicken", row=3, column=3)
        self.addCheckbutton(text="Turkey", row=4, column=3)
        self.addLabel(text="Cheese toppings", row=0, column=4)
        self.addCheckbutton(text="Provolone", row=1, column=4)
        self.addCheckbutton(text="Chedder", row=2, column=4)
        self.addCheckbutton(text="Swiss", row=3, column=4)
        self.addCheckbutton(text="American", row=4, column=4)
        self.addLabel(text="Vegetable toppings", row=0, column=5)
        self.addCheckbutton(text="Lettuce", row=1, column=5)
        self.addCheckbutton(text="Tomato", row=2, column=5)
        self.addLabel(text="Sauce toppings", row=0, column=6)
        self.addLabel(text="Extra Toppings", row=0, column=7)
        self.addLabel(text="Completed order", row=0, column=8)

        




def main():
    subMaker().mainloop()
if __name__ == "__main__":
    main()