Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> from pprint import pprint

cities = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

distances = dict()

moscow = cities['Moscow']
london = cities['London']
paris = cities['Paris']

moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2) ** 0.5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2) ** 0.5
london_paris = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_paris
distances['Paris']['London'] = london_paris

pprint(distances)
