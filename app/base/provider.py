import psycopg2
import os
from pprint import pprint
from psycopg2.extras import RealDictCursor

from app.config import DATABASE


class Provider:
    """
    Базовый класс для работы с БД
    """
    def __init__(self):
        """
        При совершение запроса
        """
        self.query = None
        self.connect, self.current_connect = Provider.connect()

    def __del__(self):
        """
        После завершения обработки запроса
        """
        self.connect.commit()
        self.connect.close()

    def execute(self):
        if os.environ["IS_DEBUG"]:
            print(self.query)
        return self.exec(self.query)

    @staticmethod
    def connect():
        """
        Метод подключения к бд
        :return:
        """
        config_connect = "dbname='{dbname}' user='{user}' host='{host}' password='{password}'"
        connect = psycopg2.connect(config_connect.format(**DATABASE))
        return connect, connect.cursor(cursor_factory=RealDictCursor)

    @staticmethod
    def exec(query=None, args=None, file=None):
        """
        Метод для выполнения sql запроса
        :param query:
        :param args:
        :param file:
        :return:
        """
        return Provider._switch(query=query, args=args, file=file)

    @staticmethod
    def _switch(query=None, args=None, file=None):
        """
        Метод разводящий - для выбора режима sql запроса
        с аргументами
        без аргументов
        файл с аргументами
        файл без аргументов
        :param query:
        :param args:
        :param file:
        :return:
        """
        if query and args:
            return Provider._query_exec_args(query, args)
        if query and not args:
            return Provider._query_exec(query)
        if file and args:
            return Provider._query_file_args_exec(file, args)
        if file:
            return Provider._query_file_exec(file)
        return

    @staticmethod
    def _query_exec(query):
        """
        Выполнить sql без аргументов
        :param query:
        :return:
        """
        return Provider._exec(query)

    @staticmethod
    def _query_file_exec(file):
        """
        Метод вычитывает sql запрос из файла и исполняет его без аргументов
        :param file:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read()
            return Provider._exec(query)

    @staticmethod
    def _query_file_args_exec(file, args):
        """
        Метод вычитывает sql запрос из файла и исполняет его с аргументами
        :param file:
        :param args:
        :return:
        """
        with open(file, 'r') as f:
            query = f.read().format(**args)
            return Provider._exec(query)

    @staticmethod
    def _query_exec_args(query, args):
        """
        Метод выполняет sql запрос с аргументами
        :param query:
        :param args:
        :return:
        """
        for k, v in args.items():
            alert_items = ["'", '"', ';', '-', '*', 'drop', 'select', '=', 'insert']
            if isinstance(v, str):
                for alert in alert_items:
                    if alert in v:
                        args[k] = args[k].replace(alert, '')
        query = query.format(**args)
        print(query)
        return Provider._exec(query)

    @staticmethod
    def _exec(query):
        """
        Метод выполняет SQL запрос к базе
        :param query: str SQL запрос
        :return: dict результат выполнения запроса
        """
        connect, current_connect = Provider.connect()
        current_connect.autocommit = True
        result = None
        try:
            current_connect.execute(query)
            connect.commit()
        except psycopg2.Error as e:
            print(e.pgerror)
            print(e.diag.message_primary)
            print(psycopg2.errorcodes.lookup(e.pgcode))
        finally:
            try:
                result = current_connect.fetchall()
            except:
                pass
            finally:
                connect.close()
                return result
