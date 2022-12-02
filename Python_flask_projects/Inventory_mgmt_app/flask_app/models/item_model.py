from flask_app.config.mysqlcontroller import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Items:
    def __init__(self,data):
        self.id = data['id']
        self.item_name = data['item_name']
        self.item_number = data['item_number']
        self.shelf_life = data['shelf_life']
        self.ship_hold = data['ship_hold']
        self.incr = data['incre']
        self.unit_size = data['unit_size']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO items (item_name, item_number, shelf_life, ship_hold, incre, unit_size, user_id) VALUES "\
            "(%(item_name)s, %(item_number)s, %(shelf_life)s, %(ship_hold)s, %(incre)s,%(unit_size)s, %(user_id)s)"
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
        query = "UPDATE items SET item_name = %(item_name)s, item_number = %(item_number)s, shelf_life = %(shelf_life)s, ship_hold = %(ship_hold)s, incre= %(incre)s, unite_size = %(unit_size)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validator(form_data):
        is_valid = True
        if len(form_data['item_name']) < 1:
            flash('item name is required')
            is_valid = False
        if len(form_data ['item_number']) < 1:
            flash('item number is required')
            is_valid = False
        if len(form_data['self_life']) < 1:
            flash('self life in days is required')
            is_valid = False
        if len(form_data['ship_hold']) < 1:
            flash('ship hold in days is required')
            is_valid = False
        if len(form_data['incre']) < 1:
            flash('increment of Lots or Units is required')
            is_valid = False
        if len(form_data['unit_size']) < 1:
            flash('unit size in lbs or kgs is required')
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