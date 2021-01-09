import gamer
import filtering

games = gamer.get_games()


needed_player = str(input('Скільки гравців? - '))
print('\n', '-----------------------------------')

filtered_list1 = filtering.filter_by_players_count(games['gameList'], needed_player)
for game in filtered_list1:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['minPlayersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')


needed_inventory = str(input('Наявність інвентаря?(канцелярія | спортивний | підручні | нема) - ').lower())
print('\n', '-----------------------------------')

filtered_list2 = filtering.filter_by_inventory(filtered_list1, needed_inventory)
for game in filtered_list2:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['minPlayersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')


needed_type = str(input('Який тип гри?(активна | пасивна) - ').lower())
print('\n', '-----------------------------------')

filtered_list3 = filtering.filter_by_type(filtered_list2, needed_type)
for game in filtered_list3:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['minPlayersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')


needed_location = str(input('Де будете грати?(всередині | зовні) - ').lower())
print('\n', '-----------------------------------')

filtered_list4 = filtering.filter_by_location(filtered_list3, needed_location)
for game in filtered_list4:
    print('Назва гри - ', game['gameName'])
    print('Кількість гравців - ', game['minPlayersNumber'])
    print('Тип гри - ', game['gameType'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')
