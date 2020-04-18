from app.person.provider import Provider


class Processor:
    def __init__(self):
        self.provider = Provider()

    def all_person(self):
        return self.provider.all_person()

    def get_person(self, id_person):
        return self.provider.get_person(id_person)
