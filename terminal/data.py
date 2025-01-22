import mysql.connector

class Connect:
    def __init__(self, Host, User, Password, Database):
        self.Host = Host;
        self.User = User;
        self.Password = Password;
        self.Database = Database;
    def Connection(self):
        DB_Connection = mysql.connector.connect(host = self.Host, user = self.User, password = self.Password, database =  self.Database);
        if(DB_Connection.is_connected()):
            return DB_Connection;
        else: return False;

def EnterQuery(connection, todo, query, param=()):
    if connection:
        cursor = connection.cursor()
        try:
            match todo.lower():
                case 'readone':
                    cursor.execute(query, param)
                    return cursor.fetchone()
                case 'readall':
                    cursor.execute(query, param)
                    return cursor.fetchall()
                case 'create':
                    cursor.execute(query, param)
                    connection.commit()
                    return True
                case 'delete':
                    cursor.execute(query, param)
                    connection.commit()
                    return True
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            return None
        finally:
            cursor.close()
    return False
