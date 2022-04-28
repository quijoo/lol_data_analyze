from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/lol'
app.config['SQLALCHEMY_BINDS'] = {'two': "sqlite:///data_backend.db"}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] =True
db=SQLAlchemy(app)


