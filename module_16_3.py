# Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete.

# импорт библиотеки FastAPI, Path, Annotated
from fastapi import FastAPI, Path
from typing import Annotated

# Создано приложение(объект) FastAPI
app = FastAPI()

# Создайте словарь
users = {'1': 'Имя: Example, возраст: 18'}

# get запрос по маршруту '/users', который возвращает словарь users
@app.get('/users')
async def get_users() -> dict:
    return users

# post запрос по маршруту '/user/{username}/{age}',
# который добавляет в словарь по максимальному по значению
# ключом значение строки "Имя: {username}, возраст: {age}".
# И возвращает строку "User <user_id> is registered"
@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str,
            Path(max_length=30, description='Введите имя', example='Vasiliy')],
        age: Annotated[int,
            Path(le=120, description='Введите возраст', example='20')]
) -> str:
    # присвоение следующего id пользователю
    new_user_id = str(int(max(users, key=int)) + 1)
    # добавление в users
    users[new_user_id] = f'Имя: {username}: Возраст: {age}'
    return f'Пользователь {new_user_id} зарегестрирован'

# put запрос по маршруту '/user/{user_id}/{username}/{age}',
# который обновляет значение из словаря users под ключом
# user_id на строку "Имя: {username}, возраст: {age}".
# И возвращает строку "The user <user_id> is updated"
@app.put('/user/{user_id}/{username}/{age}')
async def put_users(
        user_id: int,
        username: Annotated[str,
            Path(max_length=30, description='Введите свое имя', example='Vasiliy')],
        age: Annotated[int,
            Path(ge=18, le=120, description='Введите возраст', example='24')]
) -> str:
    # изменяем имя и возраст пользователя с user_id
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'Пользователь {user_id} обновлен'

# запрос по маршруту '/user/{user_id}', который удаляет из словаря users
# по ключу user_id пару
@app.delete('/user/{user_id}')
async def del_users(user_id: str) -> str:
    users.pop(user_id)
    return f'Пользователь {user_id} удален'