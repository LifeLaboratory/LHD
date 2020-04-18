from app.users.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def create(self, data):
        return self.provider.create(data)

    def login(self, data):
        return self.provider.login(data)

    def profile(self, id_user):
        return self.provider.profile(id_user)

    def users(self):
        return self.provider.users()
