from computer import Computer

class ResaleShop:

    # What attributes will it need?
    #inventory: Dict[int, Dict] = {}
    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    def buy(self, computer: Computer):
        self.inventory.append(computer)
        print("Bought computer:", computer.description,"!")

    def sell(self, computer: Computer):
        if computer in self.inventory:
            self.inventory.remove(computer)
            print("Item",computer.description , "sold!")
        else:
            print("Error: computer not found. Please try again.")
    
    def printInventory(self):
        print("----------INVENTORY BELOW----------")
        print(self.inventory)

def main():
    my_computer = Computer(
         "Mac Pro (Late 2013)",
         "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    
    my_resaleShop = ResaleShop()
    
    my_resaleShop.buy(my_computer)
    my_resaleShop.printInventory()
    my_resaleShop.sell(my_computer)
    my_resaleShop.printInventory()

if __name__ == "__main__":
    main()


        

    # What methods will you need?