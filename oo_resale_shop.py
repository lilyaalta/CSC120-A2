from computer import *
from typing import Dict, Optional

class ResaleShop:
    itemID: int
    inventory: dict[int: Computer]

    # What attributes will it need?
        # to buy
        # to sell an item
        # to check inventory 
        # refurbishing a computer
# this is to initialize the inventory and start listing off the items as they come in
    def __init__(self):
        self.inventory = {}
        self.itemID = 0 
        

    def buy(self, Computer: object):
        # When the shop purchases a computer, it will put the computer information in the value, as well as the number of the computer
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = Computer
        return self.itemID
    
    # this will print the dictionary of the computer 
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].stringifycomputer()}')
        else:
            print("No inventory to display.")

# this function will look for the item in the computer dictionary. If it is there, then it will be sold and deleted. If it is not there it will tell the user so.
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

# this function will replace the updated version of the refurbished computer
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.updateprice(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.updateprice(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.updateprice(500) # discounted price on machines 4-to-10 year old machines
            else:
                computer.updateprice(1000) # recent stuff

            if new_os is not None:
                computer.updateos(new_os) # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


    # What methods will you need?
    # def buy(self, computer(description)):
    #     global itemID
    #     itemID = itemID + 1
    #     inventory[itemID] = computer
    #     return itemID
    # def update_price(self):
    #     pass
    # def sell(self):
    #     pass
    # def update_OS(self):
    #     pass
    # def refurbish(self):
    #     pass
        


    # 1.1 call Computer(...) constructor to creat a new computer instance
    # 2. call inventory.append(...) to add the new computer insatance to the inventory
