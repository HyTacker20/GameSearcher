import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def home():
    home = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    searchgame = KeyboardButton('Вибрати гру')
    feedback = KeyboardButton('Зв\'язок з розробниками')
    home.add(searchgame,feedback,)
    return home

def search():
    sg = ReplyKeyboardMarkup(resize_keyboard=True)
    search = KeyboardButton('Шукати')
    sg.add(search)
    return sg

def menu():
    MenuBar = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    info = KeyboardButton('Інформація про розробників')
    feedback1 = KeyboardButton('Зв\'язок з нами')
    back = KeyboardButton('Назад')
    MenuBar.add(info, feedback1, back)
    return MenuBar

def inventory():
    inventory = ReplyKeyboardMarkup(resize_keyboard=True)
    sport = KeyboardButton('Cпортивний')
    office = KeyboardButton('Канцелярія')
    hand = KeyboardButton('Підручні')
    no = KeyboardButton('Нема')
    inventory.add(sport, office, hand, no)
    return inventory

def location():
    location = ReplyKeyboardMarkup(resize_keyboard=True)
    outside = KeyboardButton('На вулиці')
    inside = KeyboardButton('У приміщенні')
    location.add(outside, inside)
    return location

def delete():
    keyboard0 = telebot.types.ReplyKeyboardRemove()
    return keyboard0
