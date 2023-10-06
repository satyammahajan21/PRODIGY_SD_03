class Contact:

  def __init__(self, name, phone_number, email_address):
    self.name = name
    self.phone_number = phone_number
    self.email_address = email_address

class ContactManager:

  def __init__(self):
    self.contacts = []

  def add_contact(self, contact):
    self.contacts.append(contact)

  def view_contacts(self):
    for contact in self.contacts:
      print(contact.name, contact.phone_number, contact.email_address)

  def edit_contact(self, name):
    contact = self.get_contact_by_name(name)
    if contact is not None:
      new_name = input("Enter the new name: ")
      new_phone_number = input("Enter the new phone number: ")
      new_email_address = input("Enter the new email address: ")

      contact.name = new_name
      contact.phone_number = new_phone_number
      contact.email_address = new_email_address

      print("Contact edited successfully!")
    else:
      print("Contact not found!")

  def delete_contact(self, name):
    contact = self.get_contact_by_name(name)
    if contact is not None:
      self.contacts.remove(contact)

      print("Contact deleted successfully!")
    else:
      print("Contact not found!")

  def get_contact_by_name(self, name):
    for contact in self.contacts:
      if contact.name == name:
        return contact

    return None

if __name__ == "__main__":
  contact_manager = ContactManager()

  while True:
    print("1. Add contact")
    print("2. View contacts")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
      name = input("Enter the contact name: ")
      phone_number = input("Enter the contact phone number: ")
      email_address = input("Enter the contact email address: ")

      contact = Contact(name, phone_number, email_address)
      contact_manager.add_contact(contact)

      print("Contact added successfully!")
    elif choice == 2:
      contact_manager.view_contacts()
    elif choice == 3:
      name = input("Enter the name of the contact to edit: ")

      contact_manager.edit_contact(name)
    elif choice == 4:
      name = input("Enter the name of the contact to delete: ")

      contact_manager.delete_contact(name)
    elif choice == 5:
      break
    else:
      print("Invalid choice!")


  print("Goodbye!")
