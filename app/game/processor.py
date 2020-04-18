from app.game.provider import Provider
from app.base.helper import get_person

class Processor:
    def __init__(self):
        self.provider = Provider()

    def start_game(self, data):
        """
        Метод запускает новую игру
        :param data:
        :return:
        """
        self.close_old_game(data)
        question = self.get_next_question(data)
        if question:
            data['id_question'] = question.get('id_question')
            person = self.set_person_character(data)
            game = self.provider.start_game(person)
            if not game:
                question = {}
        return question

    def set_person_character(self, data):
        """
        Метод по ID персонажа получает все базовые характеристики
        :param data:
        :return:
        """
        person = get_person(data.get('id_person'))
        person['id_user'] = data.get('id_user')
        return person

    def get_game(self):
        """
        Метод получает информацию о текущей игре пользователя
        :return:
        """
        pass

    def close_old_game(self, data):
        """
        Метод заканчивает старую игру пользователя
        :param data:
        :return:
        """
        self.provider.close_old_game(data)

    def get_question(self):
        """
        Метод возвращает текущий вопрос для игры
        :return:
        """
        pass

    def check_question(self, data):
        """
        Метод проверяет, верно ли ответил пользователь
        :param data:
        :return:
        """
        pass

    def get_next_question(self, data):
        """
        Метод выбирает следующий вопрос для пользователя
        :return:
        """
        return self.provider.get_next_question(data)