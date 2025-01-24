# main.py
This serves as the entry point for our program, where we combine all of the features we have developed into a single file. By including these functions in the main file, it is simple to implement the features, which will operate sequentially.
# data.py
This file is a critical component of the software since it contains a class that initiates a connection to the MySQL database and produces an error if the connection cannot be established. This file also contains functions that are developed based on CRUD operations and can be implemented without having to manually connect to each database. This class handles all connections and can handle queries that need to be added manually. 
# utils.py

# login.py

## How to run
First to run this program we have to have a `.env` file which should have the following variables and the values that it is asking:-
```
HOST='localhost' # Do not change
USER='root' # Change if using different user
PASSWORD='mypassword'
DATABASE='inventory' # Do not change
```
After you have set this up simply install the following packages using PIP:
```
pip install mysql-connector-python
pip install python-dotenv
pip install tabulate
```
Now since everything is setup make sure you have the database in your system, because this whole application runs only if the database exist.
