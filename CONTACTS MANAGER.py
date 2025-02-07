

def save_contact(name, number):
    contacts[name] = number

def menu():
    menu_text = """
----- Welcome To The Contact Folder -----
 1. Create A New Contact.
 2. Delete Existing Contact By Number Or Name.
 3. Update A Contact Info.
 4. Display All Contacts.
 5. Exit.
"""
    print(menu_text)
    return input("Enter Your Choice (The Number): ")

while True:
    choice = menu()
    
    if choice == "1":
        conName = input("Enter Contact Name: ")
        conNum = input("Enter Contact Number: ")
        if conName in contacts:
            print("❌ This contact already exists!")
        else:
            save_contact(conName, conNum)
            print(f"✅ Contact '{conName}' saved successfully!")

    elif choice == "2":
        print("""
 Delete Existing Contact:
  1. By Number.
  2. By Name.
""")
        theChoice = input("Enter Your Choice (The Number): ")

        if theChoice == "1":
            conNum = input("Enter Contact Number: ")
            # Find the key associated with this number
            conName = next((key for key, value in contacts.items() if value == conNum), None)
            if conName:
                contacts.pop(conName)
                print(f"✅ Contact '{conName}' with number {conNum} was successfully deleted.")
            else:
                print("❌ No contact found with this number.")

        elif theChoice == "2":
            conName = input("Enter Contact Name: ")
            if conName in contacts:
                conNum = contacts.pop(conName)
                print(f"✅ Contact '{conName}' with number {conNum} was successfully deleted.")
            else:
                print("❌ No contact found with this name.")

        else:
            print("❌ Invalid input. Please enter a valid option.")

    elif choice == "3":
        conNameOrNum = input("Enter Contact Name or Number (The Old One): ")
        newNum = input("Enter Contact Number (The New One): ")

        found = False
        for name, num in contacts.items():
            if conNameOrNum == name:
                contacts[name] = newNum
                found = True
                print(f"✅ Contact '{name}' updated successfully!")
                break
            elif conNameOrNum == num:
                contacts[name] = newNum
                found = True
                print(f"✅ Contact '{name}' updated successfully!")
                break

        if not found:
            print("❌ No matching contact found.")

    elif choice == "4":
        if not contacts:
            print("📭 Your contact list is empty.")
        else:
            print("📖 Contact List:")
            for name, number in contacts.items():
                print(f"📌 {name} : {number}")

    elif choice == "5":
        print("👋 Thank you! Exiting the program.")
        break

    else:
        print("❌ Invalid input. Please enter a valid option.")
