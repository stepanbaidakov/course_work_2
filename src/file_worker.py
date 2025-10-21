import json
import os.path
from abc import ABC, abstractmethod

from config import DATA_DIR


class BaseJSONSaver(ABC):
    """Базовый класс для взаимодействия с api"""

    @abstractmethod
    def add_vacancies_to_file(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies_from_file(self, url):
        pass

    @abstractmethod
    def delete_vacancies(self):
        pass


class JSONSaver(BaseJSONSaver):
    """Класс для работы с файлом"""

    file_name: str

    def __init__(self, file_name: str ="vacancies.json"):
        self.__file_name = file_name

    def add_vacancies_to_file(self, vacancies: list):

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

    def get_vacancies_from_file(self, urls: list) -> list:
        with open(os.path.join(DATA_DIR, self.__file_name), "r", encoding="utf-8") as file:
            data = json.load(file)
        result = []
        for vacancy in data:
            for url in urls:
                if url in vacancy["url"]:
                    result.append(vacancy)
        return result

    def delete_vacancies(self):
        with open(os.path.join(DATA_DIR, self.__file_name), "w"):
            pass
