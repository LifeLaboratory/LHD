import app.base.provider as bp


class Provider(bp.Provider):
    def __init__(self):
        super().__init__()
        self.table_name = 'person'
        self.field = ['id_person', 'name', 'description', 'pic']

    def all_person(self, where='where True'):
        self.query = f'''
    select *
    from "{self.table_name}"
    {where}
'''
        return self.execute()

    def get_person(self, id_person):
        where = f'''
    where True
      and id_person = {id_person}
    limit 1
'''
        return self.all_person(where)[0]
