import json
from abc import ABC, abstractmethod

from src.vacancies import Vacancy


class Abc_Json(ABC):
    """Абстрактный метод для чтения записи и редактирования JSON файла"""

    @abstractmethod
    def w_vacancies(self, vacancies):
        """Метод записи в файл"""
        pass

    @abstractmethod
    def r_vacancies(self):
        """Метод чтения файла"""
        pass

    @abstractmethod
    def d_vacancies(self):
        """Метод удаления данных"""
        pass


class JSONFile(Abc_Json):
    def __init__(self, filename="../data/vacancies.json"):
        self.__filename = filename

    def w_vacancies(self, vacancies: list[dict]):
        """Добавляет вакансии в JSON-файл"""
        vacancies_filter = []
        for vacancy in vacancies:
            vacancies_filter.append(
                {
                    "name": vacancy["name"],
                    "link": vacancy["alternate_url"],
                    "salary": vacancy["salary"],
                    "area": vacancy["area"]["name"],
                    "description": vacancy["snippet"]["responsibility"],
                }
            )
        try:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(vacancies_filter, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            print(f"Ошибка: файл {self.__filename} не найден. Проверьте путь к файлу.")
        except IOError as e:
            print(f"Ошибка при записи файла: {e}")

    def r_vacancies(self):
        """Читает JSON-файл"""
        try:
            with open(self.__filename, encoding="utf-8") as file:
                data = json.load(file)
                vac = []
                for vacancy in data:
                    vac.append(Vacancy(**vacancy))
                return vac
        except FileNotFoundError:
            print(f"Ошибка: файл {self.__filename} не найден. Проверьте путь к файлу.")
        except IOError as e:
            print(f"Ошибка при записи файла: {e}")

    def d_vacancies(self):
        """Очищает JSON-файл"""
        with open(self.__filename, "w") as file:
            json.dump([], file)
