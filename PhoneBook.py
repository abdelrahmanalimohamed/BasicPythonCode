#Simple phonebook contacts just for learning 

class Contacts:
    def __init__(self, name, address, phonenumber):
        self.name = name
        self.address = address
        self.phonenumber = phonenumber


print("Welcome to phonebook directory :")

phoneBook = [Contacts("FirstName", "Cairo", 123456), Contacts("SecondName", "italy", 789),
             Contacts("ThirdName", "spain", 101010)]

# search technique
searchkeyword = input("Enter the name you want to search for : ")

x = True

for item in range(len(phoneBook)):
    if searchkeyword == phoneBook[item].name:
        x = True
        print(phoneBook[item].address, phoneBook[item].phonenumber)
        break
    else:
        x = False

if not x:
    print("No item found")

# Delete Technique
deletekeyword = input("Enter the item you want to delete : ")

for item in range(len(phoneBook)):
    if deletekeyword == phoneBook[item].name:
        x = True
        del (phoneBook[item])
        break
    else:
        x = False

if not x:
    print("No item found")
else:
    print(len(phoneBook))

# Insert Technique

name = input("Enter the name you want to add : ")
address = input("Enter the address you want to add : ")
phonenumber = input("Enter the phone number you want to add  : ")

phoneBook.append(Contacts(name, address, phonenumber))

for item in phoneBook:
    print(item.name)

# Update Technique
updatekeyword = input("Enter the name you want to update  : ")
for item in range(len(phoneBook)):
    if updatekeyword == phoneBook[item].name:
        phoneBook[item].name = str(input("enter the new name"))
        break
    else:
        x = False

for item in phoneBook:
    print(item.name)
