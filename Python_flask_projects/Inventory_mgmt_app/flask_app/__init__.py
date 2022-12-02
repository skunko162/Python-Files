from flask import Flask
DATABASE = "Inventory_management"
app = Flask(__name__)
app.secret_key = "Placeholder do not use in production."