import os.path
import json

from config import DATA_DIR
from src.file_worker import JSONSaver


def test_jsonsaver_init():
    file_worker = JSONSaver("new_vacancies.json")
    assert file_worker._JSONSaver__file_name == "new_vacancies.json"


def test_add_vacancies():
    file_worker = JSONSaver()
    vacancies = [
        {
            "name": "Инженер по тестированию",
            "url": "https://api.hh.ru/vacancies/126274858?host=hh.ru",
            "salary": 0,
            "requirements": "Опыт работы с автотестами, в том числе написание и внедрение. "
                            "Базовые знания bash, <highlighttext>python</highlighttext>. Базовые навыки "
                            "работы с измерительным инструментов...",
        }
    ]
    file_worker.delete_vacancies()
    file_worker.add_vacancies_to_file(vacancies)
    report_path = os.path.join(DATA_DIR, "vacancies.json")

    with open(report_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert vacancies[0] in data


def test_add_vacancies_new_file():
    report_file = os.path.join(DATA_DIR, "new_vacancies.json")
    file_worker = JSONSaver(report_file)
    vacancies = [
        {
            "name": "Инженер по тестированию",
            "url": "https://api.hh.ru/vacancies/126274858?host=hh.ru",
            "salary": 0,
            "requirements": "Опыт работы с автотестами, в том числе написание и внедрение. Базовые знания bash, "
                            "<highlighttext>python</highlighttext>. Базовые навыки работы с измерительным "
                            "инструментов...",
        }
    ]

    file_worker.add_vacancies_to_file(vacancies)

    with open(report_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    assert len(data) == 1
    assert vacancies[0] in data
    os.remove(report_file)


def test_get_vacancies_from_file():
    file_worker = JSONSaver()
    url = "https://api.hh.ru/vacancies/126274858?host=hh.ru"
    founded_vacancy = file_worker.get_vacancies_from_file(url)

    assert founded_vacancy[0]["url"] == url


def test_delete_vacancies():
    file_worker = JSONSaver()
    file_worker.delete_vacancies()
    report_path = os.path.join(DATA_DIR, "vacancies.json")

    with open(report_path, "r", encoding="utf-8") as file:
        data = file.read()
    assert data == ""
