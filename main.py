from src.hh_api import HhRu
from src.vacancies import Vacancy
from src.user_communication import get_top_vacancies, filter_vacancies
from src.file_worker import JSONSaver

def main():
    # search_query = input("Введите запрос по профессии: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите слова для фильтрации вакансий: ").split(",")
    search_query = "Python"
    top_n = 2
    filter_words = "знания".split(",")

    hh_api = HhRu()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy.cast_to_object_list(v) for v in hh_vacancies]
    filtered_list = filter_vacancies(vacancies_list, filter_words)
    top_vacancies = get_top_vacancies(filtered_list, top_n)

    final_list = []
    for vacancy in top_vacancies:
        print(vacancy.to_json())
        final_list.append(vacancy.to_json())

    file_saver = JSONSaver()
    file_saver.add_vacancies(final_list)


if __name__ == "__main__":
    main()