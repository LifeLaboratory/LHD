from app.session.processor import Processor as Session
from app.person.processor import Processor as Person


def header_option():
    return {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*'}
    # return {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'Access-Control-Allow-Methods': '*'}


def create_session(id_user):
    return Session().create(id_user)[0]


def session_to_id_user(header):
    data = {}
    check_session(data, header)
    return data.get('id_user')


def check_session(data, header):
    session = header.get('session') or header.get('Session')
    if session:
        id_user = Session().check_session(session)
        if id_user:
            data['id_user'] = id_user.get('id_user')


def get_person(id_person):
    return Person().get_person(id_person)
