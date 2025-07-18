from src.hh_api import HH_Api
from src.json_file import JSONFile
from src.utils import filter_top_vac, filter_vac_by_name, filter_vacancies_by_city


def greeting():
    return "Добро пожаловать в программу по поиску вакансий!"


def w_json_file(keyword=None):
    """Запись вакансий в JSON файл"""
    try:
        hh = HH_Api()
        if not keyword:
            keyword = input("Введите ключевое слово для поиска вакансий: ").lower()

        vacancies = hh.get_vacancies(keyword)
        json_file = JSONFile()
        json_file.w_vacancies(vacancies)

        return "Список вакансий успешно сохранен."
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def r_json():
    """Чтение JSON файла и вывод данных в консоль"""
    json_file = JSONFile()
    vac = json_file.r_vacancies()
    print("\nЗагружаем список вакансий...")
    print(f"\nЗагружено {len(vac)} вакансий")
    for v in vac:
        print(v)
    return


def filter_by_name():
    """Фильтрация вакансий по названию"""
    hh = HH_Api()
    vac_name = input("Введите ключевое слово для поиска: ").lower()
    vacancies = hh.get_vacancies(vac_name)
    filtered_vacancies = filter_vac_by_name(vacancies, vac_name)
    print(f"\nНайдено вакансий: {len(filtered_vacancies)} по запросу '{vac_name}'\n")

    for vacancy in filtered_vacancies:
        salary_str = f"от {vacancy['salary_from']} до {vacancy['salary_to']}"

        print(
            f"Название: {vacancy['name']}\n"
            f"Ссылка: {vacancy['link']}\n"
            f"Описание: {vacancy['description'] or 'Описание отсутствует'}\n"
            f"Город: {vacancy['area']}\n"
            f"Зарплата: {salary_str}\n"
            f"{'-' * 50}"  # разделитель между вакансиями
        )

    return


def sort_top():
    """Сортировка топ вакансий"""
    json_file = JSONFile()
    vac = json_file.r_vacancies()
    print(f"\nМожно отсортировать {len(vac)} вакансий по топу ")
    top_vacancies = int(input("Для вывода топа вакансий введите число: "))
    vacancion = filter_top_vac(vac, top_vacancies)
    if 0 < top_vacancies <= len(vac):
        print(f"Вы ввели {top_vacancies}, отсортировано {top_vacancies}: ")
        for v in vacancion:
            print(v)
    elif top_vacancies > len(vac):
        print(f"Вы ввели {top_vacancies}, для сортировки доступно только {len(vac)}, отсортировано {len(vac)}: ")
        for v in vacancion:
            print(v)
    elif top_vacancies <= 0:
        print(f"Вы указали {top_vacancies}, не получится отсортировать")


def filter_by_city():
    """Фильтрация вакансий по городам"""
    hh = HH_Api()
    city_name = input("Введите название города: ").lower()
    vacancies = hh.get_vacancies(city_name)
    filtered_vacancies = filter_vacancies_by_city(vacancies, city_name)
    print(f"\nНайдено вакансий: {len(filtered_vacancies)} по запросу '{city_name}'\n")

    for vacancy in filtered_vacancies:
        salary_str = f"от {vacancy['salary_from']} до {vacancy['salary_to']}"

        print(
            f"Название: {vacancy['name']}\n"
            f"Ссылка: {vacancy['link']}\n"
            f"Описание: {vacancy['description'] or 'Описание отсутствует'}\n"
            f"Город: {vacancy['area']}\n"
            f"Зарплата: {salary_str}\n"
            f"{'-' * 50}"  # разделитель между вакансиями
        )

    return


if __name__ == "__main__":
    print(greeting())
    print(w_json_file())
    r_json()
    filter_by_name()
    sort_top()
    filter_by_city()
