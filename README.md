# Overview

The purpose of this software is to enhance my skills in database integration, secure user management, and modular programming by building a practical and efficient application.

This software connects to a SQL relational database to handle user registration, login with hashed passwords, and inventory management. Users can perform CRUD operations such as adding, viewing, and deleting inventory items.

To run this program please follow the instruction in Readme file inside the terminal folder.

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database

We are using MySQL Server for our RDBMS

We have created three tables in our database which are: `User`, `Item`, and `Category`. So one user can have more than one items and that items is belong to one of the categories.

# Development Environment
We primarily used Git version control, MySQL Server, MySQL Workbench, and Visual Studio Code.

The primary programming language that has been used in the project is Python and SQL. We also added additional packages like `python-dotenv`, `mysql-connector-python`, `tabulate`, `pwinput`.

# Useful Websites

{Make a list of websites that you found helpful in this project}

- [MySQL Documentation](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
- [Python Documentation](https://docs.python.org/3/tutorial/classes.html)

# Future Work
- Needs to add Update function to update the item quantity
- Graphical User Interface