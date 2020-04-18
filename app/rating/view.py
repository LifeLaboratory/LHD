from flask import request, jsonify
from app import app
from app.rating.processor import Processor
from app.base.helper import header_option

PREFIX = '/api/rating'


@app.route(PREFIX, methods=['GET'])
def all_rating():
    top = Processor().get_top_users()
    func = {
        'top': top
    }
    answer = jsonify(func)
    return answer, header_option()
