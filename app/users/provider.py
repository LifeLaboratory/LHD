import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'
        self.field = ['login', 'password']

    def create(self, data):
        self.query = f'''
  insert into "{self.table_name}"
  (login, password)
  values (
    '{data.get('login')}'
    , '{data.get('password')}'
  )
  returning id_user
'''
        return self.execute()

    def check_user(self, data):
        where = f'''
  where true
    and '{data.get('login')}' = "login"
  limit 1
'''
        user = self.users(where)
        return user[0] if user else None

    def login(self, data):
        where = f'''
  where true
    and '{data.get('login')}' = "login"
    and '{data.get('password')}' = "password"
  limit 1
        '''
        user = self.users(where)
        return user[0] if user else None

    def profile(self, id_user):
        where = f'where id_user = {id_user}'
        return self.users(where)

    def users(self, where='where True'):
        self.query = f'''
  select 
    id_user
    , login
  from "{self.table_name}"
  {where}
        '''
        return self.execute()
