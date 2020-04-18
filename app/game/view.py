from flask import request, jsonify
from app import app
from app.game.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/game'


@app.route(PREFIX, methods=['GET', 'POST', "OPTIONS"])
def game_main():
    if request.method == 'OPTIONS':
        return {}, header_option()
    elif request.method == 'POST':
        pass # Вызвать метод создания игры
    func = {
      'id_question': 1,
      'description': 'Самый лучший вопрос?',
      'round': 10, # Номер раунда игры
      'health': 10.0,   # Здоровье
      'food': 10.0,     # Питание
      'leisure': 10.0,  # Досуг
      'communication': 10.0,   # Общение
      'point': 2,  # количество очков
      'value': 3,  # количество денег
    }
    answer = jsonify(func)
    return answer, header_option()


@app.route(PREFIX + '/question', methods=['POST'])
def game_question():
    if request.method == 'OPTIONS':
        return {}, header_option()
    func = {
      'id_question': 1,
      'description': 'Самый лучший вопрос?',
      'round': 10,  # Номер раунда игры
      'health': 10.0,   # Здоровье
      'food': 10.0,     # Питание
      'leisure': 10.0,  # Досуг
      'communication': 10.0,   # Общение
      'point': 2,  # количество очков
      'value': 3,  # количество денег
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer, header_option()


@app.route(PREFIX + '/events', methods=['GET'])
def game_question():
    func = {
      'event': [
        {
          'element': 'DIV', # какой элемент изменился
          'description': 'Пользователь заразился CoronaVirus'
        }
      ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer, header_option()
