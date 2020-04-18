from app.session.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def create(self, id_user):
        return self.provider.create(id_user)

    def check_session(self, session):
        return self.provider.check_session(session)