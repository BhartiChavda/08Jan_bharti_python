import datetime

# Initial Inventory
inventory = {
    "Paracetamol": {"price": 10.0, "stock": 100},
    "Crocin": {"price": 15.0, "stock": 50}
}

sales = []


# ------------------ FUNCTIONS ------------------ #

def add_medicine():
    try:
        name = input("Enter medicine name: ")
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))

        inventory[name] = {"price": price, "stock": stock}
        print(f"{name} added/updated successfully!\n")

    except ValueError:
        print("Invalid input! Please enter correct data.\n")


def view_inventory():
    print("\n------ Current Inventory ------")
    if not inventory:
        print("Inventory is empty.\n")
        return

    for name, details in inventory.items():
        print(f"Medicine: {name}")
        print(f"Price: ₹{details['price']}")
        print(f"Stock: {details['stock']}")
        print("-----------------------------")
    print()


def process_sale():
    try:
        customer = input("Enter customer name: ")
        medicine = input("Enter medicine name: ")

        if medicine not in inventory:
            print("Medicine not found!\n")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0!\n")
            return

        if inventory[medicine]["stock"] < quantity:
            print("Not enough stock available!\n")
            return

        total = inventory[medicine]["price"] * quantity
        inventory[medicine]["stock"] -= quantity
        date = datetime.date.today()

        sales.append({
            "customer": customer,
            "medicine": medicine,
            "quantity": quantity,
            "total": total,
            "date": date
        })

        print("\n------ BILL ------")
        print(f"Customer: {customer}")
        print(f"Medicine: {medicine}")
        print(f"Quantity: {quantity}")
        print(f"Total Amount: ₹{total}")
        print(f"Date: {date}")
        print("------------------\n")

    except ValueError:
        print("Invalid input! Please enter correct data.\n")


def update_stock():
    try:
        name = input("Enter medicine name to update: ")

        if name not in inventory:
            print("Medicine not found!\n")
            return

        stock = int(input("Enter new stock quantity: "))
        price = float(input("Enter new price: "))

        inventory[name]["stock"] = stock
        inventory[name]["price"] = price

        print("Medicine updated successfully!\n")

    except ValueError:
        print("Invalid input! Please enter correct data.\n")


# ------------------ MAIN MENU ------------------ #

def main():
    while True:
        print("====== MediTrack - QuickMed Pharmacy ======")
        print("1. Add Medicine")
        print("2. View Inventory")
        print("3. Process Sale")
        print("4. Update Stock")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_medicine()
        elif choice == "2":
            view_inventory()
        elif choice == "3":
            process_sale()
        elif choice == "4":
            update_stock()
        elif choice == "5":
            print("Thank you for using MediTrack!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# Run Program
main()