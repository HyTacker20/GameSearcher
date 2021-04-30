import logging
import re

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

def filter_by_players_count(gamesList, needed_player):
    filtered_games = []
    needed_player = str(needed_player)
    if needed_player.isdigit():
        needed_player = int(needed_player)
        for game in gamesList :
            if needed_player >= int(game['minPlayersNumber']):
                filtered_games.append(game)
    else:
        needed_player = 0
        for game in gamesList :
            if needed_player >= int(game['minPlayersNumber']):
                filtered_games.append(game)

    # logger.info('%s games after filtering by player numbers', len(filtered_games))
    return filtered_games


def filter_by_inventory(gamesList, needed_inventory):
    filtered_games = []
    needed_inventory = str(needed_inventory)
    if needed_inventory.isdigit():
        needed_inventory = 'error'
    for game in gamesList :
        if needed_inventory.lower() == game['inventory'].lower():
            filtered_games.append(game)
    # logger.info('%s games after filtering by game inventory', len(filtered_games))
    return filtered_games


def filter_by_location(gamesList, needed_location):
    filtered_games = []
    needed_inventory = str(needed_location)
    if needed_location.isdigit():
        needed_location = 'error'
    for game in gamesList :
        if needed_location.lower() == game['location'].lower() or game['location'].lower() == 'байдуже':
            filtered_games.append(game)
    return filtered_games

def print_info(filtered_games):
    test = ''
    for game in filtered_games:
        test += f'Назва гри - {game["gameName"]}\n' \
        f'мін. Кількість гравців {game["minPlayersNumber"]}\n ' \
        f'Наявність інвентаря - {game["inventory"]}\n' \
        f'Місце для гри - {game["location"]}\n\n'
    logger.info(test)


def final_filter(gamesList, needed_data):
    filtered_games = filter_by_players_count(gamesList, needed_data[0])
    logger.info('%s games after filtering by player number', len(filtered_games))
    print_info(filtered_games)
    filtered_games = filter_by_inventory(filtered_games, needed_data[1])
    logger.info('%s games after filtering by game inventory', len(filtered_games))
    print_info(filtered_games)
    filtered_games = filter_by_location(filtered_games, needed_data[2])
    logger.info('%s games after filtering by location', len(filtered_games))
    print_info(filtered_games)
    logger.info('All games filtered done\n')
    return filtered_games

def filter_by_keyword(gameList, needed_keyword):
    filtered_games = []
    needed_keyword = needed_keyword.lower()
    if needed_keyword.isdigit():
        needed_location = 'error'
    else:
        for game in gameList:
            kwInDesc = game["description"].lower()
            index = re.search(needed_keyword, kwInDesc)

            try:
                if index.group() == needed_keyword :
                    filtered_games.append(game)
            except AttributeError :
                logger.warn('Це не підходить!')

    return filtered_games


def final_filter_with_kw(gamesList, needed_data):
    logger.info(needed_data)
    filtered_games = filter_by_players_count(gamesList, needed_data[0])
    logger.info('%s games after filtering by player number', len(filtered_games))
    filtered_games = filter_by_keyword(filtered_games, needed_data[1])
    logger.info('%s games after filtering by keyword', len(filtered_games))
    return filtered_games
