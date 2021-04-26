import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)
def get_games():

    games = None
    with open('dataaccess/data/games.json', 'r', encoding='utf-8') as f:
        games = json.load(f)

    logger.info(' %s games loaded', len(games['gameList']))

    return games
