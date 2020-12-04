import json

with open('games.json', 'r', encoding='utf-8') as f:
    games = json.load(f)
    # print(games)

for game in games['gameList']:
    print('Назва гри - ', game['gameName'], '\n')
    print('Кількість гравців - ', game['playersNumber'], '\n')
    print('Тип гри - ', game['gameType'], '\n')
    print('Наявність інвентаря - ', game['inventory'], '\n')
    print('Місце для гри - ', game['location'], '\n')
