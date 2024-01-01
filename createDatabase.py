# Script to create the database and tables

# Import libaries and config file
import mysql.connector
import dbconfig as cfg


# Add your own details here to connect to the database and get a cursor
class DataRepDAO:
    connection= ""
    cursor = ""
    host = "127.0.0.1"
    user = "root"
    password = "root"
    database = "datarep3"
    

    # Details from my config file
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    # Connecting to database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor


    # Close connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         

     # Function to create the database   
    def createdatase(self):
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password   
        )
    
        self.cursor = self.connection.cursor()
        sql= "CREATE DATABASE IF NOT EXISTS " + self.database
        self.cursor.execute(sql)
        self.connection.commit()
        print('database created')
        self.closeAll()
        

    
    # Create the users table
    def createUsersTable(self):
        cursor = self.getcursor()

        sql = '''CREATE TABLE users (user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
            username VARCHAR(200) NOT NULL UNIQUE, 
            email VARCHAR(150) NOT NULL UNIQUE,
            password VARCHAR(150) NOT NULL)'''

        cursor.execute(sql)
        self.connection.commit()
        print('Users Table Created')
        self.closeAll()


    
    # Create the Book Check Out table
    def createBookTable(self):
        cursor = self.getcursor()

        sql = '''CREATE TABLE book (deptID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                author VARCHAR(200) NOT NULL, 
                title VARCHAR(200))'''

        cursor.execute(sql)
        self.connection.commit()
        print('Book CheckOut Table Created')
        self.closeAll()

    # Create the Student Account table
    def createStudentTable(self):
        cursor = self.getcursor()

        sql = '''CREATE TABLE students (studentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                firstname VARCHAR(200) NOT NULL, 
                lastname VARCHAR(200) NOT NULL,
                dept INT NOT NULL, FOREIGN KEY(dept) REFERENCES book(deptID))'''

        cursor.execute(sql)
        self.connection.commit()
        print('Student Account Table Created')
        self.closeAll()

# data access object
datarepDAO = DataRepDAO()

if __name__ == "__main__":

    #Creating database
    datarepDAO.createdatase()

    # Create database tables
    datarepDAO.createUsersTable()
    datarepDAO.createBookTable()
    datarepDAO.createStudentTable()

    #print("running :)")