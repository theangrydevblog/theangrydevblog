from django.template import engines
from django.db import connection as dbconn

class DataAccessObject:
    TEMPLATE_ENGINE = engines['django']
    DATABASE_CURSOR = dbconn

    def __init__(self, sql):
        self.sql = self.__class__.TEMPLATE_ENGINE.from_string(sql)

    def run(self, params={}):
        with self.__class__.DATABASE_CURSOR.cursor() as conn:
            conn.execute(self.sql.render(params))
            return conn.fetchall()
