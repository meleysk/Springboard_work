import json
import sqlite3

db = sqlite3.connect('test.db')

with open('xpath-scraper-results.json', encoding='utf-8-sig') as json_file:
    json_data = json.loads(json_file.read())

# get the list of the columns(keys) in the JSON file and insert to colums list
    columns = []
    column = []
    for data in json_data:
        column = list(data.keys())
        for c in column:
            if c not in columns:
                columns.append(c)
# get values of the columns in the JSON file in the right order.
    value = []
    values = []
    for data in json_data:
        for i in columns:
            value.append(str(dict(data).get(i)))
        values.append(list(value))
        value.clear()

# generate the create and insert queries and apply it to the sqlite3 database
    create_query = "create table if not exists quotes ({0})".format(
        " text,".join(columns))
    insert_query = "insert into quotes ({0}) values (?{1})".format(
        ",".join(columns), ",?" * (len(columns)-1))
    c = db.cursor()
    c.execute(create_query)
    c.executemany(insert_query, values)
    values.clear()
    db.commit()
    c.close()
