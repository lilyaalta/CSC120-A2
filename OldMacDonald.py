class OldMacDonald:
    animal: str
    sound: str

    def __init__(self, a:str, s:str):
        self.animal = a 
        self.sound = s
    
    def sing(self):
        print("Old MaDonald had a farm, E-I-E-I-O")
        print("And on that farm he had a", self.animal, "E-I-E-I-O")
        print("With a", self.sound, self.sound, "here")


#Old MaDonald had a farm, E-I-E-I-O
#And on that famr he had <animal>, E-I-E-I-O
#with a <sound> <sound> here
# with a <sound> <sound> here


# An vs. a before animal name
        
def main():
    myVerse = OldMacDonald("goat", "meh")
    myVerse.sing()

main()