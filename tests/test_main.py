from src.utils import filter_top_vac, filter_vac_by_name, filter_vacancies_by_city
from src.vacancies import Vacancy


def test_filter_vac_by_name():
    """Тестирование фильтрации вакансий по названию"""

    test_vacancies = [
        {
            "name": "Кладовщик",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "area": {"name": "Москва"},
            "snippet": {"responsibility": "Разкладывать товары"},
        },
        {
            "name": "Java Developer",
            "alternate_url": "https://hh.ru/vacancy/2",
            "salary": {"to": 120000, "currency": "RUR"},
            "area": {"name": "Санкт-Петербург"},
            "snippet": {"responsibility": "Разработка на java"},
        },
    ]

    result = filter_vac_by_name(test_vacancies, "кладовщик")
    assert len(result) == 1, "Должна быть найдена одна вакансия"

    result = filter_vac_by_name(test_vacancies, "javascript")
    assert len(result) == 0


def test_filter_vacancies_by_city():
    """Тестирование фильтрации вакансий по городу"""
    test_vacancies = [
        {
            "name": "Python Developer",
            "alternate_url": "https://hh.ru/vacancy/1",
            "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
            "area": {"name": "Москва"},
            "snippet": {"responsibility": "Разработка на Python"},
        },
        {
            "name": "Java Developer",
            "alternate_url": "https://hh.ru/vacancy/2",
            "salary": None,
            "area": {"name": "Санкт-Петербург"},
            "snippet": {"responsibility": "Разработка на Java"},
        },
    ]
    result = filter_vacancies_by_city(test_vacancies, "москва")
    assert len(result) == 1
    assert result[0]["area"] == "Москва"

    result = filter_vacancies_by_city(test_vacancies, "владивосток")
    assert len(result) == 0


def test_filter_top_vac():
    """Тестирование сортировки и отбора топ-N вакансий"""
    vacancies = [
        Vacancy("Junior", "link1", {"from": 0, "to": 50000}, "Описание 1", "City"),
        Vacancy("Middle", "link2", {"from": 80000, "to": 120000}, "Описание 2", "City"),
        Vacancy("Senior", "link3", {"from": 150000, "to": 200000}, "Описание 3", "City"),
        Vacancy("Team Lead", "link4", {"from": 180000, "to": None}, "Описание 4", "City"),
    ]

    top_result = filter_top_vac(vacancies, 2)
    assert len(top_result) == 2

    small_list = vacancies[:2]
    result = filter_top_vac(small_list, 5)

    assert len(result) == 2
