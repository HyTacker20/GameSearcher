def filter_by_players_count(gamesList, needed_player):
    filtered_games = []

    for game in gamesList :
        if needed_player >= int(game['minPlayersNumber']):
            filtered_games.append(game)

    return filtered_games


def filter_by_inventory(gamesList, needed_inventory):
    filtered_games = []

    for game in gamesList :
        if needed_inventory == game['inventory']:
            filtered_games.append(game)

    return filtered_games


def filter_by_location(gamesList, needed_location):
    filtered_games = []

    for game in gamesList :
        if needed_location == game['location'] or game['location'] == 'байдуже':
            filtered_games.append(game)

    return filtered_games

def final_filter(gamesList, needed_data):
    filtered_games = filter_by_players_count(gamesList, needed_data[0])
    filtered_games = filter_by_inventory(filtered_games, needed_data[1])
    filtered_games = filter_by_location(filtered_games, needed_data[2])
    return filtered_games
