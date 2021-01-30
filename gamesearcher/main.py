import telebot
import time
import config
import logging

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from  dataaccess import gamer
from filtering import filter

bot = telebot.TeleBot(config.TOKEN)

games = gamer.get_games()
logging.basicConfig(level = logging.INFO)
logger = logger = logging.getLogger(__name__)

logger.info('Bot started')

needed_data=[]
final_list=[]
# ---------------------------------------------------------
keyboard0 = telebot.types.ReplyKeyboardRemove()
# ---------------------------------------------------------
home = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
searchgame = KeyboardButton('Вибрати гру')
feedback = KeyboardButton('Зв\'язок з розробниками')
home.add(searchgame,feedback,)
# ---------------------------------------------------------
sg = ReplyKeyboardMarkup(resize_keyboard=True)
search = KeyboardButton('Шукати')
sg.add(search)
# ---------------------------------------------------------
MenuBar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
info = KeyboardButton('Інформація про розробників')
feedback1 = KeyboardButton('Зв\'язок з нами')
back = KeyboardButton('Назад')
MenuBar.add(info, feedback1, back)
# ---------------------------------------------------------
inventory = ReplyKeyboardMarkup(resize_keyboard=True)
sport = KeyboardButton('Cпортивний')
office = KeyboardButton('Канцелярія')
hand = KeyboardButton('Підручні')
no = KeyboardButton('Нема')
inventory.add(sport, office, hand, no)
# ---------------------------------------------------------
location = ReplyKeyboardMarkup(resize_keyboard=True)
outside = KeyboardButton('Зовні')
inside = KeyboardButton('Всередині')
location.add(outside, inside)
# ---------------------------------------------------------
logger.info('Keyboards loaded')
logger.info('Bot wait for user')
@bot.message_handler(commands=['start'])
def start(msg):
    start_text = 'Привіт, це бот для пошуку ігор)'
    Home = bot.send_message(msg.chat.id,start_text,parse_mode='markdown',reply_markup=home)

@bot.message_handler(regexp='Зв\'язок з розробниками')
def Menu(msg):
    bot.send_message(msg.chat.id,'Що тебе цікавить? :)',reply_markup=MenuBar)

@bot.message_handler(regexp='Назад')
def Menu(msg):
    bot.send_message(msg.chat.id,'Ви повернулися назад',reply_markup=home)

@bot.message_handler(regexp='Інформація про розробників')
def Menu(msg):
    info = 'Бот розроблений учасником команди FLL *United Kingdom* @HyTacker20, з допомогою @alex\_dubchak'
    bot.send_message(msg.chat.id, info, parse_mode='markdown')

@bot.message_handler(regexp='Вибрати гру')
def start_search(msg):
    bot.send_message(msg.chat.id, 'Скільки гравців?', reply_markup=keyboard0)
    bot.register_next_step_handler(msg, get_number)

def get_number(msg):
    needed_number = int(msg.text)
    needed_data.append(needed_number)
    bot.send_message(msg.chat.id, 'Наявність інвентаря?', reply_markup=inventory)
    bot.register_next_step_handler(msg, get_inventory)

def get_inventory(msg):
    needed_inventory = msg.text
    needed_data.append(needed_inventory)
    bot.send_message(msg.chat.id, 'Де будете грати??', reply_markup=location)
    bot.register_next_step_handler(msg, get_location)

def get_location(msg):
    needed_location = msg.text
    needed_data.append(needed_location)
    message = f'**Ти вибрав такі параметри :** \n Кількість граців - {needed_data[0]} \n Інвентарь - {needed_data[1]} \n Розташування - {needed_data[2]}'
    bot.send_message(msg.chat.id, message, reply_markup=sg, parse_mode='markdown')
    # bot.register_next_step_handler(msg, send_data)

@bot.message_handler(regexp='Шукати')
def send_data(msg):
    final_list = filter.final_filter(games['gameList'], needed_data)
    msg2 = f'ну тут короче {final_list}'
    bot.send_message(msg.chat.id, msg2)
    msg1 = ''
    for game in final_list:
        msg1 += f'Назва гри - {game["gameName"]}\n' \
        f'мін. Кількість гравців {game["minPlayersNumber"]}\n ' \
        f'Наявність інвентаря - {game["inventory"]}\n' \
        f'Місце для гри - {game["location"]}\n\n'

    bot.send_message(msg.chat.id, msg1)

bot.polling(none_stop=True, interval=0)
