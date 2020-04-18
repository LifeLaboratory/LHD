from flask import request, jsonify
from app import app
from app.users.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/user'


@app.route(PREFIX, methods=['GET'])
def all_user():
    func = {
        'users': [
            {
                'id_user': 1,
                'login': 'Hacker_user'
            }
        ]
    }
    answer = jsonify(func)
    return answer


@app.route(PREFIX + '/<int:id_user>', methods=['GET'])
def profile(id_user):
    func = {
      'id_user': 1,
      'login': 'Hacker',
      'rating': 1,  # какое место пользователь занимает в общем рейтинге
      'game_history': [
        {
          'id_game': int,
          'time': str,
          'Health': float,   # Здоровье
          'food': float,     # Питание
          'Leisure': float,  # Досуг
          'Communication': float,   # Общение
          'point': int # Количество очков, заработанных за игру.
        }
      ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer


@app.route(PREFIX + '/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    answer = {
        'session': '123e4567-e89b-12d3-a456-426655440000'
    }

    # return jsonify(Processor().login(data))
    return jsonify(answer)


@app.route(PREFIX + '/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return {}, header_option()
    data = request.json
    answer = {
        'session': '123e4567-e89b-12d3-a456-426655440000'
    }
    # return jsonify(Processor().create(data))
    return jsonify(answer)

