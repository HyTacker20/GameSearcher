def filter_by_players_count(gamesList, needed_player):

    good_games = []

    for game in gamesList :
        if needed_player >= game['minPlayersNumber']:
            good_games.append(game)

    return good_games
