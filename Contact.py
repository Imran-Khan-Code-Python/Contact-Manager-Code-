def add_contact(contacts):
    while True:
        name = input("Enter name: ").strip()
        if not name.replace(" ", "").isalpha():
            print("Invalid name. Only letters are allowed.")
            continue
        if name in contacts:
            print("Contact already exists.")
            return
        break

    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if not phone.isdigit():
            print("Invalid phone number. Only digits are allowed.")
            continue
        if len(phone) != 10:
            print("Invalid phone number. It must be exactly 10 digits.")
            continue
        break

    contacts[name] = {"phone": phone}
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    for name, info in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['phone']}")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def main():
    contacts = {}

    while True:
        print("\n=== Contact Manager ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
