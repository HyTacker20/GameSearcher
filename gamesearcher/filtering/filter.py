import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def filter_by_players_count(gamesList, needed_player):
    filtered_games = []

    for game in gamesList :
        if needed_player >= int(game['minPlayersNumber']):
            filtered_games.append(game)
    # logger.info('%s games after filtering by player numbers', len(filtered_games))
    return filtered_games


def filter_by_inventory(gamesList, needed_inventory):
    filtered_games = []

    for game in gamesList :
        if needed_inventory == game['inventory']:
            filtered_games.append(game)
    # logger.info('%s games after filtering by game inventory', len(filtered_games))
    return filtered_games


def filter_by_location(gamesList, needed_location):
    filtered_games = []

    for game in gamesList :
        if needed_location == game['location'] or game['location'] == 'байдуже':
            filtered_games.append(game)
    # logger.info('%s games filtering by needed location', len(filtered_games))
    return filtered_games
def final_filter(gamesList, needed_data):
    filtered_games = filter_by_players_count(gamesList, needed_data[0])
    logger.info('%s games after filtering by player number', len(filtered_games))
    test = ''
    for game in filtered_games:
        test += f'Назва гри - {game["gameName"]}\n' \
        f'мін. Кількість гравців {game["minPlayersNumber"]}\n ' \
        f'Наявність інвентаря - {game["inventory"]}\n' \
        f'Місце для гри - {game["location"]}\n\n'
    logger.info(test)
    filtered_games = filter_by_inventory(filtered_games, needed_data[1])
    logger.info('%s games after filtering by game inventory', len(filtered_games))
    test1 = ''
    for game in filtered_games:
        test1 += f'Назва гри - {game["gameName"]}\n' \
        f'мін. Кількість гравців {game["minPlayersNumber"]}\n ' \
        f'Наявність інвентаря - {game["inventory"]}\n' \
        f'Місце для гри - {game["location"]}\n\n'
    logger.info(test1)
    filtered_games = filter_by_location(filtered_games, needed_data[2])
    logger.info('%s games after filtering by location', len(filtered_games))
    test2 = ''
    for game in filtered_games:
        test2 += f'Назва гри - {game["gameName"]}\n' \
        f'мін. Кількість гравців {game["minPlayersNumber"]}\n ' \
        f'Наявність інвентаря - {game["inventory"]}\n' \
        f'Місце для гри - {game["location"]}\n\n'
    logger.info(test2)
    logger.info('All games filtered done\n')
    return filtered_games
