from src.hh_api import HhRu
from src.vacancies import Vacancy
from src.user_communication import get_top_vacancies, filter_vacancies
from src.file_worker import JSONSaver


def main():
    """Функция взаимодействия с пользователем"""

    search_query = input("Введите запрос по профессии: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    all_filter_words = input("Введите слова для фильтрации вакансий со строчной буквы: ").split(",")

    filter_words_1 = "знания".split(",")
    all_filter_words.extend(filter_words_1)
    for filter_word in filter_words_1:
        filter_word_2 = filter_word.title()
        all_filter_words.append(filter_word_2)

    hh_api = HhRu()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy.cast_to_object_list(v) for v in hh_vacancies]
    filtered_list = filter_vacancies(vacancies_list, all_filter_words)
    top_vacancies = get_top_vacancies(filtered_list, top_n)

    final_list = []
    for vacancy in top_vacancies:
        print(vacancy.to_json())
        final_list.append(vacancy.to_json())

    file_saver = JSONSaver()
    file_saver.add_vacancies_to_file(final_list)

    get_vacancies_input = input("Хотите получить вакансии из файла. Да/Нет: ").lower()
    if get_vacancies_input == "да":
        urls_input = input("Введите ссылку на вакансию, которую Вы ищете: ").split(", ")
        got_vacancies = file_saver.get_vacancies_from_file(urls_input)
        print(got_vacancies)
    else:
        pass


if __name__ == "__main__":
    main()
