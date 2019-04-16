from Dice import Dice
from Characters import Characters

def main():
    ########################
    ###Tetrahedron Roller###
    ########################
    dice = Dice(10000)

    ####################################
    ###Character Inventory Management###
    ####################################
    characters = Characters({})
    
    #Character Creation
    characters.add_character("Gandalf", {"food":5, "grapefruit":10, "green potions":7, "red potions":8, "spells of enchantment":10})
    characters.add_character("Frodo", {"food":0, "kiwi":5, "wands of confusion":7, "green potions":8})
    characters.add_character("Sauron", {"bat wings":5, "evil spells":10, "fire wands":5})
    characters.add_character("Bilbo", {"food":0, "kiwi":5, "wands of confusion":7, "green potions":8})

    #Adding Items
    characters.add_item("Gandalf", "food", 1)
    characters.add_item("Frodo", "green potions", 1)
    characters.add_item("Sauron", "evil spells", 1)

    # #Creating Items
    characters.add_item("Gandalf", "Shadowfax", 1)
    characters.add_item("Frodo", "Coat of Mithril Maille", 1)
    characters.add_item("Sauron", "Ring of Power", 1)

    #Removing Items
    characters.remove_item("Gandalf", "food", 7)
    characters.remove_item("Frodo", "food", 1)
    characters.remove_item("Sauron", "evil spells", 11)

    #Removing Nonexistant Items
    characters.remove_item("Gandalf", "Great Eagle", 1)
    characters.remove_item("Frodo", "Sting", 1)
    characters.remove_item("Sauron", "Nazgul", 100)


if __name__ == "__main__":
    main()





        