import os
from dotenv import load_dotenv
from data import Connect

from utils import WelcomeScreen, LoginScreen, UserInventory

load_dotenv();

HOST = os.getenv("HOST");
USERNAME = os.getenv("USER");
PASSWORD = os.getenv("PASSWORD");
DATABASE = os.getenv("DATABASE");

connection = Connect(HOST, USERNAME, PASSWORD, DATABASE)
connect = connection.Connection()
if not connect:
    print("Cannot connect/find the database")
    exit()
USERID = 0

WelcomeScreen(connect)
USERID = LoginScreen(connect)
UserInventory(connect, USERID)