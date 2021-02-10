from flask import Flask
from app_flask.config import Config

app = Flask(__name__)
app.config.from_object(Config)  # конфиг

# Нижний импорт
from app_flask import main_routes
