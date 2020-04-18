from flask import request, jsonify
from app import app
from app.rating.processor import Processor

PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET'])
def all_rating():
    func = {
      "id_user": 1,
      "point": 12
    }

    answer = jsonify(func)
    return answer


@app.route(PREFIX + '/<int:id_user>', methods=['GET'])
def rating(id_user):
    func = {
      'game_history': [
        {
          'id_game': 1,
          'time': '2020-02-02 13:00:02',
          'Health': 10.0,   # Здоровье
          'food': 5.0,     # Питание
          'Leisure': 3.0,  # Досуг
          'Communication': 4.0,   # Общение
          'point': 5, # Количество очков, заработанных за игру.
          'value': 3, # количество денег
        }
      ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer
