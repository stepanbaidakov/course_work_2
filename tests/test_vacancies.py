import pytest

from src.vacancies import Vacancy


def test_vacancy_init(vacancy_1):
    assert vacancy_1.name == "Стажер / Junior BI engenineer"
    assert vacancy_1.url == "https://api.hh.ru/vacancies/125828331?host=hh.ru"
    assert vacancy_1.salary == 0
    assert (
        vacancy_1.requirement
        == "Знание инструментов визуализации данных (например, Power BI, Qlik) будет преимуществом. - "
        "Владение языками программирования (например, <highlighttext>Python</highlighttext>, R) "
        "приветствуется. - Стремление учиться, адаптироваться..."
    )


def test_cast_to_object_salary_none():
    vacancies = [
        {
            "id": "125828331",
            "premium": False,
            "name": "Стажер / Junior BI engenineer",
            "department": None,
            "has_test": False,
            "response_letter_required": True,
            "area": {"id": "159", "name": "Астана", "url": "https://api.hh.ru/areas/159"},
            "salary": None,
            "salary_range": None,
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Нур-Султан (Астана)",
                "street": "проспект Кабанбай Батыра",
                "building": "49",
                "lat": 51.10289019613421,
                "lng": 71.40549623676974,
                "description": None,
                "raw": "Нур-Султан (Астана), проспект Кабанбай Батыра, 49",
                "metro": None,
                "metro_stations": [],
                "id": "2332192",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-09-26T09:49:32+0300",
            "created_at": "2025-09-26T09:49:32+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125828331",
            "show_logo_in_search": None,
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/125828331?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/125828331",
            "relations": [],
            "employer": {
                "id": "3751916",
                "name": "Geometry",
                "url": "https://api.hh.ru/employers/3751916",
                "alternate_url": "https://hh.ru/employer/3751916",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1023246.png",
                    "90": "https://img.hhcdn.ru/employer-logo/5713752.png",
                    "240": "https://img.hhcdn.ru/employer-logo/5713753.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3751916",
                "country_id": 3,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "знание инструментов визуализации данных (например, Power BI, Qlik) будет "
                "преимуществом. - Владение языками программирования "
                "(например, <highlighttext>Python</highlighttext>, R) "
                "приветствуется. - Стремление учиться, адаптироваться...",
                "responsibility": "3-недельное обучение (bootcamp): интенсивная программа с погружением в BI, "
                "практические кейсы и сопровождение менторов. 2-месячная проектная часть: "
                "участие...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "156", "name": "BI-аналитик, аналитик данных"}],
            "accept_incomplete_resumes": True,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": True,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]
    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Стажер / Junior BI engenineer"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/125828331?host=hh.ru"
    assert vacancies_list[0].salary == 0
    assert (
        vacancies_list[0].requirement
        == "знание инструментов визуализации данных (например, Power BI, Qlik) будет преимуществом. "
        "- Владение языками программирования (например, <highlighttext>Python</highlighttext>, R) "
        "приветствуется. - Стремление учиться, адаптироваться..."
    )


def test_cast_to_object_salary_usd():
    vacancies = [
        {
            "id": "126619317",
            "premium": False,
            "name": "Strong Middle Backend Engineer (Python)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2759", "name": "Ташкент", "url": "https://api.hh.ru/areas/2759"},
            "salary": {"from": 2500, "to": 3600, "currency": "USD", "gross": True},
            "salary_range": {
                "from": 2500,
                "to": 3600,
                "currency": "USD",
                "gross": True,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "MONTHLY", "name": "Раз в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-16T15:37:41+0300",
            "created_at": "2025-10-16T15:37:41+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126619317",
            "show_logo_in_search": None,
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126619317?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126619317",
            "relations": [],
            "employer": {
                "id": "9554799",
                "name": "Super Dispatch (ООО Software Transport)",
                "url": "https://api.hh.ru/employers/9554799",
                "alternate_url": "https://hh.ru/employer/9554799",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1055110.jpeg",
                    "90": "https://img.hhcdn.ru/employer-logo/5841081.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo/5841082.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=9554799",
                "country_id": 6,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "...one <highlighttext>Python</highlighttext> web framework, such as "
                "Django, FastApi, etc. and willing to build and maintain services in different "
                "<highlighttext>Python</highlighttext> web...",
                "responsibility": "Work closely with your team (design, engineering, product, analytics) to "
                "figure out and deliver innovative solutions that will drive your...",
            },
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "fly_in_fly_out_duration": [],
            "work_format": [
                {"id": "REMOTE", "name": "Удалённо"},
                {"id": "HYBRID", "name": "Гибрид"},
                {"id": "FIELD_WORK", "name": "Разъездной"},
            ],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]
    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Strong Middle Backend Engineer (Python)"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126619317?host=hh.ru"
    assert vacancies_list[0].salary == 298800
    assert (
        vacancies_list[0].requirement
        == "...one <highlighttext>Python</highlighttext> web framework, such as Django, FastApi, etc. and "
        "willing to build and maintain services in different <highlighttext>Python</highlighttext> web..."
    )


def test_cast_to_object_salary_kzt():
    vacancies = [
        {
            "id": "126599052",
            "premium": False,
            "name": "Backend - разработчик",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "159", "name": "Астана", "url": "https://api.hh.ru/areas/159"},
            "salary": {"from": 500000, "to": 1000000, "currency": "KZT", "gross": False},
            "salary_range": {
                "from": 500000,
                "to": 1000000,
                "currency": "KZT",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": None,
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Астана",
                "street": "улица Достык",
                "building": "16",
                "lat": 51.124736,
                "lng": 71.432082,
                "description": None,
                "raw": "Астана, улица Достык, 16",
                "metro": None,
                "metro_stations": [],
                "id": "14764405",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-16T10:20:18+0300",
            "created_at": "2025-10-16T10:20:18+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126599052",
            "show_logo_in_search": None,
            "show_contacts": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126599052?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126599052",
            "relations": [],
            "employer": {
                "id": "10584232",
                "name": "DLS-Global KZ",
                "url": "https://api.hh.ru/employers/10584232",
                "alternate_url": "https://hh.ru/employer/10584232",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1281717.jpg",
                    "90": "https://img.hhcdn.ru/employer-logo/6747166.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo/6747167.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10584232",
                "country_id": 3,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "3+ года коммерческой разработки на <highlighttext>Python</highlighttext> (Django). "
                "Опыт проектирования и реализации нового функционала, REST API и интеграций "
                "с внешними...",
                "responsibility": "Разработка нового функционала и сервисов на "
                "<highlighttext>Python</highlighttext>/Django с “нуля” до продакшена. "
                "Разработка, документирование и отладка REST API для мобильных...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": True,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Backend - разработчик"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126599052?host=hh.ru"
    assert vacancies_list[0].salary == 150000
    assert (
        vacancies_list[0].requirement
        == "3+ года коммерческой разработки на <highlighttext>Python</highlighttext> (Django). Опыт "
        "проектирования и реализации нового функционала, REST API и интеграций с внешними..."
    )


def test_cast_to_object_salary_rur_to():
    vacancies = [
        {
            "id": "126509779",
            "premium": False,
            "name": "Python Backend разработчик",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "76", "name": "Ростов-на-Дону", "url": "https://api.hh.ru/areas/76"},
            "salary": {"from": 80000, "to": 130000, "currency": "RUR", "gross": True},
            "salary_range": {
                "from": 80000,
                "to": 130000,
                "currency": "RUR",
                "gross": True,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "TWICE_PER_MONTH", "name": "Два раза в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Ростов-на-Дону",
                "street": "Будённовский проспект",
                "building": "97",
                "lat": 47.23305,
                "lng": 39.701448,
                "description": None,
                "raw": "Ростов-на-Дону, Будённовский проспект, 97",
                "metro": None,
                "metro_stations": [],
                "id": "3718227",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-14T11:29:06+0300",
            "created_at": "2025-10-14T11:29:06+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126509779",
            "show_logo_in_search": None,
            "show_contacts": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126509779?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126509779",
            "relations": [],
            "employer": {
                "id": "2156615",
                "name": "Научно-производственный центр Космос-2",
                "url": "https://api.hh.ru/employers/2156615",
                "alternate_url": "https://hh.ru/employer/2156615",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original-round/4158334.jpg",
                    "90": "https://img.hhcdn.ru/employer-logo-round/4158336.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo-round/4158337.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=2156615",
                "country_id": 1,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Высшее техническое образование (незаконченное высшее). Знание "
                "<highlighttext>Python</highlighttext>,FastAPI, Django, DRF‚ PostgreSQL, redis, "
                "Docker. Уверенная работа с git. От 1 года...",
                "responsibility": "Разработка, развитие продуктов компании, разработка документации.",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "HYBRID", "name": "Гибрид"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Python Backend разработчик"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126509779?host=hh.ru"
    assert vacancies_list[0].salary == 130000
    assert (
        vacancies_list[0].requirement == "Высшее техническое образование (незаконченное высшее). Знание "
        "<highlighttext>Python</highlighttext>,FastAPI, Django, DRF‚ PostgreSQL, redis, Docker. "
        "Уверенная работа с git. От 1 года..."
    )


def test_cast_to_object_salary_kgs():
    vacancies = [
        {
            "id": "126362243",
            "premium": False,
            "name": "Junior Python Developer",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2760", "name": "Бишкек", "url": "https://api.hh.ru/areas/2760"},
            "salary": {"from": 30000, "to": 45000, "currency": "KGS", "gross": True},
            "salary_range": {
                "from": 30000,
                "to": 45000,
                "currency": "KGS",
                "gross": True,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": None,
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Бишкек",
                "street": "улица Горького",
                "building": "70",
                "lat": 42.856463,
                "lng": 74.617409,
                "description": None,
                "raw": "Бишкек, улица Горького, 70",
                "metro": None,
                "metro_stations": [],
                "id": "18515881",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-09T14:15:07+0300",
            "created_at": "2025-10-09T14:15:07+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126362243",
            "show_contacts": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126362243?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126362243",
            "relations": [],
            "employer": {
                "id": "11684430",
                "name": "ОсОО ИТК Кэй Джи",
                "url": "https://api.hh.ru/employers/11684430",
                "alternate_url": "https://hh.ru/employer/11684430",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=11684430",
                "country_id": 7,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "опыт работы в разработке от 1 года. - Знание "
                "<highlighttext>Python</highlighttext> и соответствующих фреймворков. - "
                "Знакомство с системами контроля версий ( Git GitHub/GitLab). - ",
                "responsibility": "Основы тестирования и отладки.",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Junior Python Developer"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126362243?host=hh.ru"
    assert vacancies_list[0].salary == 41400
    assert (
        vacancies_list[0].requirement
        == "опыт работы в разработке от 1 года. - Знание <highlighttext>Python</highlighttext> и "
        "соответствующих фреймворков. - Знакомство с системами контроля версий ( Git GitHub/GitLab). - "
    )


def test_cast_to_object_salary_byr():
    vacancies = [
        {
            "id": "125602176",
            "premium": False,
            "name": "Стажер-разработчик (Python)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1002", "name": "Минск", "url": "https://api.hh.ru/areas/1002"},
            "salary": {"from": 2300, "to": None, "currency": "BYR", "gross": True},
            "salary_range": {
                "from": 2300,
                "to": None,
                "currency": "BYR",
                "gross": True,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": {"id": "TWICE_PER_MONTH", "name": "Два раза в\xa0месяц"},
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Минск",
                "street": "улица Куйбышева",
                "building": "35",
                "lat": 53.914022,
                "lng": 27.568092,
                "description": None,
                "raw": "Минск, улица Куйбышева, 35",
                "metro": {
                    "station_name": "Немига",
                    "line_name": "Автозаводская",
                    "station_id": "63.422",
                    "line_id": "63",
                    "lat": 53.905615,
                    "lng": 27.55415,
                },
                "metro_stations": [
                    {
                        "station_name": "Немига",
                        "line_name": "Автозаводская",
                        "station_id": "63.422",
                        "line_id": "63",
                        "lat": 53.905615,
                        "lng": 27.55415,
                    },
                    {
                        "station_name": "Октябрьская",
                        "line_name": "Московская",
                        "station_id": "62.410",
                        "line_id": "62",
                        "lat": 53.901562,
                        "lng": 27.561068,
                    },
                    {
                        "station_name": "Площадь Победы",
                        "line_name": "Московская",
                        "station_id": "62.409",
                        "line_id": "62",
                        "lat": 53.908644,
                        "lng": 27.575054,
                    },
                    {
                        "station_name": "Площадь Якуба Коласа",
                        "line_name": "Московская",
                        "station_id": "62.408",
                        "line_id": "62",
                        "lat": 53.915369,
                        "lng": 27.583265,
                    },
                ],
                "id": "19640009",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-09-22T12:33:51+0300",
            "created_at": "2025-09-22T12:33:51+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=125602176",
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/125602176?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/125602176",
            "relations": [],
            "employer": {
                "id": "12293242",
                "name": "Технологии пользовательских интерфейсов",
                "url": "https://api.hh.ru/employers/12293242",
                "alternate_url": "https://hh.ru/employer/12293242",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=12293242",
                "country_id": 4,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "<highlighttext>Python</highlighttext>. Django, DRF, SQL, CSS, HTML. Желателен "
                "опыт работы.",
                "responsibility": "Разработка приложений. Сайтов, систем автоматизации, работа с базами данных.",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": True,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Стажер-разработчик (Python)"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/125602176?host=hh.ru"
    assert vacancies_list[0].salary == 57500
    assert (
        vacancies_list[0].requirement
        == "<highlighttext>Python</highlighttext>. Django, DRF, SQL, CSS, HTML. Желателен опыт работы."
    )


def test_cast_to_object_salary_uzs():
    vacancies = [
        {
            "id": "126364821",
            "premium": False,
            "name": "Middle/Middle+ backend developer (python)",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "2759", "name": "Ташкент", "url": "https://api.hh.ru/areas/2759"},
            "salary": {"from": 15000000, "to": 20000000, "currency": "UZS", "gross": False},
            "salary_range": {
                "from": 15000000,
                "to": 20000000,
                "currency": "UZS",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": None,
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Ташкент",
                "street": "улица Бахор",
                "building": "16",
                "lat": 41.333336,
                "lng": 69.267933,
                "description": None,
                "raw": "Ташкент, улица Бахор, 16",
                "metro": None,
                "metro_stations": [],
                "id": "13702912",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-09T14:58:07+0300",
            "created_at": "2025-10-09T14:58:07+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126364821",
            "show_logo_in_search": None,
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126364821?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126364821",
            "relations": [],
            "employer": {
                "id": "10027405",
                "name": "Aros (Яратов Жавадбек Васил угли)",
                "url": "https://api.hh.ru/employers/10027405",
                "alternate_url": "https://hh.ru/employer/10027405",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/1136181.jpg",
                    "90": "https://img.hhcdn.ru/employer-logo/6165309.jpeg",
                    "240": "https://img.hhcdn.ru/employer-logo/6165310.jpeg",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=10027405",
                "country_id": 6,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Proven Experience: Minimum 3+ years in <highlighttext>Python</highlighttext> "
                "web development. Fework Expertise: Strong experience with Django (>=5.1.1) and...",
                "responsibility": "Design, develop, and maintain backend services and APIs using Django "
                "and Flask. Integrate third-party services including AWS (Boto3...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "ON_SITE", "name": "На\xa0месте работодателя"}],
            "working_hours": [{"id": "HOURS_9", "name": "9 часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "Middle/Middle+ backend developer (python)"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126364821?host=hh.ru"
    assert vacancies_list[0].salary == 132000
    assert (
        vacancies_list[0].requirement
        == "Proven Experience: Minimum 3+ years in <highlighttext>Python</highlighttext> web "
        "development. Fework Expertise: Strong experience with Django (>=5.1.1) and..."
    )


def test_cast_to_object_rur_from():
    vacancies = [
        {
            "id": "126538654",
            "premium": False,
            "name": "QA manual junoir",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 70000, "to": None, "currency": "RUR", "gross": False},
            "salary_range": {
                "from": 70000,
                "to": None,
                "currency": "RUR",
                "gross": False,
                "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                "frequency": None,
            },
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2025-10-15T00:15:55+0300",
            "created_at": "2025-10-15T00:15:55+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126538654",
            "show_contacts": False,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/126538654?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/126538654",
            "relations": [],
            "employer": {
                "id": "12321365",
                "name": "Ландия",
                "url": "https://api.hh.ru/employers/12321365",
                "alternate_url": "https://hh.ru/employer/12321365",
                "logo_urls": None,
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=12321365",
                "country_id": 1,
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Знание техник тест-дизайна. - Опыт в автоматизации "
                "(<highlighttext>Python</highlighttext> / Java / JavaScript + Selenium, "
                "Playwright, Cypress). - Понимание CI/CD (Jenkins, GitLab CI).",
                "responsibility": "Функциональное, регрессионное, smoke- и UI-тестирование. - Работа с API "
                "(Postman, SoapUI или аналоги). - Анализ требований и написание тестовой "
                "документации (чек...",
            },
            "contacts": None,
            "schedule": {"id": "remote", "name": "Удаленная работа"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": True,
            "fly_in_fly_out_duration": [],
            "work_format": [{"id": "REMOTE", "name": "Удалённо"}],
            "working_hours": [{"id": "HOURS_8", "name": "8\xa0часов"}],
            "work_schedule_by_days": [{"id": "FIVE_ON_TWO_OFF", "name": "5/2"}],
            "night_shifts": False,
            "professional_roles": [{"id": "40", "name": "Другое"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "employment_form": {"id": "FULL", "name": "Полная"},
            "internship": False,
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    ]

    vacancies_list = [Vacancy.cast_to_object_list(vacancy) for vacancy in vacancies]

    assert vacancies_list[0].name == "QA manual junoir"
    assert vacancies_list[0].url == "https://api.hh.ru/vacancies/126538654?host=hh.ru"
    assert vacancies_list[0].salary == 70000
    assert (
        vacancies_list[0].requirement
        == "Знание техник тест-дизайна. - Опыт в автоматизации (<highlighttext>Python</highlighttext> / Java / "
        "JavaScript + Selenium, Playwright, Cypress). - Понимание CI/CD (Jenkins, GitLab CI)."
    )


def test_lt_correct(vacancy_1, vacancy_2):
    assert vacancy_1 < vacancy_2


def test_lt_false(vacancy_1, vacancy_2):
    with pytest.raises(AssertionError):
        assert vacancy_2 < vacancy_1


def test_gt_correct(vacancy_1, vacancy_2):
    assert vacancy_2 > vacancy_1


def test_gt_false(vacancy_1, vacancy_2):
    with pytest.raises(AssertionError):
        assert vacancy_1 > vacancy_2


def test_to_json(vacancy_1):
    assert vacancy_1.to_json() == {
        "name": "Стажер / Junior BI engenineer",
        "url": "https://api.hh.ru/vacancies/125828331?host=hh.ru",
        "salary": 0,
        "requirements": "Знание инструментов визуализации данных (например, Power BI, Qlik) будет "
        "преимуществом. - Владение языками программирования (например, "
        "<highlighttext>Python</highlighttext>, R) приветствуется. - "
        "Стремление учиться, адаптироваться...",
    }
