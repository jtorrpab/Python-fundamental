number = [1,2,3,4,5]
new_list_number = list(filter(lambda x : x % 2 == 0, number))
print(new_list_number)

# Filter con diccionarios 

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

# Filtrar solo los equipos que ganador 
print(matches)
print(len(matches))

winners = list(filter(lambda item : item['home_team_result'] == 'Win', matches))
print(winners)
print(len(winners))