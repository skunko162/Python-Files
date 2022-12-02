from flask_app.config.mysqlcontroller import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.password = data['password']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO user (first_name, last_name, email, password) VALUES "\
            "(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) > 0:
            return cls(results[0])
        return False

    @staticmethod
    def validator(potential_user):
        is_valid = True
        if len(potential_user['first_name']) < 2:
            flash("First name is required", "reg")
            is_valid = False
        if len(potential_user['last_name']) < 2:
            flash("Last Name is required", "reg")
            is_valid= False
        if len(potential_user['email']) < 2:
            flash("Email is required", "reg")
            is_valid= False
        if len(potential_user['password']) < 2:
            flash("Password is required", "reg")
            is_valid= False
        elif not EMAIL_REGEX.match(potential_user['email']):
            flash("email must be valid","reg")
            is_valid= False
        else:
            data = {
                'email': potential_user['email']
            }
            user_in_db = User.get_by_email(data)
            if user_in_db:
                flash("email already registered", "reg")
                is_valid = False
            if len(potential_user['password']) < 8:
                flash("Password must be at least 8 characters long", "reg")
                is_valid= False
            elif potential_user ['password'] != potential_user['confirm_pass']:
                flash("your password and confirm password fields must match!")
                is_valid= False
            return is_valid
