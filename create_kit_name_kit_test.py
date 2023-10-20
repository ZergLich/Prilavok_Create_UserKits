import pytest
import data
import sender_stand_request

# Тестовые названия наборов
symbol_1        = "а"
symbol_511      = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol_0        = ""
symbol_512      = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
symbol_eng      = "QWErty"
symbol_rus      = "Мария"
symbol_special  = '"№%@","'
symbol_space    = "Человек и КО"
symbol_nums     = "123"
symbol_del      = "DELETE"
symbol_int      = 123


# Базовая функция для проведения проверок различных вариантов названия набора, создаваемого под пользователем Я.Прилавок
# name - Название создаваемого набора. Подставляется одна из переменных symbol_... .
# test_type (bool) - Тип проверки: позитивная (значение True) или негативная (значение False)
def _testing_kitname(name, test_type):
    # Создание нового пользователя
    user_token = sender_stand_request.post_create_user()

    # Создание набора с заданным названием под вновь созданным пользователем
    kit = sender_stand_request.post_create_kit(user_token.json()["authToken"], name)

    # Сравнение ФР и ОР в зависимости от типа проверки (позитивная или негативная)
    if (test_type):
        assert kit.status_code == 201
        assert kit.json()["name"] == name
    else:
        assert kit.status_code == 400



# ------------ Т Е С Т Ы -----------------


# Тест 01 - Допустимое название из одного символа
def test_kitname_01_positive_1_symbol():
    _testing_kitname(symbol_1, True)

# Тест 02 - Допустимое количество символов (511)
def test_kitname_02_positive_511_symbol():
    _testing_kitname(symbol_511, True)

# Тест 03 - Количество символов меньше допустимого (0)
def test_kitname_03_negative_0_symbol():
    _testing_kitname(symbol_0, False)

# Тест 04 - Количество символов больше допустимого (512)
def test_kitname_04_negative_512_symbol():
    _testing_kitname(symbol_512, False)

# Тест 05 - Разрешены английские буквы
def test_kitname_05_positive_eng_symbol():
    _testing_kitname(symbol_eng, True)

# Тест 06 - Разрешены русские буквы
def test_kitname_06_positive_rus_symbol():
    _testing_kitname(symbol_rus, True)

# Тест 07 - Разрешены спецсимволы
def test_kitname_07_positive_special_symbol():
    _testing_kitname(symbol_special, True)

# Тест 08 - Разрешены пробелы
def test_kitname_08_positive_space_symbol():
    _testing_kitname(symbol_space, True)

# Тест 09 - Разрешены цифры
def test_kitname_09_positive_nums_symbol():
    _testing_kitname(symbol_nums, True)

# Тест 10 - Параметр не передан в запросе
def test_kitname_10_negative_del_symbol():
    _testing_kitname(symbol_del, False)

# Тест 11 - Передан другой тип параметра (число)
def test_kitname_11_negative_int_symbol():
    _testing_kitname(symbol_int, False)