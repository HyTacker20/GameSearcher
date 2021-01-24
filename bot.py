import telebot
import time
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot('1537653659:AAENNo_b0s8vmvfEF-GWhoRaNkeqWMJw0eY')

# клавіатури
# keyboard2.row('Спортивний')
# keyboard2.row('Канцелярія')
# keyboard2.row('Підручні')
# keyboard3.row('Зовні')
# keyboard3.row('Всередині')

home = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
searchgame = KeyboardButton('Вибрати гру')
feedback = KeyboardButton('Зв\'язок з розробниками')
back = KeyboardButton('Назад')
home.add(searchgame,feedback,)



@bot.message_handler(commands=['start'])
def start(msg):
    start_text = 'Привіт, це бот для пошуку ігор)'
    Home = bot.send_message(msg.chat.id,start_text,parse_mode='markdown',reply_markup=home)

MenuBar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
Item1 = KeyboardButton('Інформація про розробників')
Item2 = KeyboardButton('Зв\'язок з нами')
Item3 = KeyboardButton('Назад')
MenuBar.add(Item1,Item2,Item3)

@bot.message_handler(regexp='Зв\'язок з розробниками')
def Menu(msg):
    bot.send_message(msg.chat.id,'Що тобі треба?',reply_markup=MenuBar)

@bot.message_handler(regexp='Назад')
def Menu(msg):
    bot.send_message(msg.chat.id,'Ви повернулися назад',reply_markup=home)

@bot.message_handler(regexp='Інформація про розробників')
def Menu(msg):
    info = 'Бот розроблений учасником команди FLL *United Kingdom* @HyTacker20, з допомогою @alex\_dubchak'
    bot.send_message(msg.chat.id, info, parse_mode='markdown')





bot.polling(none_stop=True, interval=0)
