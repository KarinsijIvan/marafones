from flask_restful import Resource
from flask import request
from models import Data, db


class Registration(Resource):
    @staticmethod
    def get():
        users_data = Data.query.all()

        data_list = [
            {'id': user_data.id, 'login': user_data.login,
                "name": user_data.name, "surname": user_data.surname,
                "password": user_data.password} for user_data in users_data
        ]

        return {'data': data_list}

    @staticmethod
    def post():
        users_data = Data.query.all()
        add_data = request.get_json()
        
        if not add_data:
            return {'message': 'No input data provided'}, 400

        login = add_data.get("login")
        password = add_data.get("password")
        name = add_data.get("name")
        surname = add_data.get("surname")

        if not login:
            return {"message": "Введите логин"}, 400

        for user_data in users_data:
            if user_data.login == login:
                return {"message": "Этот логин уже существует"}, 400

        if not password:
            return {"message": "Введите пароль"}, 400

        if not name:
            return {"message": "Введите имя"}, 400

        if not surname:
            return {"message": "Введите фамилию"}, 400

        new_data = Data(login=login, name=name, surname=surname, password=password)

        db.session.add(new_data)

        db.session.commit()
        
        return {"message": "data added", "data": {
            "id": new_data.id, "login": new_data.login,
            "name": name, "surname": surname,
            "password": new_data.password}
            }
