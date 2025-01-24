# main.py
# data.py
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
