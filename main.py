import gamer
import filtering

games = gamer.get_games()
# for game in games['gameList']:
#     print('Назва гри - ', game['gameName'])
#     print('Кількість гравців - ', game['minPlayersNumber'])
#     print('Тип гри - ', game['gameType'])
#     print('Наявність інвентаря - ', game['inventory'])
#     print('Місце для гри - ', game['location'], '\n')

needed_player = str(input('Скільки гравців? - '))
print('\n', '-----------------------------------')

filtered_list = filtering.filter_by_players_count(games['gameList'], needed_player)
for game in filtered_list:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['minPlayersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')
