import json

def get_games():

    games = None
    with open('../data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)

    return games
