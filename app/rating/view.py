from flask import request, jsonify
from app import app
from app.rating.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET'])
def all_rating():
    func = {
        'top': [
            {
                'id_user': 1,
                'login': 'Hacker',
                'time': '2020-02-02 13:00:02',
                'health': 10.0,  # Здоровье
                'food': 5.0,  # Питание
                'leisure': 3.0,  # Досуг
                'communication': 4.0,  # Общение
                'point': 5,  # Количество очков, заработанных за игру.
                'value': 3,  # количество денег
            }
        ]
    }

    answer = jsonify(func)
    return answer, header_option()


@app.route(PREFIX + '/<int:id_user>', methods=['GET'])
def rating(id_user):
    func = {
      'game_history': [
        {
          'id_game': 1,
          'time': '2020-02-02 13:00:02',
          'health': 10.0,   # Здоровье
          'food': 5.0,     # Питание
          'leisure': 3.0,  # Досуг
          'communication': 4.0,   # Общение
          'point': 5, # Количество очков, заработанных за игру.
          'value': 3, # количество денег
        }
      ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer, header_option()
