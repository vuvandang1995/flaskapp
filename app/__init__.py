from flask import Flask 
my_app = Flask(__name__)
import config
my_app.config.from_object(config)
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(my_app)
from app import views
