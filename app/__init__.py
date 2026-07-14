from flask import Flask

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

from app import routes