print('==============================================================')

list_familyMember = [] # This list holds all dictionary of family memebrs


def displayNameByAge():
    userGivenAge = input('Enter age to search family member :: ')
    if userGivenAge.isdigit():
        flag = 0
        for familyMember in list_familyMember:
            if familyMember['age'] == userGivenAge:
                print(f"""
                    !!!!!   Data found   !!!!!
                    name ==> {familyMember['name']}
                    age ==> {familyMember['age']}
                """)
                flag = 1
        if flag == 0:
            print(f"""
                !!!!!   SORRY   !!!!!  NO member found with age {userGivenAge}
            """)
    else:
        print('Wrong age entry. Exiting....')


def displayDataSet():
    print('Here is the total data set displayed as table')
    index = 0
    for familyMember in list_familyMember:
        index += 1
        print(f"""
            {index})name= '{familyMember["name"]}'  age= '{familyMember["age"]}'
        """)


def receiveAndStoreData():
    name = age = ''
    name = input('Enter name of the family member: ')
    age = input('Enter age of family member: ')
    if age.isdigit() == False:
        print('Wrong age entry. Exiting....')
        return False
    if not(name.isalpha() == True and name.isdigit() == False):
        print('Wrong name entry. Exiting....')
        return False
    dictionary_familyMember = {
        'name': name,
        'age': age
    }
    list_familyMember.append(dictionary_familyMember)


def activateMenu():
    print("""
        1. Press 1+Enter to enter data
        2. Press 2+Enter to display data set
        3. Press 3+Enter to display name by age
        4. Press 4+Enter to exit
        """)
    userInput = input('Waiting for user to input:::  ')
    if userInput == '4':
        print('Ok! Tata! GoodBye!')
        return False
    elif userInput == '1':
        receiveAndStoreData()
        return True
    elif userInput == '2':
        displayDataSet()
        return True
    elif userInput == '3':
        displayNameByAge()
        return True
    else:
        print('WRONG input! Exiting program')
        return False


def main():
    while True:
        if activateMenu() == False:
            break

main()
print('==============================================================')
