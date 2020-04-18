from app.rating.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def get_top_users(self):
        return self.provider.get_top_users()
