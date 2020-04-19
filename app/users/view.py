from flask import request, jsonify
from app import app
from app.users.processor import Processor
from app.base.helper import header_option, session_to_id_user

PREFIX = '/api/user'


@app.route(PREFIX, methods=['GET'])
def all_user():
    return jsonify(Processor().users()), header_option()


@app.route(PREFIX + '/profile', methods=['GET', 'OPTIONS'])
def profile_user():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    id_user = session_to_id_user(request.headers)
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return jsonify(answer), header_option()


@app.route(PREFIX + '/<int:id_user>', methods=['GET', 'OPTIONS'])
def profile(id_user):
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    answer = Processor().profile(id_user)
    if answer:
        answer = answer[0]
    else:
        answer = {}
    return jsonify(answer), header_option()


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

