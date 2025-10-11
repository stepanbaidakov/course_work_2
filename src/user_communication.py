from src.vacancies import Vacancy


def sort_vacancies(vacancies_list):
    sorted_vacancies = sorted(vacancies_list, key=lambda x: x.salary, reverse=True)
    return sorted_vacancies

def get_top_vacancies(vacancies_list:list[dict], top_n: str) -> list[dict]:
    return vacancies_list[:top_n]

def filter_vacancies(vacancies_list: list[dict[Vacancy]], filter_words: list) -> list[dict]:
    filtered_list = []
    for vacancy in vacancies_list:
        for filter_word in filter_words:
            if vacancy.requirement is not None:
                if filter_word in vacancy.requirement:
                    filtered_list.append(vacancy)
            else:
                continue
    return filtered_list


if __name__ == "__main__":
    from hh_api import HhRu
    from vacancies import Vacancy

    search_query = "Python"
    top_n = 10
    filter_words = "знания".split(",")

    hh_api = HhRu()
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = [Vacancy.cast_to_object_list(v) for v in hh_vacancies]
    filtered_list_vac = filter_vacancies(vacancies_list, filter_words)
    # filter_words = "знания".split(",")
    print(filter_words)
    fil = filter_vacancies(vacancies_list, filter_words)
    for fi in fil:
        print(fi)

