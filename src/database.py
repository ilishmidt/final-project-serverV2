from flask_pymongo import PyMongo


class Database:
    def __init__(self):
        self.mongo = PyMongo()

    def get_mongo(self):
        return self.mongo

    def get_one_user(self, data):
        return self.mongo.db.Users.find_one(data)

    def insert_one_user(self, data):
        self.mongo.db.Users.insert(data)


mongo = Database()
# mongo = PyMongo()
