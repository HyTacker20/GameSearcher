def filter_by_players_count(gamesList, needed_player):
    good_games1 = []

    for game in gamesList :
        if needed_player >= game['minPlayersNumber']:
            good_games1.append(game)

    return good_games1


def filter_by_inventory(gamesList, needed_inventory):
    good_games2 = []

    for game in gamesList :
        if needed_inventory == game['inventory']:
            good_games2.append(game)

    return good_games2


def filter_by_type(gamesList, needed_type):
    good_games3 = []

    for game in gamesList :
        if needed_type == game['gameType']:
            good_games3.append(game)

    return good_games3


def filter_by_location(gamesList, needed_location):
    good_games4 = []

    for game in gamesList :
        if needed_location == game['location'] or game['location'] == 'байдуже':
            good_games4.append(game)
        # elif game['gameLocation'] == 'байдуже':


    return good_games4
