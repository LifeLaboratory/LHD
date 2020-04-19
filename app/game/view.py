from flask import request, jsonify
from app import app
from app.game.processor import Processor
from app.base.helper import header_option, check_session, session_to_id_user

PREFIX = '/api/game'


@app.route(PREFIX, methods=['GET', 'POST', "OPTIONS"])
def game_main():
    answer = {}
    if request.method == 'OPTIONS':
        return {}, header_option()
    elif request.method == 'POST':
        data = request.json
        check_session(data, request.headers)
        answer = Processor().start_game(data)
        answer = Processor().get_game(data.get('id_user'))
    elif request.method == 'GET':
        id_user = session_to_id_user(request.headers)
        answer = Processor().get_game(id_user)
    answer = jsonify(answer)
    return answer, header_option()


@app.route(PREFIX + '/question', methods=['POST', 'OPTIONS'])
def game_question():
    if request.method == 'OPTIONS':
        return {}, header_option()
    data = request.json
    check_session(data, request.headers)
    answer = jsonify(Processor().check_question(data))
    return answer, header_option()


@app.route(PREFIX + '/action', methods=['POST', 'OPTIONS'])
def game_action():
    if request.method == 'OPTIONS':
        return {}, header_option()
    data = request.json
    check_session(data, request.headers)
    answer = jsonify(Processor().game_action(data))
    return answer, header_option()


@app.route(PREFIX + '/events', methods=['GET'])
def game_events():
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
