
contact_book = {} # Dictionary to store contact details

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    contact_book[name] = {"Phone": phone, "Email": email}
    print("Contact added successfully!")

def search_contact():
    print("\n--- Search Contact ---")
    name = input("Enter Name to search: ")
    if name in contact_book:
        print("Contact Found:")
        print("Name  :", name)
        print("Phone :", contact_book[name]["Phone"])
        print("Email :", contact_book[name]["Email"])
    else:
        print("Contact not found.")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter Name to update: ")
    if name in contact_book:
        phone = input("Enter new Phone Number: ")
        email = input("Enter new Email: ")

        contact_book[name]["Phone"] = phone
        contact_book[name]["Email"] = email
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter Name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def display_all_contacts():
    print("\n--- All Contacts ---")
    if len(contact_book) == 0:
        print("No contacts available.")
    else:
        for name, details in contact_book.items():
            print("Name:", name, "| Phone:", details["Phone"], "| Email:", details["Email"])

def main():
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            print("Thank you for using Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            exit()

if __name__ == "__main__":
    main()