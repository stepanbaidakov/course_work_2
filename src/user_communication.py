from src.vacancies import Vacancy


def sort_vacancies(vacancies_list):
    """Функция для сортировки вакансий"""

    sorted_vacancies = sorted(vacancies_list, key=lambda x: x.salary, reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies_list: list[dict], top_n: int) -> list[dict]:
    """Функция для получения топ n вакансий"""

    return vacancies_list[:top_n]


def filter_vacancies(vacancies_list: list[dict[Vacancy]], filter_words: list) -> list[dict[Vacancy]]:
    """Функция фильтрации вакансий"""

    filtered_list = []
    for vacancy in vacancies_list:
        for filter_word in filter_words:
            if vacancy.requirement is not None:
                if filter_word in vacancy.requirement and vacancy not in filtered_list:
                    filtered_list.append(vacancy)
            # else:
            #     continue
    return filtered_list
