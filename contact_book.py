def contactBookName():
    nameList = []
    while True:
        name = input("Enter a name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        nameList.append(name)
    return nameList

def contactBookPhone():
    phoneList = []
    while True:
        phone = input("Enter a phone number (or type 'done' to finish): ")
        if phone.lower() == 'done':
            break
        phoneList.append(phone)
    return phoneList

def contactBookCity():
    cityList = []
    while True:
        city = input("Enter a city (or type 'done' to finish): ")
        if city.lower() == 'done':
            break
        cityList.append(city)
    return cityList


contact_functions = [contactBookName, contactBookPhone, contactBookCity]


contacts = [func() for func in contact_functions]


max_length = max(len(contact) for contact in contacts)
for contact in contacts:
    contact.extend(["N/A"] * (max_length - len(contact)))


headers = ["NAME", "PHONE_NUMBER", "CITY"]
print("CONTACT BOOK: ")

print("-" * 60)
print(f"{headers[0]:<20}{headers[1]:<20}{headers[2]:<20}")
print("-" * 60)


for i in range(max_length):
    print(f"{contacts[0][i]:<20}{contacts[1][i]:<20}{contacts[2][i]:<20}")
