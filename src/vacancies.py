class Vacancy:
    """
    Класс для представления вакансии с валидацией данных и сравнением по зарплате.

    Атрибуты:
    - name: название вакансии
    - link: ссылка на вакансию
    - salary_from: минимальная зарплата
    - salary_to: максимальная зарплата
    - description: описание вакансии
    - area: город размещения
    - contact: контактные данные
    """

    __slots__ = (
        "name",  # Название вакансии
        "link",  # Ссылка на вакансию
        "salary_from",  # Зарплата от
        "salary_to",  # Зарплата до
        "description",  # Описание
        "area",  # Город
        "contact",  # Контактные данные
    )

    def __init__(self, name: str, link: str, salary: dict, description: str, area: str):
        """
        Инициализация объекта вакансии.

        :param name: название вакансии
        :param link: ссылка на вакансию
        :param salary: словарь с информацией о зарплате
        :param description: описание вакансии
        :param area: город размещения
        """
        self.name = name
        self.link = link
        self.description = description
        self.area = area
        self.__validate(salary)

    def __validate(self, salary: dict):
        """
        Проверяет зарплату и устанавливает значения по умолчанию,
        если зарплата отсутствует.

        :param salary: словарь с информацией о зарплате
        """
        try:
            self.salary_from = salary.get("from", 0) or 0
            self.salary_to = salary.get("to", 0) or 0
        except Exception as e:
            print(f"Ошибка валидации зарплаты: {e}")
            self.salary_from = 0
            self.salary_to = 0

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Сравнение вакансий по минимальной зарплате.

        :param other: объект вакансии для сравнения
        :return: True если зарплата меньше, иначе False
        """
        return self.salary_from < other.salary_from

    def __str__(self) -> str:
        """
        Возвращает вакансию в виде читаемой строки.

        :return: форматированная строка с данными вакансии
        """
        return (
            f"Название: {self.name}\n"
            f"Ссылка: {self.link}\n"
            f"Описание: {self.description}\n"
            f"Город: {self.area}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
            f"{'-' * 50}"
        )
