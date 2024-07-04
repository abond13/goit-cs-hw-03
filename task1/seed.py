import faker
from random import randint
import psycopg2

NUMBER_USERS = 5
NUMBER_TASKS = 10

def generate_fake_data(number_users, number_tasks) -> tuple():
    fake_users = []# тут зберігатимемо користувачив
    fake_tasks = []# тут зберігатимемо завдання

    fake_data = faker.Faker()

# Створимо набір користувачів
    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

# Згенеруємо тепер завдання
    for _ in range(number_tasks):
        fake_tasks.append((fake_data.sentence(nb_words=2),
                           fake_data.paragraph(nb_sentences=1),
                           randint(1, 3),
                           randint(1, number_users)))

    return fake_users, fake_tasks


def insert_data_to_db(users, tasks) -> None:
# Створимо з'єднання з нашою БД та отримаємо об'єкт курсора для маніпуляцій з даними
    with psycopg2.connect('postgresql://postgres:567234@localhost:5432/hw02') as con:

        cur = con.cursor()

        sql_to_statuses = """INSERT INTO status(name)
                               VALUES (%s)"""
        cur.executemany(sql_to_statuses, [('new',), ('in progress',), ('completed',)])

        sql_to_users = """INSERT INTO users(fullname, email)
                               VALUES (%s, %s)"""
        cur.executemany(sql_to_users, users)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                              VALUES (%s, %s, %s, %s)"""
        cur.executemany(sql_to_tasks, tasks)

        con.commit()

if __name__ == "__main__":
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    insert_data_to_db(users, tasks)
