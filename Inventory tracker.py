import time

Inventory = {}  # all of the info

def Menu():
    Menu1 = """
Menu:
1. Add a new item
2. Update item quantity
3. Calculate total inventory value
4. Display all items
5. Quit """
    print(Menu1)
    return input("Enter The Number of Your Choice:")

choice = Menu()

while True:
    if choice == "5" or choice == "5.":
        print("Thank You...")
        time.sleep(2)
        break
    elif choice == "1" or choice == "1.":
        print("You Will Be Going in The Process of Adding A New Item Into The Inventory...")
        time.sleep(3)
        print("Loading...")
        time.sleep(1)

        Item_Name = input("Enter Item's Name: ").strip().lower()
        if Item_Name == "":
            print("Invalid Input. Please enter a valid name...")
            time.sleep(3)
            continue
        
        try:
            Item_Price = float(input("Enter Item's Price: "))
        except ValueError:
            print("Invalid Input. Please enter a valid number for the price...")
            time.sleep(3)
            continue

        try:
            Item_Quantity = int(input("Enter Item's Quantity: "))
        except ValueError:
            print("Invalid Input. Please enter a valid number for the quantity...")
            time.sleep(3)
            continue

        Inventory[Item_Name] = (Item_Price, Item_Quantity)
        print("Item Stored Successfully...")
        time.sleep(2)

    elif choice == "2" or choice == "2.":
        print("You Will Be Going in The Process of Updating The Quantity of An Item in the Inventory...")
        time.sleep(4)
        print("Loading...")
        time.sleep(1)

        Item_Name = input("Enter Item's Name:").strip().lower()
        if Item_Name == "":
            print("Invalid Input. Please enter a valid name...")
            time.sleep(3)
            continue

        if Item_Name in Inventory.keys():
            try:
                Item_Quantity = int(input("Enter The New Quantity:").strip())
            except ValueError:
                print("Invalid Input. Please enter a valid number for the quantity...")
                time.sleep(3)
                continue

            Quantity_value = list(Inventory[Item_Name])
            Quantity_value[1] = Item_Quantity
            Inventory[Item_Name] = tuple(Quantity_value)
            print("Quantity Changed Successfully...")
            time.sleep(3)
        else:
            print(f"Item \"{Item_Name}\" Is Not In The Inventory, Try Again...")
            time.sleep(3)
            continue

    elif choice == "3" or choice == "3.":
        if not Inventory:
            print("Sorry, But The Inventory Is Empty...")
            time.sleep(3)
        else:
            total_value = sum(price * quantity for price, quantity in Inventory.values())
            print(f"The Overall Value Of The Items In The Inventory Is {total_value:.2f}")
            time.sleep(3)

    elif choice == "4" or choice == "4.":
        if not Inventory:
            print("The Inventory is Empty")
            time.sleep(2.5)
        else:
            print("The Items In The Inventory Are:")
            for item, details in Inventory.items():
                print(f"{item.title()}: Price = {details[0]}, Quantity = {details[1]}")
            time.sleep(3)

    else:
        print("Invalid Choice! Please try again.")
        time.sleep(2)

    choice = Menu()
