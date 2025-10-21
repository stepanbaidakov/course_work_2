class Vacancy:
    """Класс для работы с вакансиями"""

    name: str
    url: str
    salary: str
    requirement: str

    __slots__ = ("name", "url", "salary", "requirement")

    def __init__(self, name, url, salary, requirement):
        validated_salary = self.__validate_salary(salary)

        self.name = name
        self.url = url
        self.salary = validated_salary
        self.requirement = requirement

    def __validate_salary(self, salary):
        if salary is None:
            salary = 0
        return salary

    @classmethod
    def cast_to_object_list(cls, vacancies_dict: dict):
        if vacancies_dict.get("salary") is None:
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary"),
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif (
            vacancies_dict.get("salary").get("from") is not None
            and vacancies_dict.get("salary").get("currency") == "BYR"
        ):
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("from") * 25,
                # print(vacancies_dict.get("salary")),
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif (
            vacancies_dict.get("salary").get("to") is not None
            and vacancies_dict.get("salary").get("currency") == "USD"
        ):
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("to") * 83,
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif (
            vacancies_dict.get("salary").get("to") is not None
            and vacancies_dict.get("salary").get("currency") == "KZT"
        ):
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("to") * 0.15,
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif (
            vacancies_dict.get("salary").get("to") is not None
            and vacancies_dict.get("salary").get("currency") == "UZS"
        ):
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("to") * 0.0066,
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif (
            vacancies_dict.get("salary").get("to") is not None
            and vacancies_dict.get("salary").get("currency") == "KGS"
        ):
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("to") * 0.92,
                vacancies_dict.get("snippet").get("requirement"),
            )

        elif vacancies_dict.get("salary").get("to") is None and vacancies_dict.get("salary").get("currency") == "RUR":
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("from"),
                vacancies_dict.get("snippet").get("requirement"),
            )
        else:
            return cls(
                vacancies_dict.get("name"),
                vacancies_dict.get("url"),
                vacancies_dict.get("salary").get("to"),
                vacancies_dict.get("snippet").get("requirement"),
            )

    def __lt__(self, other) -> int:
        if isinstance(other, Vacancy):
            return self.salary < other.salary

    def __gt__(self, other) -> int:
        if isinstance(other, Vacancy):
            return self.salary > other.salary

    def to_json(self) -> dict:
        return {"name": self.name, "url": self.url, "salary": self.salary, "requirements": self.requirement}
