>> Author: Megan O'Donovan  
>> Date: 05/01/2024

## HDip in Computing in Data Analytics - Data Representation

### Description

The aim of this project is to demonstrate an understanding of creating and consuming RESTful APIs. The RestAPI in this repository allows users to login or register and to display, create, update and delete books from a virtual college library.

### Objectives
- Create a Web application in Flask that has a RESTful API.</br>
- The application should link to one or more database tables.</br>
- Create web pages that can consume the API, performing CRUD operations on the data.</br>

### Repository Contents

- *static_pages* -  Folder containing three web HTML pages (index.html, login.html, main.html), css and image links are also included.</br>
- *application.py* -  Flask server.</br>
- *bookDAO.py* -  Creates a data access object (DAO) to interact with the created database.</br>
- *createDatabase.py* -  SQL script to create and connect to the database and tables.</br>
- *dbconfig.py* -  SQL connection</br>
- *requirements.txt* -  The package requirements to run the project.</br>


The created database datarep3 consists of three tables:</br>

*1. users*</br>
*2. book*</br>
*3. students*</br>


### How To Get The Repository on Your Machine</br>


The repository is available to the public using the following link:</br>
https://github.com/MSoD1/Data-Rep-Project</br>

The repository can then be downloaded as a zipped folder using either SSH or HTTPS. </br>

To install the necessary packages:</br>
```python
$pip install -r requirements.txt
```
</br>

Check the packages have been installed by typing the command:</br>
 ```python
$pip freeze
```
</br>
 
The file dbconfig.py stores the connection for mysql, replace the existing host, username and password with local host values.</br>

     mysql = {
          'host': '',
           'user': '',
           'password': '',
           'database': 'datarep3'
    }

The python script createDatabase.py connects to mysql and creates the database and the tables. The script bookDAO.py interacts with the database and populates the tables. A Flask server can be created by ruuning the application.py, available at http://127.0.0.1:5000.</br>

For the web interface navigate to http://127.0.0.1:5000/index.html/ and login to interact with the server.</br>

### PythonAnywhere Hosting

The application is hosted on pythonanywhere at: https://g00411435.pythonanywhere.com/index.html/</br>

### References
<br /> - *[1] :* Beatty A. Data Representation [Internet]. 2023. Available from: https://vlegalwaymayo.atu.ie/course/view.php?id=6209
<br /> - *[2] :* Venkatesan N. Create and deploy a simple web application with flask and heroku [Internet]. Towards Data Science. 2021 [cited 2022 Dec 18]. Available from: https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb
<br /> - *[3] :* Git. Bootstrap Navbar with logo centered above navbar [Internet]. Coding Yaar. 2020 [cited 2022 Dec 18]. Available from: https://codingyaar.com/responsive-bootstrap-navbar-with-logo-centered-above-navbar/
<br /> - *[4] :* 11. Jquery Ajax url path Issue [Internet]. Stack Overflow. [cited 2022 Dec 23]. Available from: https://stackoverflow.com/questions/24627075/jquery-ajax-url-path-issue
<br /> - *[5] :* PythonAnywhere LLP. Forums [Internet]. Pythonanywhere.com. [cited 2022 Dec 24]. Available from: https://www.pythonanywhere.com/forums/topic/32182/

