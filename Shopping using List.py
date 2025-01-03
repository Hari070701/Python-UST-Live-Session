def view_items(self):
    for i in self.items:
        print("Name: ", i[0], " Price: ", i[1])

def add_item(self):
    item = input("Enter the item: ").lower()
    quant = int(input("Enter the quantity: "))
    self.orderlist.append([item, quant])

def update_item(self):
    item = input("Enter the item to be updated: ").lower()
    quant = int(input("Enter the quantity to be updated: "))
    for order in self.orderlist:
        if order[0] == item:
            order[1] = quant
            return

def del_item(self):
    item = input("Enter item to be deleted: ").lower()
    self.orderlist = [order for order in self.orderlist if order[0] != item]

def print_bill(self):
    for order in self.orderlist:
        for item in self.items:
            if item[0] == order[0]:
                print(order[0], order[1], item[1], order[1] * item[1])

def disp_bill(self):
    sum1 = 0
    print("Name", "Quantity", "Price", "Total")
    for order in self.orderlist:
        for item in self.items:
            if item[0] == order[0]:
                print(order[0], order[1], item[1], order[1] * item[1])
                sum1 += order[1] * item[1]
    print("Total amount: ", sum1)

class Shopping_Cart:
    def __init__(self):
        self.items = [["bread", 40], ["cookies", 60], ["butter", 80], ["cheese", 120], ["yogurt", 90]]
        self.orderlist = []

        print("What do you want to do?\nEnter 1 for Viewing the items\nEnter 2 for adding items to the cart\nEnter 3 for updating items in cart\nEnter 4 for deleting items from cart\nEnter 5 for printing bill")

        while True:
            ch = int(input("Enter the choice: "))
            if ch == 1:
                view_items(self)
            elif ch == 2:
                add_item(self)
            elif ch == 3:
                update_item(self)
            elif ch == 4:
                del_item(self)
            elif ch == 5:
                print_bill(self)
            else:
                disp_bill(self)
                exit()

c = Shopping_Cart()
