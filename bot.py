import telebot
from telebot import types
from config import tours, LANG
import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
print("TOKEN =", TOKEN)  

bot = telebot.TeleBot(TOKEN)

user_data = {}


#----- Choose language

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_data[user_id] = {}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🇷🇺 Русский", "🇬🇧 English")
    bot.send_message(user_id, LANG["ru"]["language_prompt"], reply_markup=markup)
    bot.register_next_step_handler(message, choose_language)
    
def choose_language(message):
    user_id = message.chat.id
    text = message.text
    if "Русский" in text:
        user_data[user_id]["lang"] = "ru"
    elif "English" in text:
        user_data[user_id]["lang"] = "en"
    else:
        bot.send_message(user_id, LANG["ru"]["language_prompt"])
        return bot.register_next_step_handler(message, choose_language)

    lang = user_data[user_id]["lang"]

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    for tour in tours:
        markup.add(tour)
    bot.send_message(user_id, LANG[lang]["choose_tour"], reply_markup=markup)
    bot.register_next_step_handler(message, choose_tour)
    
#---- select tour
    
def choose_tour(message):
    user_id = message.chat.id
    lang = user_data[user_id]["lang"]
    tour_name = message.text
    if tour_name not in tours:
        bot.send_message(user_id, LANG[lang]["invalid_choice"])
        return bot.register_next_step_handler(message, choose_tour)

    user_data[user_id]["tour"] = tour_name
    min_days, max_days = tours[tour_name]["duration"]
    bot.send_message(user_id, LANG[lang]["days"].format(min_days=min_days, max_days=max_days),
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, choose_days)

#-------- How many days

def choose_days(message):
    user_id = message.chat.id
    lang = user_data[user_id]["lang"]
    tour_name = user_data[user_id]["tour"]
    min_days, max_days = tours[tour_name]["duration"]

    if not message.text.isdigit():
        bot.send_message(user_id, LANG[lang]["invalid_days"].format(min_days=min_days, max_days=max_days))
        return bot.register_next_step_handler(message, choose_days)

    days = int(message.text)
    if days < min_days or days > max_days:
        bot.send_message(user_id, LANG[lang]["invalid_days"].format(min_days=min_days, max_days=max_days))
        return bot.register_next_step_handler(message, choose_days)

    user_data[user_id]["days"] = days
    bot.send_message(user_id, LANG[lang]["people"])
    bot.register_next_step_handler(message, choose_people)

#------- How many people

def choose_people(message):
    user_id = message.chat.id
    lang = user_data[user_id]["lang"]
    if not message.text.isdigit():
        bot.send_message(user_id, LANG[lang]["invalid_number"])
        return bot.register_next_step_handler(message, choose_people)

    user_data[user_id]["people"] = int(message.text)

    # Выбор отеля
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("3", "4", "5")
    bot.send_message(user_id, LANG[lang]["choose_hotel"], reply_markup=markup)
    bot.register_next_step_handler(message, choose_hotel)
    
#------ Hotel(how many stars)

def choose_hotel(message):
    user_id = message.chat.id
    lang = user_data[user_id]["lang"]
    hotel = message.text
    if hotel not in ["3", "4", "5"]:
        bot.send_message(user_id, LANG[lang]["invalid_choice"])
        return bot.register_next_step_handler(message, choose_hotel)

    user_data[user_id]["hotel"] = int(hotel)
    calculate_total(message)

#------ Calculate 
def calculate_total(message):
    user_id = message.chat.id
    lang = user_data[user_id]["lang"]
    data = user_data[user_id]

    tour_name = data["tour"]
    base_price = tours[tour_name]["base_price"]
    days = data["days"]
    min_days = tours[tour_name]["duration"][0]
    people = data["people"]
    hotel = data["hotel"]

    # Hotel coefficient
    hotel_coef = {3: 1.0, 4: 1.15, 5: 1.3}[hotel]

    total = int((days * 500) * people * hotel_coef)

    bot.send_message(user_id,
                     LANG[lang]["result"].format(tour=tour_name, days=days, people=people, hotel=hotel, total=total),
                     parse_mode="HTML")
    bot.send_message(user_id, LANG[lang]["restart"])
    
#------ Test
print("Бот запущен...")
bot.infinity_polling() 