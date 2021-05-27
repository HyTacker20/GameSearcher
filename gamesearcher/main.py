import telebot
import time
import config
import logging

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from  dataaccess import gamer
from filtering import filter
from keyboards import keyboard as kb

bot = telebot.TeleBot(config.TOKEN)

games = gamer.get_games()
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Bot started')

needed_data={}
final_list=[]


logger.info('Keyboards loaded')
logger.info('Bot wait for user')


@bot.message_handler(commands=['start'])
def start(msg):
    start_text = 'Привіт, це бот для пошуку ігор)'
    Home = bot.send_message(msg.chat.id,start_text,parse_mode='markdown',reply_markup=kb.home())

@bot.message_handler(regexp='Зв\'язок з розробниками')
def Menu(msg):
    bot.send_message(msg.chat.id,'Що тебе цікавить? :)',reply_markup=kb.menu())

@bot.message_handler(regexp='Назад')
def Menu(msg):
    bot.send_message(msg.chat.id,'Ви повернулися назад',reply_markup=kb.home())

@bot.message_handler(regexp='Інформація про розробників')
def Menu(msg):
    info = 'Бот розроблений учасником команди FLL *United Kingdom* @HyTacker20, з допомогою @alex\_dubchak'
    bot.send_message(msg.chat.id, info, parse_mode='markdown')

@bot.message_handler(regexp="Зв'язок з нами")
def Menu(msg):
    info = 'Якщо ви маєте якісь питання чи пропозиції то пишіть сюди : \n*gameseacherbot@gmail.com*'
    bot.send_message(msg.chat.id, info, parse_mode='markdown')

@bot.message_handler(regexp='Вибрати гру')
def start_search(msg):
    bot.send_message(msg.chat.id, 'Скільки гравців?', reply_markup=kb.delete())
    bot.register_next_step_handler(msg, get_number)

def get_number(msg):
    str = msg.text
    if str.isdigit():
        if not msg.chat.id in needed_data:
            needed_data[msg.chat.id] = []
        needed_number = int(str)
        needed_data[msg.chat.id].append(needed_number)
        bot.send_message(msg.chat.id, 'Наявність інвентаря?', reply_markup=kb.inventory())
        bot.register_next_step_handler(msg, get_inventory)
    else:
        # needed_data[msg.chat.id].clear()
        bot.send_message(msg.chat.id, 'Наступного разу напишіть будь ласка число!', reply_markup=kb.home())
        # bot.register_next_step_handler(msg, start)

def get_inventory(msg):
    needed_inventory = msg.text
    if needed_inventory.isdigit():
        needed_data[msg.chat.id].clear()
        bot.send_message(msg.chat.id, 'Наступного разу нажміть кнопку!', reply_markup=kb.home())

    elif needed_inventory == 'Ключові слова':
        bot.send_message(msg.chat.id, 'Вибери ключове слово)', reply_markup=kb.keywords())
        bot.register_next_step_handler(msg, get_keywords)

    else:
        needed_data[msg.chat.id].append(needed_inventory)
        bot.send_message(msg.chat.id, 'Де будете грати??', reply_markup=kb.location())
        bot.register_next_step_handler(msg, get_location)

def get_keywords(msg):
    needed_keyword = msg.text
    if needed_keyword.isdigit():
        needed_data[msg.chat.id].clear()
        bot.send_message(msg.chat.id, 'Наступного разу нажміть кнопку!', reply_markup=kb.home())

    else:
        needed_data[msg.chat.id].append(needed_keyword)
        message = 'Ти обрав - '+needed_keyword
        bot.send_message(msg.chat.id, message, reply_markup=kb.search_kw())

def get_location(msg):
    needed_location = msg.text
    if needed_location.isdigit():
        needed_data[msg.chat.id].clear()
        bot.send_message(msg.chat.id, 'Наступного разу нажміть кнопку!', reply_markup=kb.home())
    else:
        needed_location = needed_location
        needed_data[msg.chat.id].append(needed_location)
        logger.info('%s in needed_data', needed_data[msg.chat.id])
        message = f'**Ти вибрав такі параметри :** \n Кількість граців - {needed_data[msg.chat.id][0]} \n Інвентарь - {needed_data[msg.chat.id][1]} \n Розташування - {needed_data[msg.chat.id][2]}'
        bot.send_message(msg.chat.id, message, reply_markup=kb.search(), parse_mode='markdown')

@bot.message_handler(regexp='Шукати за ключовим словом')
def send_data_by_kw(msg):
    final_list = filter.final_filter_with_kw(games['gameList'], needed_data[msg.chat.id])
    needed_data[msg.chat.id].clear()
    if len(final_list) != 0:
        for game in final_list:
            msg1 = ''
            msg1 += f'*Назва гри* : {game["gameName"]}\n\n' \
            f'*Мінімальна кількість гравців* : {game["minPlayersNumber"]}\n\n' \
            f'*Наявність інвентаря* : {game["inventory"]}\n\n' \
            f'*Місце для гри* : {game["location"]}\n\n' \
            f'*Опис* : {game["description"]}\n\n' \
            f'*Посилання* : {game["url"]}\n'
            bot.send_message(msg.chat.id, msg1, parse_mode='markdown', reply_markup=kb.home())
    else:
        bot.send_message(msg.chat.id, 'Схоже, що ми не найшли жодної гри(( Спробуй інші параметри!', reply_markup=kb.home())

@bot.message_handler(regexp='Шукати')
def send_data(msg):
    final_list = filter.final_filter(games['gameList'], needed_data[msg.chat.id])
    needed_data[msg.chat.id].clear()
    if len(final_list) != 0:
        for game in final_list:
            msg1 = ''
            msg1 += f'*Назва гри* : {game["gameName"]}\n\n' \
            f'*Мінімальна кількість гравців* : {game["minPlayersNumber"]}\n\n' \
            f'*Наявність інвентаря* : {game["inventory"]}\n\n' \
            f'*Місце для гри* : {game["location"]}\n\n' \
            f'*Опис* : {game["description"]}\n\n' \
            f'*Посилання* : {game["url"]}\n'
            bot.send_message(msg.chat.id, msg1, parse_mode='markdown', reply_markup=kb.home())
    else:
        bot.send_message(msg.chat.id, 'Схоже, що ми не найшли жодної гри(( Спробуй інші параметри!', reply_markup=kb.home())

bot.polling(none_stop=True, interval=0)
