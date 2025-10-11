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
    def cast_to_object_list(cls, vacancies_dict):
        if vacancies_dict.get("salary") is None:
            return cls(vacancies_dict.get("name"), vacancies_dict.get("url"), vacancies_dict.get("salary"),
                       vacancies_dict.get("snippet").get("requirement"))

        elif vacancies_dict.get("salary").get("to") is not None and vacancies_dict.get("salary").get("currency") == "BYR":
            return cls(vacancies_dict.get("name"), vacancies_dict.get("url"),
                       vacancies_dict.get("salary").get("to") * 25,
                       # print(vacancies_dict.get("salary")),
                       vacancies_dict.get("snippet").get("requirement"))

        elif vacancies_dict.get("salary").get("to") is not None and vacancies_dict.get("salary").get("currency") == "USD":
            return cls(vacancies_dict.get("name"), vacancies_dict.get("url"),
                       vacancies_dict.get("salary").get("to") * 83,
                       vacancies_dict.get("snippet").get("requirement"))

        elif vacancies_dict.get("salary").get("to") is not None and vacancies_dict.get("salary").get("currency") == "KZT":
            return cls(vacancies_dict.get("name"), vacancies_dict.get("url"),
                       vacancies_dict.get("salary").get("to") * 0.15,
                       vacancies_dict.get("snippet").get("requirement"))
        else:
            return cls(vacancies_dict.get("name"), vacancies_dict.get("url"), vacancies_dict.get("salary").get("to"),
                       vacancies_dict.get("snippet").get("requirement"))

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary < other.salary

    def __gt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary > other.salary

    def to_json(self):
        return {
        "name": self.name,
        "url": self.url,
        "salary": self.salary,
        "requirements": self.requirement
        }



if __name__ == "__main__":
    from hh_api import HhRu

    hh_ru = HhRu()
    vacs = hh_ru.get_vacancies("Python", )

    vac = [Vacancy.cast_to_object_list(v) for v in vacs]
    print()
    for i in vac:
        print(i.salary)
    # littler = vac[0] > vac[1]
    # print(littler)
    # print(vac[2].to_json())

