import gamer


games = gamer.get_games()

for game in games['gameList']:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['playersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')
