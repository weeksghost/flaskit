#!flask/bin/python
import random
from app import db, models


names_file = file('app/static/american-english')
num_dict_lines = 9900
bytes = num_dict_lines * 10 * 8
rand_words = [ln for ln in names_file.readlines(bytes) if "'" not in ln]
names_file.close()

def gen_name():
    idx = random.randint(2, num_dict_lines)
    username = rand_words[idx]
    return username.strip()

for i in range(100):
    name = gen_name()
    data = models.Form(name="%s" % name)
    db.session.add(data)
    db.session.commit()
