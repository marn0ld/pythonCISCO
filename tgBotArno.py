import config
import telebot
import config
import http.client
import json
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def MENU(message):
    keyboard = types.ReplyKeyboardMarkup(True, False)
    keyboard.add('Menu')
    send = bot.send_message(message.chat.id, "Hi!\nWelcome to Arno's covid-tracker!", reply_markup=keyboard)
    bot.register_next_step_handler(send, CONTINENT)

#button with continent/s
def CONTINENT(message):
    if message.text == 'Menu':
        keyboard = types.ReplyKeyboardMarkup(True, False)
        keyboard.row('Europe')
        send = bot.send_message(message.chat.id, 'Choose a continent', reply_markup=keyboard)
        bot.register_next_step_handler(send, OUTPUT)
    else:
        bot.send_message(message.chat.id, 'Something went wrong...')

#output of statistic about each country of an continent and sended by an txt file
def OUTPUT(message):

    #parsing
    if message.text == 'Europe':
        fp = open('Covid-tracker by Arno Muke.txt', 'w')
        conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")
        headers = {
            'x-rapidapi-key': "e36cf147d2msh773e180e52d7742p1f4ad1jsnd148121bd4cf",
            'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
                }
        conn.request("GET", "/api/npm-covid-data/europe", headers=headers)
        res = conn.getresponse()
        data = res.read()
        conv_str = data.decode("utf-8")  # making a list of dictionaries into an dictionary
        country = json.loads(conv_str)  # loading the result into json format

        # inputing statistic of each country
        for i in range(30):
            fp.write(str(' '.join(list(country[i].items())[2])))
            fp.write('\n')
            fp.write(str(' '.join(list(country[i].items())[3])))
            fp.write('\n')
            fp.write(str(' '.join(list(country[i].items())[14])))
            fp.write('\n')
            fp.write(str(' '.join(list(country[i].items())[18])))
            fp.write('\n')
            fp.write('-' * 25)
            fp.write('\n')
        fp.close()

        # sendDocument
        txt_sms = open('Covid-tracker by Arno Muke.txt', 'rb')
        bot.send_document(message.chat.id, txt_sms)


if __name__ == '__main__':
    bot.infinity_polling()