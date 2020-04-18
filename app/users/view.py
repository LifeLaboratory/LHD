from flask import request, jsonify
from app import app
from app.users.processor import Processor

PREFIX = '/api/v1/user'



@app.route(PREFIX + '/<int:id_user>', methods=['GET', 'PUT'])
def profile(id_user):
    answer = dict()
    if request.method == 'PUT':
        answer = jsonify(Processor())
    elif request.method == 'GET':
        answer = jsonify(Processor().profile(id_user))
    return answer


@app.route(PREFIX + '/login', methods=['POST'])
def login():
    data = request.json
    return jsonify(Processor().login(data))


@app.route(PREFIX + '/register', methods=['POST'])
def register():
    data = request.json
    return jsonify(Processor().create(data))

