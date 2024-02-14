class Computer: # identifying the variables
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

 # initializing 
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def stringifycomputer(self):
        return f"{self.description}, {self.processor_type}, {self.hard_drive_capacity}, {self.memory}, {self.operating_system}, {self.year_made}, {self.price}"
    
    def updateprice(self, price: int):
        self.price = price

    def updateos(self, operating_system: str):
        self.operating_system = operating_system

# You'll remove this when you fill out your constructor
def main():
    computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    print(computer.description)

main()
    # What methods will you need?