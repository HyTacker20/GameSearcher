import json

def get_games():
    with open('games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)
        # print(games)

    for game in games['gameList']:
        print('Назва гри - ', game['gameName'])
        print('Кількість гравців - ', game['playersNumber'])
        print('Тип гри - ', game['gameType'])
        print('Наявність інвентаря - ', game['inventory'])
        print('Місце для гри - ', game['location'], '\n')
