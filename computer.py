from typing import Optional
class Computer:
    
    # What attributes will it need?
    #item_id : int = ""
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = ""
    memory: int = ""
    operating_system: str = ""
    year_made: int = ""
    price: int = ""

    # How will you set up your constructor?
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):

        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        #self.item_id = item_id
        
    # Remember: in python, all constructors have the same name (__init__)
    # What methods will you need?
    def printDetails(self):
        print("--------DETAILS BELOW--------")
        #print("Item ID:", self.item_id)
        print("Description:", self.description)
        print("Processor Type:", self.processor_type)
        print("Hard Drive Capacity:", self.hard_drive_capacity)
        print("Memory:", self.memory)
        print("Operating System:", self.operating_system)
        print("Year made:", self.year_made)
        print("Price:", self.price)
    
    def updatePrice(self, newPrice: float):
        #possibly add contidional here to sort out bad computers -- not sure if this is necessary in OO program as opposed to procedural program
        self.price = newPrice
        print("Price has been updated to", self.price)

    def refurbish(self, newOS: Optional[str] = None):
        if(self.year_made < 2000):
            self.price = 0 #too old to sell
        elif(self.year_made < 2012):
            self.price = 250 #discounted bc old
        elif(self.year_made < 2018):
            self.price = 550 #less discounted but still old
        else:
            self.price = 1000 #no discount

        if(newOS is not None):
            self.operating_system = newOS #install new operating system
        print("Computer has been updated to", self.operating_system, "operating system, and it now costs", self.price, "dollars.")


def main():
    my_computer = Computer(
         "Mac Pro (Late 2013)",
         "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    my_computer.printDetails()
    my_computer.updatePrice(2000)
    my_computer.printDetails()
    my_computer.refurbish("Windows")
    my_computer.printDetails()
# Only call main() if I am running this program directly
if __name__ == "__main__":
    main()