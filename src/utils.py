from src.vacancies import Vacancy


def filter_vac_by_name(vacancies: list[Vacancy], vac_name):
    """Функция для фильтрации вакансий по названию"""
    vac_name_count = 0
    vac_name_filter = []
    vac_name_lower = vac_name.lower()

    for vacancy in vacancies:
        try:
            if "name" not in vacancy:
                continue
            if vac_name_lower in vacancy["name"].lower():
                salary = vacancy["salary"]
                salary_from = salary.get("from", 0)
                salary_to = salary.get("to", 0)
                vac_data = {
                    "name": vacancy["name"],
                    "link": vacancy["alternate_url"],
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "area": vacancy["area"]["name"],
                    "description": vacancy["snippet"]["responsibility"],
                }
                vac_name_filter.append(vac_data)
                vac_name_count += 1
        except Exception as e:
            print(f"Ошибка обработки вакансии: {e}")
            continue

    return vac_name_filter


def filter_top_vac(vacancies: list[Vacancy], top_vacancies):
    """Сортирует топ вакансий"""
    return sorted(vacancies, reverse=True)[:top_vacancies]


def filter_vacancies_by_city(vacancies: list[Vacancy], city_name):
    """Функция для фильтрации вакансий по городу"""
    vac_count = 0
    vac_filter = []
    for vacancy in vacancies:
        try:
            if city_name == vacancy["area"]["name"].lower():
                salary = vacancy["salary"]
                salary_from = salary["from"] if salary and salary["from"] is not None else 0
                salary_to = salary["to"] if salary and salary["to"] is not None else 0
                vac_data = {
                    "name": vacancy["name"],
                    "link": vacancy["alternate_url"],
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "currency": salary["currency"] if salary else "RUR",
                    "area": vacancy["area"]["name"],
                    "description": vacancy["snippet"]["responsibility"],
                }
                vac_filter.append(vac_data)
                vac_count += 1
            elif city_name not in vacancy["area"]["name"]:
                continue
        except Exception as e:
            print(f"Ошибка обработки вакансии: {e}")
            continue

    return vac_filter
