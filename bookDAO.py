# Script to create the data access object and interact with the database

# Import libaries and config file
import mysql.connector 
import dbconfig as cfg


# Add your own details here to connect to the database and get a cursor
class BookDAO:
    connection=''
    cursor=''
    host = '127.0.0.1'
    user = 'root'
    password = 'root'
    database = 'datarep3'
        
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']


    # Function to connect to the database
    def getcursor(self): 
        self.connection = mysql.connector.connect(
        host=       self.host,
        user=       self.user,
        password=   self.password,
        database=   self.database,
        )

        self.cursor = self.connection.cursor()
        return self.cursor


    # Function to close connection
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

  
    # Function to register a user
    def register(self, account):
        print(account)     
        cursor = self.getcursor()

        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
        values = [
            account["username"], 
            account["email"],
            account["password"]
        ]
    
        cursor.execute(sql,values)
        self.connection.commit()
        print ("user registered")
        return 1  
        
          
   
    # Function to log a user in
    def login(self, account):
        cursor = self.getcursor()
        sql = "SELECT username, password FROM users WHERE username = %s"
        values = [account["username"]]      
        cursor.execute(sql,values)
        data = cursor.fetchone()
        print(data)
        
        # If no username or password
        if data[0] == "" and data[1]=="":
            print("User not found")
            return 0
        else: # Checking the password matches the username
            if account["password"] == data[1]:
                print("Logged in")
                return 1
            else:
                print("Password is incorrect")
                return 0
        #self.closeAll()            
        


    # Function to return user for given id
    def findUserByID(self, userId):
       cursor = self.getcursor()
       sql = 'select * from users where user_id = %s'
       values = [userId]
       cursor.execute(sql, values)
       result = cursor.fetchone()
       user = self.convertUserToDict(result)
       cursor.close()
       return user


    
    # Function to get all users
    def getAllUsers(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM users"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = [] # Empty array to store the data from the dict
        
        for r in result:
            result_as_dict = self.userDict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr


    
    # Function to convert Users response to a dictionary
    def userDict(self,result):
        colnames = ["id","username","email", "password"]
        users= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                users[col_name] = value
        return users

 # Function to create a student account
    def createStudent(self, students):
        print(students) 
        cursor = self.getcursor()

        sql = "INSERT INTO students (studentID, firstname, lastname, dept) VALUES (%s,%s,%s,%s)"
        values = [
            students["studentID"],
            students["firstname"],
            students["lastname"],
            students["dept"],
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid # Next id
        

    # Function to create a book
    def createBook(self, book):
        print(book) 
        cursor = self.getcursor()

        sql = "INSERT INTO book(deptID, author, title) VALUES (%s,%s,%s)"
        values = [
            book["deptID"],
            book["author"],
            book["title"],
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return cursor.lastrowid # Next id
      
    #####################
        # Function to convert Book responses to a dictionary
    def convert_to_dict(self,result):
        colnames = ["deptID","author","title"]
        book= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                book[col_name] = value
        return book

    # Function to convert Student response to a dictionary
    def convert_to_dict_student(self,result):
        colnames = ["studentID","firstname","lastname","dept"]
        students= {}

        if result:
            for c, col_name in enumerate(colnames):
                value = result[c]
                students[col_name] = value
        return students

    ######################
     # Function to get all books
    def getAllBook(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM book"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = [] # Empty array to store the data from the dict
        
        for r in result:
            result_as_dict = self.convert_to_dict(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr
    
         # Function to get all students
    def getAllStudents(self):
        cursor = self.getcursor()     
        sql = "SELECT * FROM students"
        cursor.execute(sql)
        result = cursor.fetchall()
        return_arr = [] # Empty array to store the data from the dict
        
        for r in result:
            result_as_dict = self.convert_to_dict_student(r)
            return_arr.append(result_as_dict)     
        self.closeAll()
        return return_arr
       
       ################################   
    # Function to get a book by id
    def getBookById(self,deptID):
        cursor = self.getcursor()
        
        sql = "SELECT * FROM book WHERE deptID = %s"
        values = [deptID]

        cursor.execute(sql,values)
        result = cursor.fetchone()
        #self.closeAll()
        book = self.convert_to_dict(result)
        self.close()
        return book

        
      # Function to get a student by department id
    def getStudentByID(self,dept):
        cursor = self.getcursor()
        
        sql = "SELECT * FROM students WHERE dept = %s"
        values = [dept]

        cursor.execute(sql,values)
        result = cursor.fetchone()
        students = self.convert_to_dict_student(result)
        self.close()
        return students
    ####################################################
    
    # Function to get book by author
    def getBookByAuthor(self, author):
      cursor = self.getcursor()

      sql = "SELECT * FROM book WHERE author = %s"
      values = [author]

      cursor.execute(sql, values)
      results = cursor.fetchall()
      allBook = []

      for result in results:
          resultDict = self.convert_to_dict(result)
          allBook.append(resultDict)     
      self.close()
      return allBook

    # Function to update book information based on department ID
    def updateBook(self, book):
        cursor = self.getcursor() 
        sql = "UPDATE book SET author = %s, title = %s WHERE deptID = %s"
        values = [
            book['author'], 
            book['title'],
            book['deptID']
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.close()
        return book
        
    # Function to update student information based on student ID
    def updateStudents(self, students):
        cursor = self.getcursor() 
        sql = "UPDATE students SET firstname = %s, lastname = %s, dept = %s WHERE studentID = %s"
        values = [
            students['firstname'], 
            students['lastname'],
            students['dept'],
            students['studentID']
        ]  

        cursor.execute(sql, values)
        self.connection.commit()
        self.close()
        return students
        

    
    # Function to delete a book based on department id
    def deleteBook (self, deptID):
        cursor = self.getcursor()

        sql = "DELETE FROM book WHERE deptID = %s"
        values = [deptID]

        cursor.execute(sql,values)
        self.connection.commit()
        self.close()
        return {}
    
    # Function to delete a student based on student id
    def deleteStudents (self, studentID):
        cursor = self.getcursor()

        sql = "DELETE FROM students WHERE studentID = %s"
        values = [studentID]

        cursor.execute(sql,values)
        self.connection.commit()
        self.close()
        return {}

    # Function to delete a users based on login
    def deleteUser (self, username):
        cursor = self.getcursor()

        sql = "DELETE FROM users WHERE username = %s"
        values = [username]

        cursor.execute(sql,values)
        self.connection.commit()
        self.close()
        return {}
    
# Data Access Object   
bookDAO = BookDAO()

if __name__ == "__main__":
    print('running')

 
    ###### TEST DATA ######
    
    ###### USERS ######
   # user = {"username":"odonovanm", "email":"g00411@atu.ie", "password": "pwd"}

    #bookDAO.register(user)
   
    ###### BOOK ######
    #data = {"deptID":"221", "author":"Paul Deitel","title":"Intro to Python"}
    #bookDAO.createBook(data)
  
   ###### STUDENT ######
    #data = {"studentID":"00411","firstname":"Megan","lastname":"Donovan","dept":"221"}
    #bookDAO.createStudent(data)
  

