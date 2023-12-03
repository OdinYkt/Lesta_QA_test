import pytest
import requests
import re
import typing
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class ProgrammingLanguage:
    website: str
    popularity: str
    frontend: str
    backend: str
    database: str
    notes: str


def clear_from_references(s):
    return re.sub(r'\[\d+\]', '', s)


def format_popularity(popularity: str) -> str:
    """Преобразовать строку популярности в число"""
    pattern = r'\d{1,3}([.,]\d{3})*'    # Не нашёл лучше способа универсально доставать число
    only_popularity = re.match(pattern, popularity).group()
    return only_popularity.replace('.', '').replace(',', '')


def fetch_programming_languages_data(url: str) -> typing.Optional[list[ProgrammingLanguage]]:
    """Получение данных таблицы"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find('table', {'class': 'wikitable'})
        rows = table.find_all('tr')[1:]

        languages_data = []
        for row in rows:
            columns = row.find_all(['th', 'td'])
            website = clear_from_references(columns[0].get_text(strip=True))
            popularity = format_popularity(
                clear_from_references(columns[1].get_text(strip=True))
            )
            frontend = clear_from_references(columns[2].get_text(strip=True))
            backend = clear_from_references(columns[3].get_text(strip=True))
            database = clear_from_references(columns[4].get_text(strip=True))
            notes = clear_from_references(columns[5].get_text(strip=True))

            languages_data.append(ProgrammingLanguage(website,
                                                      popularity,
                                                      frontend,
                                                      backend,
                                                      database,
                                                      notes,
                                                      )
                                  )

        return languages_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None



@pytest.mark.parametrize("expected_popularity",
                         [10 ** 7, 1.5 * 10 ** 7, 5 * 10 ** 7, 10 ** 8, 5 * 10 ** 8, 10 ** 9, 1.5 * 10 ** 9])
def test_popularity_check(expected_popularity):
    wikipedia_url = r"https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    languages_data = fetch_programming_languages_data(wikipedia_url)

    if languages_data:
        errors = []
        for language in languages_data:
            if int(language.popularity) < expected_popularity:
                error_message = (
                    f"{language.website} (Frontend:{language.frontend}|Backend:{language.backend}) "
                    f"has {int(language.popularity):,.0f} unique visitors per month. "
                    f"(Expected more than {expected_popularity:,.0f})".replace(',', ' ')
                )
                errors.append(error_message)

        assert not errors, "\n".join(errors)
    else:
        assert False, "Failed to fetch programming languages data."


# if __name__ == '__main__':
#     wikipedia_url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
#     languages_data = fetch_programming_languages_data(wikipedia_url)
