from app.session.processor import Processor as Session
from app.person.processor import Processor as Person


def header_option():
    return {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*'}
    # return {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*'}


def create_session(id_user):
    return Session().create(id_user)[0]


def get_person(id_person):
    return Person().get_person(id_person)
