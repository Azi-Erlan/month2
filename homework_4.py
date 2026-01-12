class Contact:
    def __init__(self, name, phone_number, contact_id):
        self.name = name
        self.phone_number = phone_number
        self.id = contact_id


    @classmethod
    def validate_phone_number(cls, phone_number):
        return(
                isinstance(phone_number, str)
                and phone_number.isdigit()
                and len(phone_number) == 10)

class ContactList:
    all_contacts = []
    last_id = 0

    @classmethod
    def add_contact (cls, name, phone_number):
        if not Contact.validate_phone_number(phone_number):
            raise ValueError("Неверный номер телефона!!!")

        cls.last_id += 1
        contact = Contact(name, phone_number, cls.last_id)
        cls.all_contacts.append(contact)

    @classmethod
    def show_contact(cls):
        print('Список контактов:')
        for contact in cls.all_contacts:
            print(contact.name, contact.phone_number, contact.id)


ContactList.add_contact("Шарипов Санжар", "0555123456")
ContactList.add_contact("Джумашева Айжан", "0700123456")
# ContactList.add_contact("Сапар", "+996777123456")   # вариант неверного ввода

ContactList.show_contact()

