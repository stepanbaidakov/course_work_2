from abc import ABC, abstractmethod
import requests


class HhAPI(ABC):
    """Базовый класс для взаимодействия с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def _connect_to_api(self, url, params):
        pass

    @abstractmethod
    def get_vacancies(self, key_word, per_page):
        pass


class HhRu(HhAPI):
    """Класс для взаимодействия с api"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def _connect_to_api(self, url: str, params: dict):
        """Метод подключения к api"""

        return self.__connect_to_api(url, params)

    def __connect_to_api(self, url: str, params: dict):
        response = requests.get(url, params)
        if response.status_code >= 400:
            return response.raise_for_status()
        else:
            return response.json()

    def get_vacancies(self, keyword: str, per_page: int =100) -> list[dict]:
        """Метод получения вакансий в виде списка словарей"""

        self.__params["text"] = keyword
        self.__params["per_page"] = per_page
        while self.__params.get("page") != 1:
            response = self._connect_to_api(self.__url, self.__params)
            data = response["items"]
            self.__vacancies.extend(data)
            self.__params["page"] += 1
        return self.__vacancies
