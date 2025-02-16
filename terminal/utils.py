from data import EnterQuery
from tabulate import tabulate
from login import hash_password, Validate_password
from pwinput import pwinput

# Welcome screen that handles user registration
def WelcomeScreen(connect):
    while True:
        print("Welcome to Inventory Management System: ")
        choice = input("Enter 1 if existing user: ")
        if(choice == "1"):
            break
        else:
            while True:
                Username = input("Please enter your username: ")
                result = EnterQuery(connect, 'readone', 'SELECT Username FROM user WHERE Username = %s',(Username,))
                if(result == Username):
                    print("Username Exist")
                    continue
                else:
                    break
            while True:
                while True:
                    Password = pwinput(prompt="Please enter a new password: ",mask="*")
                    passChecking = Validate_password(Password)
                    if passChecking:
                        break
                    else:
                        continue
                PasswordRe = pwinput(prompt="Please retype your password: ",mask="*")
                if(Password == PasswordRe):
                    break
                else:
                    continue
            CompanyName = input("Please enter the Company Name: ")
            # Insert the new user in the database
            EnterQuery(connect, 'create', 'INSERT INTO user(Username, Password, CompanyName) VALUES (%s, %s, %s)',(Username, hash_password(Password), CompanyName,))
            break
# Function for login process
def LoginScreen(connect):
    USERID = 0 # This variable is to create a temporary session for a user
    while True:
        while True: # This loop check the username if it exist if yes move to password
            username = input('Enter Username: ')
            result = EnterQuery(connect, 'readone', 'SELECT Username,Id FROM user WHERE Username = %s', (username,))
            if(result != None and result[0] == username):
                USERID = result[1]
                break
            else: 
                print("Username does not exist")
                continue
        while True: # This loop authenticate the user and let user in if the password matches which is comming from the database
            password = pwinput(prompt='Enter Password: ',mask="*")
            result = EnterQuery(connect, 'readone', 'SELECT Password FROM user WHERE Username = %s', (username,))
            if(result != None and (result[0] == password or result[0] == hash_password(password))):
                break
            else: 
                print("Password does not match")
                continue
        return USERID

# Function to manage user inventory
def UserInventory(connect, USERID):
    while True:
        todos = ['1. Show Items', '2. Add Item', '3. Delete Item', '4. Exit']
        for todo in todos:
            print(todo)
        prompt = input('Please Enter The Number of the Task: ')
        match int(prompt):
            case 1: # This case returns all the itesm available in their inventory
                result = EnterQuery(connect, 'readall', "SELECT I.Name, I.ItemId, I.Price, I.Quantity, CASE WHEN I.IsWeight > 0 THEN 'Yes' ELSE 'No' END AS Weight, CASE WHEN I.IsPerItem > 0 THEN 'Yes' ELSE 'No' END AS PerItem, C.Name FROM item I INNER JOIN category C ON I.CategoryId = C.Id  WHERE I.UserId = %s", (USERID,))
                print(tabulate([i for i in result] , headers=['Item Name', 'Item Id', 'Cost', 'Total Quantity','Per Lbs','Per Item', 'Category']),'\n')
            case 2: # This case let user to add the item to an inventory
                itemName = input('Please Enter the Item Name: ')
                itemId = input('Please Enter the Item Id: ')
                itemQuantity = input('Please Enter the Quantity: ')
                itemPrice = float(input('Please Enter the Price: '))
                while True:
                    itemWeight = int(input('Is item price according to weight (0 = False, 1 = True): '))
                    itemPerItem = int(input('Is item price according to per item (0 = False, 1 = True): '))
                    if (itemWeight == 0 and itemPerItem == 0) or (itemWeight == 1 and itemPerItem == 1):
                        print('Item must be either priced based on Per Item or Weight')
                        continue
                    else:
                        break
                categories = EnterQuery(connect, 'readall', 'SELECT Id, Name FROM category')
                for category in categories:
                    print(f'{category[0]}.  {category[1]}')
                itemCategory = int(input('Which category item belongs to: '))
                EnterQuery(connect, 'create', 'INSERT INTO item(ItemId, Name, Quantity, Price, IsWeight, IsPerItem, UserId, CategoryId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',(itemId, itemName, itemQuantity, itemPrice, itemWeight, itemPerItem, USERID, itemCategory,))
            case 3: # This case let user delete the item based on the ItemId that is created by the user
                itemId = input('Please Enter the Item that needes to be remove: ')
                EnterQuery(connect, 'delete', 'DELETE FROM item WHERE ItemId = %s AND UserId = %s',(itemId, USERID))
            case 4: # This case is to exit the inventory
                break
            case _: # Default case for wrong input
                print("Please choose the correct option")