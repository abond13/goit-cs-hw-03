from pymongo import MongoClient
from pymongo.server_api import ServerApi


def find_all(db):
    for doc in db.cats.find({}):
        print(doc)

def find_by_name(db, name):
    for doc in db.cats.find({"name": name}):
        print(doc)

def update_age(db, name, age):
    if db.cats.update_one({"name": name},
                          {"$set": {"age": age}}
                          ).matched_count == 1:
        print(f"update age for {name} on {age}: done")
    else:
        print(f"Wrong name {name}")

def add_feature(db, name, feature):
    if db.cats.update_one({"name": name},
                          {"$push": {"features": feature}}
                          ).matched_count == 1:
        print(f"add feature for {name}: done")
    else:
        print(f"Wrong name {name}")

def delete_by_name(db, name):
    db.cats.delete_one({"name": name})
    print(f"delete {name}: done")

def delete_all(db):
    db.cats.delete_many({})
    print("delete all: done")

def main():
    with MongoClient(
        "mongodb://root:example@localhost:27017/?retryWrites=true&w=majority",
        server_api=ServerApi('1')
        ) as client:

        db = client.cats

        # Тестові записи
        result_many = db.cats.insert_many(
            [
                {
                    "name": "Barsik",
                    "age": 3,
                    "features": ["ходить в капці", "дає себе гладити", "рудий"]
                },
                {
                    "name": "Lama",
                    "age": 2,
                    "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
                },
                {
                    "name": "Liza",
                    "age": 4,
                    "features": ["ходить в лоток", "дає себе гладити", "білий"],
                },
            ]
        )
        print(result_many.inserted_ids)

        print("\n\nВсі документи:")
        find_all(db)

        print("\n\nДокумент для Barsik:")
        find_by_name(db, "Barsik")

        print("\n\nЗмінити вік для Barsik:")
        update_age(db, "Barsik", 8)    

        print("\n\nДодати Barsik нову feature:")
        add_feature(db, "Barsik", "ловить мишей")

        print("\n\nДокумент для Barsik:")
        find_by_name(db, "Barsik")

        print("\n\nВидалити документ для Barsik:")
        delete_by_name(db, "Barsik")

        print("\n\nВсі документи:")
        find_all(db)    

        print("\n\nВидалити всі документи:")
        delete_all(db)

        print("\n\nВсі документи:")
        find_all(db)

if __name__ == "__main__":
    main()