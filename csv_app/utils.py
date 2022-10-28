# Mi solución
'''
def get_population(country):
  new_country = {}
  for key, value in country.items():
    if ' Population' in key and not 'World' in key :
      new_key = key.replace(' Population', '')
      new_country[new_key] = int(value)
    else: 
      continue
      
  return new_country
'''


def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  keys = population_dict.keys()
  values = population_dict.values()
  return keys, values

def get_world_population_percentage(country):
  return { country['Country/Territory']: country['World Population Percentage']}

  
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result