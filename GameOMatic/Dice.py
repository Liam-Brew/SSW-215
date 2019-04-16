import random

class Dice:
    """Representation of a 12-sided dice (dodecahedron)."""
    def __init__(self, rolls): 
        """Instantiates the number of rolls from the class' input."""
        self.rolls = rolls
        self.results = []
        self.count = dict()
        self.txt_file = open("Result.txt", "w")
        self.roll()
        self.analysis()
        self.print()
        
    def roll(self, min_dice=1, max_dice=12):
        """Rolls the dice the required number of times."""
        for i in range(0, self.rolls):
            self.results.append(random.randint(min_dice, max_dice))

    def analysis(self):
        """Counts the number of each roll present in the results."""
        for i in self.results:
            self.count[i] = self.count.get(i, 0) + 1
            self.count[i][j] = (self.count[i]/10000) * 100

    def print(self):
        """Prints the results of the rolls into an output file."""
        self.txt_file.write(f"Number of instances of each roll: {self.count} \n\n" )
        self.txt_file.write(str(self.results) + "\n")
        print("Rolls saved!")
        self.txt_file.close()