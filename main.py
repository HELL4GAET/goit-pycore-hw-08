import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}  # Словарь для хранения контактов

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

    def find_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def display_contacts(self):
        for name, phone in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")

    # Методы для сохранения и загрузки данных
    def save_to_file(self, filename="addressbook.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.contacts, f)

    def load_from_file(self, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as f:
                self.contacts = pickle.load(f)
        except FileNotFoundError:
            self.contacts = {}
            print(f"File {filename} not found. A new address book will be created.")
        except Exception as e:
            print(f"An error occurred while loading the file: {e}")
            self.contacts = {}

# Главная функция, которая обеспечивает работу программы
def main():
    address_book = AddressBook()  # Создаем экземпляр класса AddressBook
    address_book.load_from_file()

    try:
        while True:
            print("\n1. Add Contact")
            print("2. Remove Contact")
            print("3. Find Contact")
            print("4. Display All Contacts")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                name = input("Enter name: ")
                phone = input("Enter phone number: ")
                address_book.add_contact(name, phone)
            elif choice == "2":
                name = input("Enter name to remove: ")
                address_book.remove_contact(name)
            elif choice == "3":
                name = input("Enter name to find: ")
                print(address_book.find_contact(name))
            elif choice == "4":
                address_book.display_contacts()
            elif choice == "5":
                address_book.save_to_file()
                print("Address book saved. Exiting...")
                break
            else:
                print("Invalid option. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Saving address book before exiting...")
        address_book.save_to_file()
        print("Address book saved. Exiting...")

if __name__ == "__main__":
    main()
