class Characters:
    """Manages an inventory for the characters of the game."""
    def __init__(self, character_list):
        self.character_list = dict()
        self.txt_file = open("Inventory.txt", "w")
        
    def add_character(self, name, inventory={}):
        """Adds a character to the dictionary."""
        self.character_list[name] = inventory
        self.txt_file.write(f"Welcome {name}! \n{name} has joined the game with {self.character_list[name]}! \n\n")

    def add_item(self, name, item, amount):
        """Adds the type of item and its amount to that character's inventory."""
        self.txt_file.write(f"Adding {amount} {item} to {name}'s inventory... \n")
        try:
            self.character_list[name][item] += amount
        except:
            self.character_list[name][item] = amount
        self.txt_file.write(f"{name}'s number of {item} increased by {amount}! \n{name}'s inventory is now {self.character_list[name]}. \n\n")
        
    def remove_item(self, name, item, amount):
        """Removes the type of item and its amount to that character's inventory."""
        self.txt_file.write(f"Removing {amount} {item} from {name}'s inventory... \n")
        try:
            if self.character_list[name][item] - amount >= 0: 
                self.character_list[name][item] -= amount
                self.txt_file.write(f"Removed {amount} {item} from {name}'s inventory. \n{name}'s inventory is now {self.character_list[name]}. \n")
                if self.character_list[name][item] == 0:
                    self.txt_file.write(f"Warning: {name} has 0 {item} remaining. \n")
            else:
                self.txt_file.write(f"Error: can't remove {amount} {item} as {name} only has {self.character_list[name][item]} of them. \n{name}'s inventory is now {self.character_list[name]}.")
        except:
            self.txt_file.write(f"Error: cannot remove {item} from {name}'s inventory as they have none in the first place. \n")
        self.txt_file.write("\n\n")