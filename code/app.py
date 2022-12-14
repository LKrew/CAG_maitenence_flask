from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from db import db
import pymysql
import secrets


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host:port/database_name'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'CAG_maitenance'
api = Api(app)

jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

if __name__=='__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)