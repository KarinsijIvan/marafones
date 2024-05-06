from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User {self.id}: {self.login} {self.name} {self.surname} {self.password}'
