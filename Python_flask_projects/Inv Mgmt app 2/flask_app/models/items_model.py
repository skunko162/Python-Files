from flask_app.config.mysqlcontroller import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Items:
    def __init__(self,data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.item_number = data['item_number']
        self.product_description = data['product_description']
        self.price = data['price']
        self.units = data['units']
        self.lower_stock_limit = data['lower_stock_limit']
        self.total_value = data['total_value']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO items (item_name, product_description, units, price, lower_stock_limit, user_id) VALUES "\
            "(%(item_name)s, %(product_description)s, %(units)s, %(price)s, %(lower_stock_limit)s, %(user_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items JOIN user ON items.user_id = user.id"
        results = connectToMySQL(DATABASE).query_db(query)
        if len(results) > 0:
            all_items = []
            for row in results:
                this_item = cls(row)
                user_data = {
                    **row,
                    'id': row['user.id'],
                    'created_at': row['user.created_at'],
                    'updated_at': row['user.updated_at']
                }
                this_user = user_model.User(user_data)
                this_item.reporter = this_user
                all_items.append(this_item)
            return all_items
        return []

    @classmethod
    def update(cls,data):
        query = "UPDATE items SET item_name = %(item_name)s, product_description = %(product_description)s, units= %(units)s, price = %(price)s, lower_stock_limit = %(lower_stock_limit)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def add_total_value(cls,data):
        query = "SELECT units, price,(units*price) AS total_value FROM items"
        return connectToMySQL(DATABASE).query_db(query,data)

    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['item_name']) < 1:
            flash('name is required')
            is_valid = False
        if len(form_data ['product_description']) < 1:
            flash('description made is required')
            is_valid = False
        if len(form_data['price']) < 1:
            flash('price is required')
            is_valid = False
        if len(form_data['units']) < 1:
            flash('number of units is required')
            is_valid = False
        if len(form_data['lower_stock_limit']) < 1:
            flash('lower limit is required')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM items JOIN user ON items.user_id = user.id WHERE items.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)<1:
            return False
        row = results[0]
        this_item = cls(row)
        user_data = {
            **row,
            'id': row['user.id'],
            'created_at': row['user.created_at'],
            'updated_at': row['user.updated_at']
        }
        this_user = user_model.User(user_data)
        this_item.reporter = this_user
        return this_item

    @classmethod
    def delete(cls,data):
        query= "DELETE FROM items WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)