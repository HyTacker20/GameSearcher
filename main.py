import gamer
import filtering

games = gamer.get_games()

needed_data=[]

needed_data.append(int(input('Скільки гравців? - ')))
print('\n', '-----------------------------------')
needed_data.append(str(input('Наявність інвентаря?(канцелярія | спортивний | підручні | нема) - ').lower()))
print('\n', '-----------------------------------')
needed_data.append(str(input('Де будете грати?(всередині | зовні) - ').lower()))
print('\n', '-----------------------------------')

final_list = filtering.final_filter(games['gameList'], needed_data)

for game in final_list:
    print('Назва гри - ', game['gameName'])
    print('мін. Кількість гравців - ', game['minPlayersNumber'])
    print('Наявність інвентаря - ', game['inventory'])
    print('Місце для гри - ', game['location'], '\n')
