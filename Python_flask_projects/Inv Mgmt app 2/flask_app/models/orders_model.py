from flask_app.config.mysqlcontroller import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Orders:
    def __init__(self,data):
        self.id = data['id']
        self.quantity_ordered = data['quantity_ordered']
        self.order_number = data['order_number']
        