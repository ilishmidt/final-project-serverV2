from flask import request, jsonify
import src.database
from src.models import User


class AuthenticationController:
    @staticmethod
    def login():
        try:
            data = request.get_json(force=True)
            username_form = data.get('username')
            password_form = data.get('password')
            # user_mongo_db = src.database.mongo.db.Users.find_one({'username': username_form})
            user_mongo_db = src.database.mongo.get_one_user({'username': username_form})

            user = User(user_mongo_db['username'], user_mongo_db['password'], user_mongo_db['user_id'])

            if user and user.compare_password(password_form):
                result = True
            else:
                result = False
            return jsonify({"success": result}), 200
        except Exception as e:
            return jsonify(str(e)), 400

    @staticmethod
    def register():
        try:
            data = request.get_json(force=True)
            new_user = User(data.get('username'), data.get('password'))
            src.database.mongo.db['Users'].insert_one(new_user.__dict__)
            return jsonify({"user_id": new_user.get_user_id()}), 200
        except Exception as e:
            return jsonify(str(e)), 400

