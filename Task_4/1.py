#Data input 
N = int(input('Enter count lines: '))
input_strings = list()
for i in range(N):
    input_string = input('Enter number of lines #%s: ' % i)
    input_strings.append(input_string)
#Dictionary entry
city_dict = dict()
for input_string in input_strings:
    words = input_string.split()
    city_dict[words[0]] = words[1:]
#Cities input
city_count = int(input('Enter number of cities: '))
cities = list()
for _ in range(city_count):
    city = input('Enter a city: ')
    cities.append(city)
#Country output
for city in cities:
    for key, values in city_dict.items():
        if city in values:
            print(key)
    
