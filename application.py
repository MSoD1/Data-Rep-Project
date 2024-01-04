# Import libaries, database config file and bookDAO
from flask import Flask, jsonify, abort, request, session
from bookDAO import bookDAO
import dbconfig 

   

# Creating the Flask and setting secret key for session
app = Flask(__name__, static_url_path='', static_folder='static_pages')
app.config['SECRET_KEY'] = 'secret'


# ############################################################################


# Homepage route
@app.route('/')
def index():
    if not 'username' in session:
        return app.send_static_file('/login.html')
    return app.send_static_file('/index.html')



# Login 
@app.route("/login", methods = ["POST"])
def login():

    if request.method == "POST":
        account = {
            "username":request.json["username"],
            "password":request.json["password"]       
        }

    session['username'] = account["username"]

    return jsonify(bookDAO.login(account))



# Logout 
@app.route("/logout", methods = ["POST"])
def logout():
    session.pop("username", None)

    return app.send_static_file('index.html')
 


# Register a new user
# # curl -i -H "Content-Type:application/json" -X POST -d "{\"username\":\"odonovanm\",\"email":\"g00411@atu.com\",\"password":pwd}"
# http://127.0.0.1:5000/register
@app.route('/register', methods = ["POST"])
def register():

    account = {
        "username":request.json["username"],
        "email":request.json["email"],
        "password":request.json["password"]
    }

    return jsonify(bookDAO.register(account))
    


# Get all users 
# curl "http://127.0.0.1:5000/users"
@app.route("/users", methods=["GET"])
def getAllUsers():
    return jsonify(bookDAO.getAllUsers())



# Get all book 
# curl "http://127.0.0.1:5000/book"
@app.route("/book", methods=["GET"])
def getAllBook():
    return jsonify(bookDAO.getAllBook())

# Get all students 
# curl "http://127.0.0.1:5000/students"
@app.route("/students", methods=["GET"])
def getAllStudents():
    return jsonify(bookDAO.getAllStudents())

# Get all users 
# curl "http://127.0.0.1:5000/users"
@app.route("/users/username", methods=["GET"])
def getUserByName():
    return jsonify(bookDAO.getUserByName())



# Find book by bookID 
# curl "http://127.0.0.1:5000/book/221"
@app.route("/book/<int:bookID>")
def getBookById(bookID):
    current_book = bookDAO.getBookById(bookID)
    print(current_book)
    return jsonify(current_book)

# Find student by bookid 
# curl "http://127.0.0.1:5000/student/221"
@app.route("/students/<int:bookid>")
def getStudentByID(bookid):
    current_book = bookDAO.getStudentByID(bookid)
    print(current_book)
    return jsonify(current_book)




# Create a book
# curl -i -H "Content-Type:application/json" -X POST -d "{\"bookID\":\" --\",\"author\":\" --\",\"title":\"--\}" 
# http://127.0.0.1:5000/book
@app.route("/book", methods = ["POST"])
def create():

    if not request.json:
        abort(400)

    book = {
        "bookID":request.json["bookID"],
        "author":request.json["author"],
        "title":request.json["title"]
    }

    return jsonify(bookDAO.createBook(book))

# Create a student account
# curl -i -H "Content-Type:application/json" -X POST -d "{\"bookid\":\" --\",\"firstname\":\" --\",\"lastname":\"--\,\"studentID":\"--\}" 
# http://127.0.0.1:5000/students
@app.route("/students", methods = ["POST"])
def createstudent():

    if not request.json:
        abort(400)

    book = {
        "bookid":request.json["bookID"],
        "firstname":request.json["firstname"],
        "lastname":request.json["lastname"],
       "studentID":request.json["studentID"]
    }

    return jsonify(bookDAO.createStudent(students))


# Update book
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"author\":\"--",\"title\":\"--"}"
# http://127.0.0.1:5000/book/1
@app.route("/book/<int:bookID>", methods = ["PUT"])
def update(bookID):
    foundBook = bookDAO.getBookById(bookID)

    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)

    if 'author' in request.json:
        foundBook['author'] = request.json['author']
    if 'title' in request.json:
        foundBook['title'] = request.json['title']

    values = (foundBook['author'], foundBook['title'])

    bookDAO.updateBook(values)
    return jsonify(foundBook)
        

# Update students
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"studentID\":\"--",\"firstname\":\"--",\"lastname\":\"--"}"
# http://127.0.0.1:5000/students/1
@app.route("/students/<int:bookid>", methods = ["PUT"])
def updatestudent(bookid):
    foundBook = bookDAO.getStudentById(bookid)

    if not foundBook:
        abort(404)
    
    if not request.json:
        abort(400)

    if 'firstname' in request.json:
        foundBook['firstname'] = request.json['firstname']
    if 'lastname' in request.json:
        foundBook['lastname'] = request.json['lastname']
    if 'studentID' in request.json:
        foundBook['studentID'] = request.json['studentID']

    values = (foundBook['firstname'], foundBook['lastname'], foundBook['studentID'])

    bookDAO.updateStudents(values)
    return jsonify(foundBook)
        

# Delete a book
# curl -X DELETE http://127.0.0.1:5000/book/211
@app.route("/book/<int:bookID>", methods = ["DELETE"])
def deletebook(bookID):
    bookDAO.deleteBook(bookID)
    return jsonify({"done":True})

# Delete a book from student account
# curl -X DELETE http://127.0.0.1:5000/students/1
@app.route("/students/<int:bookid>", methods = ["DELETE"])
def deletestudent(bookid):
    bookDAO.deleteStudents(bookid)
    return jsonify({"done":True})

# Delete a user
# curl -X DELETE http://127.0.0.1:5000/users/odonovanm
@app.route("/users/<username>", methods = ["DELETE"])
def deleteuser(username):
    bookDAO.deleteUser(username)
    return jsonify({"done":True})

# Find book by author 
# curl "http://127.0.0.1:5000/book/"
@app.route("/book/<author>", methods=["GET"])
def getAuthor(author):
    current_book = bookDAO.getBookByAuthor(author)
    print(current_book)
    return jsonify(current_book)





if __name__ == '__main__' :
    app.run(debug= True)

    print('flask is running')
