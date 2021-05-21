#import
import random
import faker
from faker import Faker


faker = Faker()

#class
class BaseContact:

    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email


    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}")

    @property
    def label_length(self) -> int:
        return len(self.name) + len(self.last_name)+1

    def __str__(self):
        return f'{self.name}, {self.last_name}, {self.email}'
    def __repr__(self):
        return f' Full name: {self.name} {self.last_name}, phone:  {self.phone} and @: {self.email}'

class BusinessContact(BaseContact):

    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contact(self):
        print(f"Wybieram numer {self.business_phone} i dzwonię do {self.name} {self.last_name}")


    @property
    def label_length(self) -> int:
        return len(self.name) + len(self.last_name)

    def __str__(self):
        return f'{self.name}, {self.last_name}, {self.email}'
    def __repr__(self):
        return f' Full name: {self.name} {self.last_name}, phone:  {self.phone} and @: {self.email}; business details: position - {self.position} in {self.company}, business phone: {self.business_phone}'

# function (2 functions)

#first - "create function"
def create_contacts1(contact_type, n) -> object:
    if contact_type == 'Base':
        contacts_list1 = [BaseContact(name=faker.name(), last_name=faker.last_name(), phone=faker.country_calling_code() + " " + faker.phone_number(), email=faker.email()) for number in range(n)]
        print(contacts_list1)
    elif contact_type == 'Business':
        contacts_list1 = [BusinessContact(name=faker.name(), last_name=faker.last_name(), phone=faker.country_calling_code() + " " + faker.phone_number(), email=faker.email(), position=faker.job(), company=faker.company(), business_phone = faker.phone_number()) for number in range(n)]
        print(contacts_list1)
#check
create_contacts1('Business', 3)


#second -"create function"
def create_contacts2(contact_type, number):
    contact_list2 = []
    if contact_type == 'Base':
        for contact in range(number):
            contact = BaseContact(
                name = faker.name(),
                last_name = faker.last_name(),
                phone =faker.country_calling_code() + " " + faker.phone_number(),
                email= faker.email()
            )
            contact_list2.append(contact)
    elif contact_type == 'Business':
        for contact in range(number):
            contact = BusinessContact(
                name = faker.name(),
                last_name = faker.last_name(),
                phone = faker.random_int(100000000, 999999999),
                email = faker.email(),
                company = faker.company(),
                position = faker.job(),
                business_phone = faker.country_calling_code() + " " + faker.phone_number(),
            )
            contact_list2.append(contact)
    else:
        raise ValueError(
            f"Business Card name: {business_card} "
            f"is neither 'BaseContact' nor 'BusinessContact'")
    return contact_list2
#check
data = create_contacts2('Business', 1)
print(data)

# label length  & contact function check (but only "create_contacts2" is working properly!)
if __name__ == "__main__":
    contacts = []
    contacts += create_contacts2('Base', 2)
    contacts += create_contacts2('Business', 3)

    random.shuffle(contacts)

    for contact in contacts:

        contact.contact()
        print("(Label length: " + str(contact.label_length) + ")")