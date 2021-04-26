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
    sport = KeyboardButton('Спортивний')
    office = KeyboardButton('Канцелярія')
    hand = KeyboardButton('Підручні')
    keyword = KeyboardButton('Ключові слова')
    no = KeyboardButton('Нема')
    inventory.row(sport, office, hand)
    inventory.row(keyword)
    inventory.row(no)
    return inventory

def location():
    location = ReplyKeyboardMarkup(resize_keyboard=True)
    outside = KeyboardButton('На вулиці')
    inside = KeyboardButton('У приміщенні')
    location.add(outside, inside)
    return location

def keywords():
    keywords = ReplyKeyboardMarkup(resize_keyboard=True)
    word1 = KeyboardButton("М'яч")
    word2 = KeyboardButton('Скотч')
    word3 = KeyboardButton('Крейда')
    keywords.add(word1, word2, word3)
    return keywords

def search_kw():
    search = ReplyKeyboardMarkup(resize_keyboard=True)
    search1 = KeyboardButton('Шукати за ключовим словом')
    search.add(search1)
    return search

def delete():
    keyboard0 = telebot.types.ReplyKeyboardRemove()
    return keyboard0
