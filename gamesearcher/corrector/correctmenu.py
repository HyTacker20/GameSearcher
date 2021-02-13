import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import random

TOKEN = '1537653659:AAENNo_b0s8vmvfEF-GWhoRaNkeqWMJw0eY'
bot = telebot.TeleBot(TOKEN)

game_filters = {
    'count': {
        'message': 'Скільки гравців?'
    },
    'inventory': {
        'message': 'Наявність інвентаря?',
        'options': [
            'Спортивний',
            'Канцелярія',
            'Підручні',
            'Нема'
        ],
        'keyboard': ""
    },
    'location': {
        'message': 'Де будете грати??',
        'options': [
            'Всередині',
            'Зовні'
        ]
    }
}
bt0 = KeyboardButton('null 0')
bt1 = KeyboardButton('null 1')
bt2 = KeyboardButton('null 2')
bt3 = KeyboardButton('null 3')
bt4 = KeyboardButton('null 4')
bt5 = KeyboardButton('null 5')
list = [bt0, bt1, bt2, bt3, bt4, bt5]

def get_step(key):
    data = game_filters[key]
    data = data['options']
    print(data)
    count = (len(data))
    print(count)
    n = 0

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in data:
        print(i)
        list[n] = KeyboardButton(data[n])
        keyboard.add(list[n])
        n = n + 1
        print(n)
    return keyboard

lol = get_step('location')

@bot.message_handler(commands=['start'])
def start(msg):
    start_text = 'Привіт, це бот для пошуку ігор)'
    bot.send_message(msg.chat.id,start_text,parse_mode='markdown',reply_markup=get_step('location'))

bot.polling(none_stop=True, interval=0)
