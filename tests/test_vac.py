import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vac_test_fix():
    vac = Vacancy(
        "Кладовщик",
        "https://hh.ru/vacancy/121171854",
        {"from": 100000, "to": 150000},
        "Погрузка и выгрузка товара. Сборка заказа с помощью " "голосового терминала и электротележки.",
        "Москва",
    )
    return vac


def test_product(vac_test_fix):
    assert vac_test_fix.name == "Кладовщик"
    assert vac_test_fix.link == "https://hh.ru/vacancy/121171854"
    assert vac_test_fix.salary_from == 100000
    assert vac_test_fix.salary_to == 150000
    assert vac_test_fix.description == (
        "Погрузка и выгрузка товара. Сборка заказа " "с помощью голосового терминала и электротележки."
    )
    assert vac_test_fix.area == "Москва"


def test_product_min_salary():
    vac = Vacancy(
        "Кладовщик",
        "https://hh.ru/vacancy/121171854",
        {"from": 0, "to": 0},
        "Погрузка и выгрузка товара. Сборка заказа " "с помощью голосового терминала и электротележки.",
        "Москва",
    )

    assert vac.salary_from == 0
    assert vac.salary_to == 0


def test_empty_name():
    vac = Vacancy(
        None,
        "https://hh.ru/vacancy/121171854",
        {"from": 0, "to": 0},
        "Погрузка и выгрузка товара. Сборка заказа с помощью голосового терминала и электротележки.",
        "Москва",
    )

    assert vac.name is None
