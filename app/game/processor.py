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
        question = {}
        if data.get('id_user'):
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
        person['id_question'] = data.get('id_question')
        return person

    def get_game(self, id_user):
        """
        Метод получает информацию о текущей игре пользователя
        :return:
        """
        answer = {}
        game = self.provider.get_game(id_user)
        if game:
            answer = game[0]
        return answer

    def close_old_game(self, data):
        """
        Метод заканчивает старую игру пользователя
        :param data:
        :return:
        """
        self.provider.close_old_game(data)

    def update_game_status(self, data):
        """
        Метод обновляет текущую игру
        :param data:
        :return:
        """
        self.provider.update_game_status(data)

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
        answer = {}
        if data.get('id_user') and data.get('answer') in ['left', 'right']:
            answer = self.provider.check_question(data)
            if not answer:
                return {}
            else:
                answer = answer[0]
            self.debuf(answer)
            self.update_game_status(answer)
            answer['covid'] = True if answer.get('round') - answer.get('covid') < 10 else False
            if answer.get('health') <= 0:
                self.close_old_game(data)
        return answer

    def debuf(self, data):
        """
        Метод добавляет дебафы, если нехватает любой из потребностей пользователя
        :param data:
        :return:
        """
        food = -1 if data.get('food') == 0 else 0
        leisure = -1 if data.get('leisure') == 0 else 0
        communication = -1 if data.get('communication') == 0 else 0
        data['health'] += food + leisure + communication

    def game_action(self, data):
        """
        Метод обрабатывает события в игре
        :param data:
        :return:
        """
        action = {
            'worked': self.worked,
            'call_friend': self.call_friend,
            'call_delivery': self.call_delivery,
        }
        if data.get('id_user') and data.get('action') in ['worked', 'call_friend', 'call_delivery']:
            game = self.provider.game_action(data)[0]
            action.get(data.get('action'))(game)
            self.provider.update_action(game)
            return self.get_game(data.get('id_user'))

    def worked(self, game):
        work = game.get('worked')
        round = game.get('round')
        if work < 2 or round - work > 2:
            game['point'] += 1
            game['worked'] = round

    def call_friend(self, game):
        calling = game.get('call')
        round = game.get('round')
        if calling < 2 or round - calling > 2:
            game['point'] -= 3
            game['communication'] += 2
            game['leisure'] += 1
            game['call'] = round

    def call_delivery(self, game):
        calling = game.get('call')
        round = game.get('round')
        if calling < 2 or round - calling > 2:
            game['point'] -= 3
            game['food'] += 2
            game['call'] = round

    def get_next_question(self, data):
        """
        Метод выбирает следующий вопрос для пользователя
        :return:
        """
        return self.provider.get_next_question(data)