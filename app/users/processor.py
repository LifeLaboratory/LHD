from app.users.provider import Provider
from app.base.helper import create_session


class Processor:
    def __init__(self):
        self.provider = Provider()

    def create(self, data):
        user = self.provider.create(data)
        if user:
            return create_session(user[0].get('id_user'))

    def login(self, data):
        user = self.provider.login(data)
        if user:
            return create_session(user.get('login'))

    def profile(self, id_user):
        return self.provider.profile(id_user)

    def users(self):
        return self.provider.users()
