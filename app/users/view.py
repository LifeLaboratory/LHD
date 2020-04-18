from flask import request, jsonify
from app import app
from app.users.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/user'


@app.route(PREFIX, methods=['GET'])
def all_user():
    return jsonify(Processor().users()), header_option()


@app.route(PREFIX + '/profile', methods=['GET'])
def profile_user():
    func = {
        'id_user': 1,
        'login': 'Hacker',
        'rating': 1,  # какое место пользователь занимает в общем рейтинге
        'count_game': 25,
        'max_point': 243,
        'pic': 'https://emojio.ru/images/apple-b/1f9d4-1f3fb.png',
        'game_history': [
            {
                'id_game': 1,
                'time': '2020-04-18 22:32:44',
                'health': 10.0,  # Здоровье
                'food': 10.0,  # Питание
                'leisure': 10.0,  # Досуг
                'communication': 10.0,  # Общение
                'point': 5  # Количество очков, заработанных за игру.
            }
        ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer, header_option()


@app.route(PREFIX + '/<int:id_user>', methods=['GET'])
def profile(id_user):
    func = {
      'id_user': 1,
      'login': 'Hacker',
      'rating': 1,  # какое место пользователь занимает в общем рейтинге
      'count_game': 25,
      'max_point': 243,
      'pic': 'https://emojio.ru/images/apple-b/1f9d4-1f3fb.png',
      'game_history': [
        {
            'id_game': 1,
            'time': '2020-04-18 22:32:44',
            'health': 10.0,  # Здоровье
            'food': 10.0,  # Питание
            'leisure': 10.0,  # Досуг
            'communication': 10.0,  # Общение
            'point': 5  # Количество очков, заработанных за игру.
        }
      ]
    }
    # answer = jsonify(Processor().profile(id_user))
    answer = jsonify(func)
    return answer, header_option()


@app.route(PREFIX + '/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    print(f'data = {data}')
    return jsonify(Processor().login(data)), header_option()


@app.route(PREFIX + '/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return {}, header_option()
    data = request.json
    print(f'data = {data}')
    return jsonify(Processor().create(data)), header_option()

