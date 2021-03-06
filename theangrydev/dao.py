from angrydevblog.settings import BASE_DIR
from django.template import engines
import os
from .lib.sql import DataAccessObject

dml_dir = os.path.join(BASE_DIR, 'theangrydev', 'sql')
dmls = os.listdir(dml_dir)
sql_templates = {}

for sql in dmls:
    with open(os.path.join(dml_dir, sql), "r") as f:
        sql_templates[sql] = DataAccessObject(f.read())
