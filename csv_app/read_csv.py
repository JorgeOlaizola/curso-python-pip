import csv # Módulo nativo para leer csv
import utils

def format_country(country, keys):
  return {keys[index] : country[index] for index in range(0, len(keys))}

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    keys = reader.__next__() # También funciona next(reader)
    # countries = list(map(lambda x : format_country(x, keys), reader)) # Mi solució
    data = []
    for row in reader:
      iterable = list(zip(keys, row))
      country_dict = { key : value for key, value in iterable }
      data.append(country_dict)
      #print(row) # Cada fila viene como un array
    return data

if __name__ == "__main__":
  data = read_csv('./app/data.csv')
  world_population_array = list(map(lambda x : utils.get_world_population_percentage(x), data).items())
  countries_population = list(map(lambda x : utils.get_population(x), data))

