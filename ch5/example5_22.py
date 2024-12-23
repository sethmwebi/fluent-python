import typing


class City(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City("Asia", "Tokyo", "JP"),
    City("Asia", "Delhi", "IN"),
    City("North America", "Mexico City", "MX"),
    City("North America", "New York", "US"),
    City("South America", "São Paulo", "BR"),
]


def match_asian_cities():
    results = []
    for city in cities:
        match city:
            case City(continent="Asia", country=cc):
                results.append(cc)
    return results


def match_asian_cities_pos():
    results = []
    for city in cities:
        match city:
            case City("Asia", _, country):
                results.append(country)
    return results


# print(match_asian_cities_pos())
print(City.__match_args__)
