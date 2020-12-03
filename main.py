import json

with open('games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)
    # print(games)

for txt in games['gameList']:
    print('Назва гри - ', txt['gameName'], '\n', 'Кількість гравців - ', txt['playersNumber'], '\n', 'Тип гри - ', txt['gameType'], '\n', 'Наявність інвентаря - ', txt['inventory'], '\n', 'Місце для гри - ', txt['location'], '\n')
