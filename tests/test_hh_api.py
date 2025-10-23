from unittest.mock import Mock, patch


@patch("requests.get")
def test_connect_to_api(mock_get, hh_ru):
    mock_response = Mock()
    mock_response.json.return_value = {
        "items": [
            {
                "id": "126400719",
                "premium": False,
                "name": "Мобильный frontend разработчик Kotlin Multiplatform",
                "department": None,
                "has_test": False,
                "response_letter_required": False,
                "area": {"id": "159", "name": "Астана", "url": "https://api.hh.ru/areas/159"},
                "salary": {"from": 200000, "to": 500000, "currency": "KZT", "gross": True},
                "salary_range": {
                    "from": 200000,
                    "to": 500000,
                    "currency": "KZT",
                    "gross": True,
                    "mode": {"id": "MONTH", "name": "За\xa0месяц"},
                    "frequency": {"id": "MONTHLY", "name": "Раз в\xa0месяц"},
                },
                "type": {"id": "open", "name": "Открытая"},
                "address": {
                    "city": "Астана",
                    "street": "улица Сакена Сейфуллина",
                    "building": "3",
                    "lat": 51.169396,
                    "lng": 71.400991,
                    "description": None,
                    "raw": "Астана, улица Сакена Сейфуллина, 3",
                    "metro": None,
                    "metro_stations": [],
                    "id": "2182466",
                },
                "response_url": None,
                "sort_point_distance": None,
                "published_at": "2025-10-10T12:51:35+0300",
                "created_at": "2025-10-10T12:51:35+0300",
                "archived": False,
                "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=126400719",
                "show_logo_in_search": None,
                "show_contacts": True,
                "insider_interview": None,
                "url": "https://api.hh.ru/vacancies/126400719?host=hh.ru",
                "alternate_url": "https://hh.ru/vacancy/126400719",
                "relations": [],
                "employer": {
                    "id": "1903100",
                    "name": "AST Group Capital",
                    "url": "https://api.hh.ru/employers/1903100",
                    "alternate_url": "https://hh.ru/employer/1903100",
                    "logo_urls": {
                        "original": "https://img.hhcdn.ru/employer-logo-original/399709.jpg",
                        "90": "https://img.hhcdn.ru/employer-logo/2040914.jpeg",
                        "240": "https://img.hhcdn.ru/employer-logo/2040915.jpeg",
                    },
                    "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1903100",
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "Опыт разработки на Kotlin от 1–2 лет, желательно с практикой в Kotlin "
                    "Multiplatform (KMP). Знание Jetpack Compose / Compose Multiplatform. ",
                    "responsibility": "Разработка и поддержка кроссплатформенных пользовательских интерфейсов с "
                    "использованием Kotlin Multiplatform и Jetpack Compose Multiplatform. Интеграция фронтенда "
                    "с backend API и...",
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
                "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
                "employment": {"id": "full", "name": "Полная занятость"},
                "employment_form": {"id": "FULL", "name": "Полная"},
                "internship": True,
                "adv_response_url": None,
                "is_adv_vacancy": False,
                "adv_context": None,
            },
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
                    "accredited_it_employer": False,
                    "trusted": True,
                },
                "snippet": {
                    "requirement": "знание инструментов визуализации данных (например, Power BI, Qlik) будет "
                    "преимуществом. - Владение языками программирования (например, "
                    "<highlighttext>Python</highlighttext>, R) приветствуется. - Стремление учиться, "
                                   "адаптироваться...",
                    "responsibility": "3-недельное обучение (bootcamp): интенсивная программа с погружением в BI, "
                    "практические кейсы и сопровождение менторов. 2-месячная проектная часть: участие...",
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
            },
        ],
        "found": 9016,
        "pages": 1000,
        "page": 0,
        "per_page": 2,
        "clusters": None,
        "arguments": None,
        "fixes": None,
        "suggests": None,
        "alternate_url": "https://hh.ru/search/vacancy?enable_snippets=true&items_on_page=2&text=Python",
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    result = hh_ru._connect_to_api("https://api.hh.ru/vacancies", {"text": "Python", "page": 0, "per_page": 1})
    assert result == mock_response.json.return_value
    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", {"text": "Python", "page": 0, "per_page": 1})


@patch("requests.get")
def test_connect_to_api_bad_answer(mock_get, hh_ru):
    mock_response = Mock()
    mock_response.status_code = 400

    mock_get.return_value = mock_response
    hh_ru._connect_to_api("https://api.hh.ru/vacancies", {"text": "Python", "page": 0, "per_page": 1})
    mock_response.raise_for_status.assert_called_once()
    mock_get.assert_called_once_with("https://api.hh.ru/vacancies", {"text": "Python", "page": 0, "per_page": 1})


@patch("requests.get")
def test_get_vacancies(mock_get, hh_ru):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [
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
                    "requirement": "знание инструментов визуализации данных (например, Power BI, Qlik) "
                    "будет преимуществом. - Владение языками программирования (например, "
                    "<highlighttext>Python</highlighttext>, R) приветствуется. - Стремление учиться, "
                                   "адаптироваться...",
                    "responsibility": "3-недельное обучение (bootcamp): интенсивная программа с погружением в BI, "
                    "практические кейсы и сопровождение менторов. 2-месячная проектная часть: участие...",
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
        ],
        "found": 8964,
        "pages": 2000,
        "page": 0,
        "per_page": 1,
        "clusters": None,
        "arguments": None,
        "fixes": None,
        "suggests": None,
        "alternate_url": "https://hh.ru/search/vacancy?enable_snippets=true&items_on_page=1&text=Python",
    }
    mock_get.return_value = mock_response
    result = hh_ru.get_vacancies("Python", 1)
    assert result == [
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
                "requirement": "знание инструментов визуализации данных (например, Power BI, Qlik) "
                "будет преимуществом. - Владение языками программирования (например, "
                "<highlighttext>Python</highlighttext>, R) приветствуется. - Стремление учиться, адаптироваться...",
                "responsibility": "3-недельное обучение (bootcamp): интенсивная программа с погружением в BI, "
                "практические кейсы и сопровождение менторов. 2-месячная проектная часть: участие...",
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
