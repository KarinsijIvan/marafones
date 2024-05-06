from flask import Flask
from flask_restful import Api
from models import db
import config
from resources import Registration

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

api = Api(app)
api.add_resource(Registration, '/registration')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
