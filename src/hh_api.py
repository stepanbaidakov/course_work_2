from abc import ABC, abstractmethod
import requests


class HhAPI(ABC):
    """Класс для взаимодействия с API"""

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
    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    def _connect_to_api(self, url, params):
        return self.__connect_to_api(url, params)

    def __connect_to_api(self, url, params):
        response = requests.get(url, params)
        if response.status_code >= 400:
            response.raise_for_status()
        else:
            return response.json()

    def get_vacancies(self, keyword, per_page=100):
        self.__params['text'] = keyword
        self.__params["per_page"] = per_page
        while self.__params.get('page') != 1:
            response = self._connect_to_api(self.__url,self.__params)
            data = response["items"]
            self.__vacancies.extend(data)
            self.__params['page'] += 1
        return self.__vacancies


if __name__ == "__main__":
    hh = HhRu()
    vacancies = hh._connect_to_api("https://api.hh.ru/vacancies", {'text': 'Python', 'page': 0, 'per_page': 1})
    print(vacancies)
    # for vac in vacancies:
    #     print(vac)
        # if vac.get("salary") is None:
        #     print(0)
        # else:
        #     print(vac.get("salary").get("to"))
    # response = requests.get("https://api.hh.ru")
    # if response.status_code < 400:
    #     print("Возникла ошибка")
    # else:
    #     print(response)