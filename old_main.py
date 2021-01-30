import telebot
import time

bot = telebot.TeleBot('1346403257:AAF8nja2C3OYMiHRMo-3Bi4lD8E911lnXzU')

# клавіатури
keyboard0 = telebot.types.ReplyKeyboardRemove()
keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard3 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard4 = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True)
keyboard1.row('Вибрати гру', 'Зв\'язок з розробниками')
keyboard2.row('З інвентарем', 'Без інвентаря')
keyboard3.row('спорт')
keyboard3.row('канцелярія')
keyboard3.row('підручні')
keyboard4.row('активні','пасивні')


    # for game in final_list:
    #     print('Назва гри - ', game['gameName'])
    #     print('мін. Кількість гравців', game['minPlayersNumber'])
    #     print('Наявність інвентаря - ', game['inventory'])
    #     print('Місце для гри - ', game['location'], '\n')




# змінні
number = 0
with_inventory = 'none'
inventory = "none"
game_type = 'none'

# команди
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт, це типу майбутній бот))    *привітання*', reply_markup=keyboard1)

# меню
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'вибрати гру':
        bot.send_message(message.chat.id, 'Нам потрібно трішки інформації про вашу компашку, щоб підібрати ідеальну гру!', reply_markup=keyboard0)
        # time.sleep(2)                                                ------------------------------------------------------------------------------------------------------------
        bot.send_message(message.chat.id, 'Скільки людей у вашій компашці? (введи число)')
        bot.register_next_step_handler(message, get_number)

    elif message.text.lower() == 'зв\'язок з розробниками':
        bot.send_message(message.chat.id, 'Над ботом працює @HyTacker20')

    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощавай, творець!')

    # else :
         # bot.send_message(message.chat.id, 'Ану бистро витер, і написав нормально!!!')

def get_number(message):
    number = str(message.text)
    bot.send_message(message.chat.id, 'Окей, у вашій компашці ' +number+ ' людей)')
    # time.sleep(1)
    # bot.send_message(message.chat.id, 'Яку гру ви хочете : з інвентарем чи без?', reply_markup=keyboard2)
    # bot.register_next_step_handler(message, what_type)

def what_type(message):
    bot.send_message(message.chat.id, 'Який тип ігор ви хочете? Активні чи пасивні?', reply_markup=keyboard4)
    if message.text.lower() == 'активні':
        game_type = 'active'
    elif message.text.lower() == 'пасивні':
        game_type = 'passive'


def get_inventory(message):
    while with_inventory != 'yes':
        if message.text.lower() == 'з інвентарем':
            bot.send_message(message.chat.id, 'ну ок, буде тобі з інвентарем!')
            with_inventory = 'yes'
            bot.register_next_step_handler(message, which_inventory)

        elif message.text.lower() == 'без інвентаря':
            with_inventory = 'no'
            bot.register_next_step_handler(message, which_inventory)

def which_inventory(message):
    if with_inventory == 'with':
        bot.send_message(message.chat.id, 'Вибери який інвентарь у тебе є під рукою', reply_markup=keyboard3)
        if message.text.lower() == 'спорт':
            inventory = 'sport'
        elif message.text.lower() == 'канцелярія':
            inventory = 'cans'
        elif message.text.lower() == 'підручні':
            inventory = 'pidruch'
        bot.register_next_step_handler(message, what_type);


def what_type(message):
    bot.send_message(message.chat.id, 'Який тип ігор ви хочете? Активні чи пасивні?', reply_markup=keyboard4)
    if message.text.lower() == 'активні':
        game_type = 'active'
    elif message.text.lower() == 'пасивні':
        game_type = 'passive'



bot.polling(none_stop=True, interval=0)
