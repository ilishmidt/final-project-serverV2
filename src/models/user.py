users_id = 1


class User:
    def __init__(self, username, password, user_id=users_id):
        self.username = username
        self.password = password

        global users_id
        if user_id == users_id:
            users_id += 1
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def compare_password(self, to_compare):
        return self.password == to_compare

    def change_password(self, new_pass):
        self.password = new_pass
