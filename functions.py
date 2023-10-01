import sqlite3
from config import admin

connection = sqlite3.connect('data.db')  # Подключение к базе данных
q = connection.cursor()

# Создаем таблицу users, если она ещё не существует
q.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        block INTEGER DEFAULT 0
    )
""")
connection.commit()

def join(chat_id):
    q.execute(f"SELECT * FROM users WHERE user_id = {chat_id}")
    result = q.fetchall()
    if len(result) == 0:
        sql = 'INSERT INTO users (user_id, block) VALUES ({}, 0)'.format(chat_id)
        q.execute(sql)
        connection.commit()

async def antiflood(*args, **kwargs): #анти-флуд система, время изменить можно на 102 строчке в bot.py
    m = args[0]
    if m.chat.id == admin:
    	pass
    else:
    	await m.answer("Сработала защита от флуда! Попробуйте через 2 минуты!")