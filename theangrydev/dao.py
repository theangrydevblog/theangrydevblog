from angrydevblog.settings import BASE_DIR
import os

dml_dir = os.path.join(BASE_DIR, 'theangrydev', 'sql')
dmls = os.listdir(dml_dir)
queries = {}
for sql in dmls:
    with open(os.path.join(dml_dir, sql), "r") as f:
        queries[sql] = f.read()
