import random
import datetime
from pymongo import MongoClient
from faker import Faker
from bson import ObjectId
import timeit

Faker.seed(datetime.datetime.utcnow())
fake = Faker()

# Создаем экземпляр клиента MongoClient и подключаемся к стандартному хосту и порту
client = MongoClient('mongodb://localhost:27017/')

# Подключаемся к базе даных
db = client.test

# Получаем коллекции
collection_users = db.users
collection_devices = db.devices
collection_comments = db.comments
collection_sensors = db.sensors

list_device = ['Arduino Uno', 'Arduino Nano', 'Arduino Mega', 'ESP8266', 'ESP32', 'ESP32S2', 'Raspberry Pi 2',
               'Raspberry Pi 3', 'Raspberry Pi 4', 'Raspberry Pi Pico', 'Orange Pi 2 Lite', 'Orange Pi 2', 'PC',
               'MyDevice', 'Microchip', 'STM32']

dev = [list_device[random.randrange(0, len(list_device))] for i in range(3)]
list_names = []
list_id_users = []

code_to_test = """
for _ in range(20000):
    post = {"username": fake.simple_profile()['username'],
            "name": fake.simple_profile()['name'],
            "mail": fake.simple_profile()['mail'],
            "address": fake.simple_profile()['address'],
            "devices": [list_device[random.randrange(0, len(list_device))] for i in range(3)],
            "birthdate": str(fake.simple_profile()['birthdate']),
            "date_create": datetime.datetime.utcnow()
            }
"""
#     list_names.append(post["username"])
# insert document into selected document
#    result = collection_users.insert_one(post).inserted_id
#    list_id_users.append(result)
# collection_users.insert_one(post)
# print(list_names)

# for i in range(len(list_names)):
#     print(list_names[i])
#     collection_users.delete_one({'username': list_names[i]})

# for i in range(len(list_id_users)):
#    # print(list_id_users[i])
#    collection_users.delete_one({'_id': ObjectId(list_id_users[i])})


elapsed_time = timeit.timeit(code_to_test, globals=globals(), number=10) / 10
print(elapsed_time)

# all_users = collection_users.find({"username": user})
# for users in all_users:
#     for user in users:
#         print(users[user])

# collection_users.drop_one({'_id': ObjectId(result)})
