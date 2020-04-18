import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'user'
        self.field = ['login, password, name', 'email']
