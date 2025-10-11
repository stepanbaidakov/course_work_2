import json
import os.path
from abc import ABC, abstractmethod

from config import DATA_DIR

class BaseJSONSaver(ABC):

    @abstractmethod
    def add_vacancies(self, vacancies):
        pass

    @abstractmethod
    def load_vacancies(self, url):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(BaseJSONSaver):

    file_name: str

    def __init__(self, file_name="vacancies.json"):
        self.__file_name = file_name

    def add_vacancies(self, vacancies):

        try:
            with open(os.path.join(DATA_DIR, self.__file_name), "r", encoding="utf-8") as f:
                data = json.load(f)  # читаем уже существующие
        except json.decoder.JSONDecodeError:
            data = []
        except FileNotFoundError:
            data = []
        for vacancy in vacancies:
            if vacancy not in data:
                data.append(vacancy)

        with open(os.path.join(DATA_DIR, self.__file_name), "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_vacancies(self, url):
        with open(os.path.join(DATA_DIR, self.__file_name), "r", encoding="utf-8") as file:
           data = json.load(file)
        result = []
        for vacancy in data:
            if url in vacancy["url"]:
                result.append(vacancy)
        return result

    def delete_vacancies(self):
        with open(os.path.join(DATA_DIR, self.__file_name), "w"):
            pass

if __name__ == "__main__":

    fw = JSONSaver("vacancies.json")
    fw.add_vacancies([{'name': 'Инженер по тестированию', 'url': 'https://api.hh.ru/vacancies/126274858?host=hh.ru', 'salary': 0, 'requirements': 'Опыт работы с автотестами, в том числе написание и внедрение. Базовые знания bash, <highlighttext>python</highlighttext>. Базовые навыки работы с измерительным инструментов...'}
])

    print(fw.load_vacancies("https://api.hh.ru/vacancies/126274858?host=hh.ru"))
    # fw.delete_vacancies()
