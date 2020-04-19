from flask import request, jsonify
from app import app
from app.person.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/person'


@app.route(PREFIX, methods=['GET', 'OPTIONS'])
def all_person():
    func = {
        'id_person': 1,
        'name': 'Студент',
        'description': 'Все мы немного студенты и хотим кушать',
        'pic': 'https://emojio.ru/images/apple-b/1f468-200d-1f393.png',
        'health': 10.0,  # Здоровье
        'food': 5.0,  # Питание
        'leisure': 3.0,  # Досуг
        'communication': 4.0,  # Общение
        'value': 3,  # количество денег
    }
    return jsonify(Processor().all_person()), header_option()
