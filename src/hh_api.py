from abc import ABC, abstractmethod

import requests


class Abc_Api(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def _connect(self, text):
        """Метод для подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, text):
        """Метод для получения вакансий"""
        pass


class HH_Api(Abc_Api):
    """ ""Класс для взаимодействия с API HeadHunter (hh.ru)."""

    def __init__(self, page=0):
        """Инициализирует подключение к API hh.ru."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"page": page, "per_page": 5, "area": ["113"]}

    def _connect(self, text):
        """Устанавливает соединение с API hh.ru и возвращает ответ."""
        self.__params["text"] = text
        response = requests.get(self.__url, params=self.__params)
        response.raise_for_status()
        return response

    def get_vacancies(self, text):
        """Возвращает список вакансий по заданному поисковому запросу."""
        vacancies = self._connect(text).json()["items"]
        return vacancies
