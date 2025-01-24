# main.py
## Inventory Management System

## Overview
This script connects to a database and runs an inventory management system, including a welcome screen, login, and user inventory functions.

## Steps:
1. **Load Environment Variables**: Uses `dotenv` to load database credentials from a `.env` file.
2. **Database Connection**: Establishes a connection to the database using credentials from environment variables.
3. **Functions**: Sequentially calls the `WelcomeScreen`, `LoginScreen`, and `UserInventory` functions for the inventory management.

## Functions

`WelcomeScreen(connection)`
Displays the welcome screen of the inventory system.

**Parameters:**
- `connection`: Active database connection.

`LoginScreen(connection) -> int`
Handles user login and returns the `USERID` of the logged-in user.

**Parameters:**
- `connection`: Active database connection.

**Returns:**
- `USERID`: The unique identifier of the logged-in user.

`UserInventory(connection, user_id)`
Manages the user’s inventory by interacting with the database.

**Parameters:**
- `connection`: Active database connection.
- `user_id`: The ID of the logged-in user.

# data.py
## MySQL Connection Handler and Query Executor

This script provides a simple class and function to handle MySQL database connections and execute common CRUD operations. It is designed to make database interaction easier for small projects.

### Features

1. **`Connect` Class**:
   - **Purpose**: Establishes a connection to a MySQL database.
   - **Usage**: 
     - Instantiate the class with `Host`, `User`, `Password`, and `Database` parameters.
     - Call the `Connection` method to obtain a database connection object.
   - Returns:
     - A valid MySQL connection object if successful.
     - `False` if the connection fails.

2. **`EnterQuery` Function**:
   - **Purpose**: Executes SQL queries based on the specified task.
   - **Parameters**:
     - `connection`: A valid MySQL connection object.
     - `todo`: The type of task (`'readone'`, `'readall'`, `'create'`, or `'delete'`).
     - `query`: The SQL query to execute.
     - `param`: (Optional) Parameters for the query.
   - **Supported Tasks**:
     - `'readone'`: Fetches a single record.
     - `'readall'`: Fetches all records.
     - `'create'`: Inserts data into the database.
     - `'delete'`: Deletes data from the database.
   - Returns:
     - Query results for `'readone'` and `'readall'`.
     - `True` for successful `'create'` or `'delete'` operations.
     - `None` if an error occurs.
     - `False` if the connection is invalid.

# utils.py
# Inventory Management System

A lightweight script for managing users and inventory with MySQL.

## Features

### 1. **Welcome Screen**
- **Purpose**: Handles user registration.
- **Steps**:
  - Check username availability.
  - Validate and hash passwords.
  - Save new user info (username, hashed password, and company name) to the database.

### 2. **Login Screen**
- **Purpose**: Authenticates existing users.
- **Steps**:
  - Verify username exists.
  - Authenticate password (supports hashed passwords).
  - Returns the `USERID` for the session.

### 3. **User Inventory**
- **Purpose**: Manage inventory items.
- **Options**:
  1. **View Items**: Lists all items in a tabular format.
  2. **Add Items**: Add new items with price, quantity, and category.
  3. **Delete Items**: Remove items by `ItemId`.
  4. **Exit**: Ends the session.

## Dependencies
- `mysql.connector`: For database operations.
- `tabulate`: For table display.
- `pwinput`: For secure password input.
- `data` & `login`: Custom modules for query execution and password handling.

## Workflow
1. **Register**: Use `WelcomeScreen(connect)` for new users.
2. **Login**: Call `LoginScreen(connect)` for authentication.
3. **Manage Inventory**: Use `UserInventory(connect, USERID)` to manage items.

Simple and extensible for small projects.

# login.py
## Password Validation and Hashing

`hash_password(password: str) -> str`
Hashes the password using SHA-256.

**Parameters:**
- `password`: The password to hash.

**Returns:**  
- Hashed password as a string.

`validate_username_password(username: str, password: str, min_length=5, max_length=10) -> list`
Validates username and password.

**Parameters:**
- `username`, `password`: Credentials to validate.
- `min_length`, `max_length`: Password length constraints.

**Returns:**  
- List of error messages.

---

`validate_password(password: str, min_length=5, max_length=10) -> bool`
Validates password length and spaces.

**Parameters:**
- `password`: The password to validate.
- `min_length`, `max_length`: Password length constraints.

**Returns:**  
- `True` if valid, `False` otherwise.

# How to run
First to run this program we have to have a `.env` file which should have the following variables and the values that it is asking:-
```
HOST='localhost' # Do not change
USER='root' # Change if using different user
PASSWORD='mypassword' # Add the password for the user that is being used
DATABASE='inventory' # Do not change
```
After you have set this up simply install the following packages using PIP, these are the dependencies that our application relies on:
```
pip install mysql-connector-python
pip install python-dotenv
pip install tabulate
pip install pwinput
```
or run this command:-
`pip install -r requirements.txt`

Now since everything is setup make sure you have the database in your system, because this whole application runs only if the database exist.
