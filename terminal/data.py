import mysql.connector
# Class to handle MySQL Connection
class Connect:
    def __init__(self, Host, User, Password, Database): # Parameters for connection
        self.Host = Host;
        self.User = User;
        self.Password = Password;
        self.Database = Database;
    def Connection(self):
        # Trying to establish a connection if not error is thrown
        try:
            DB_Connection = mysql.connector.connect(host = self.Host, user = self.User, password = self.Password, database =  self.Database);
            if(DB_Connection.is_connected()):
                return DB_Connection;
        except:
            return False
        
# This function execute the sql queries based on the provided task which is basically crud operations
def EnterQuery(connection, todo, query, param=()):
    if connection:
        cursor = connection.cursor()
        try:
            match todo.lower():
                case 'readone': # Fetch a single record from the database
                    cursor.execute(query, param)
                    return cursor.fetchone()
                case 'readall': # Fetch all the records from the database
                    cursor.execute(query, param)
                    return cursor.fetchall()
                case 'create': # Insert data in the database
                    cursor.execute(query, param)
                    connection.commit() # Commiting changes
                    return True
                case 'delete': # Delete the data from the database
                    cursor.execute(query, param)
                    connection.commit() # Commiting changes
                    return True
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            cursor.close()
    return False # Retrun false if the connection is invalid
