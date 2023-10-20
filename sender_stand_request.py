import requests

import data
import configuration

# Функция для создания нового пользователя
def post_create_user():
    return requests.post(configuration.STAND_URL + configuration.CREATE_USER_PATH,
                         headers = data.user_headers,
                         json = data.user_body)

# Функция для создания нового набора под пользователем
def post_create_kit(user_token_str, kit_name):
    # Копируем дефолтные заголовки
    kits_headers = data.kits_headers.copy()
    # и вставляем в них токен от нового пользователя, полученный на вход функции
    kits_headers["Authorization"] = "Bearer " + user_token_str

    # Копируем дефолтное тело запроса на создание набора
    kit_body = data.kits_body.copy()

    # если название набора "DELETE", то удаляем сам ключ name
    # иначе вставляем в ключ name переданное функции название набора
    if(kit_name == "DELETE"):
        kit_body.pop("name")
    else:
        kit_body["name"] = kit_name

    # Возвращаем результат запроса на создание нового набора
    return requests.post(configuration.STAND_URL + configuration.CREATE_KIT_PATH,
                         headers = kits_headers,
                         json = kit_body
                        )
