import os
from dotenv import load_dotenv
from data import Connect

from utils import WelcomeScreen, LoginScreen, UserInventory

load_dotenv();
# Retrieve database credentials from environment variables
HOST = os.getenv("HOST");
USERNAME = os.getenv("USER");
PASSWORD = os.getenv("PASSWORD");
DATABASE = os.getenv("DATABASE");

# Creats database connection using Connect class
connection = Connect(HOST, USERNAME, PASSWORD, DATABASE)
connect = connection.Connection()

# Checks if the connection is successful
if not connect:
    print("Cannot connect/find the database")
    exit()
USERID = 0

# Calling the functions squentially for the inventoy management system
WelcomeScreen(connect)
USERID = LoginScreen(connect)
UserInventory(connect, USERID)