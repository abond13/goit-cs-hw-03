import psycopg2

with psycopg2.connect('postgresql://postgres:567234@localhost:5432/hw02') as con:
    cur = con.cursor()
    cur.execute(open("schema.sql", "r").read())
    con.commit()