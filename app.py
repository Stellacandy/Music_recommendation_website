from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server host
app.config['MYSQL_USER'] = 'username'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'password'  # MySQL password
app.config['MYSQL_DB'] = 'database_name'  # MySQL database name
mysql = MySQL(app)
