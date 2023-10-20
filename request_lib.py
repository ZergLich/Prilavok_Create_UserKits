import requests

import data
import urls

# Функция для создания нового пользователя
def post_create_user():
    return requests.post(urls.STAND_URL + urls.CREATE_USER_PATH,
                         headers = data.user_headers,
                         json = data.user_body)

# Функция для создания нового набора под пользователем
def post_create_kit(user_token_str, kit_name):
    kits_headers = data.kits_headers.copy()
    kit_body = data.kits_body.copy()
    kits_headers["Authorization"] = "Bearer " + user_token_str
    if(kit_name == "DELETE"):
        kit_body.pop("name")
    else:
        kit_body["name"] = kit_name
    return requests.post(urls.STAND_URL + urls.CREATE_KIT_PATH,
                         headers = kits_headers,
                         json = kit_body
                        )
