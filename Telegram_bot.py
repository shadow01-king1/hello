import telebot
import requests

BOT_TOKEN = "bot_token"
API_KEY = "openweathermap_api_key"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def pogoda(message):
    city = "Khujand"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        r = requests.get(url)
        d = r.json()
        print(d)

        if d.get("cod") != 200:
            bot.send_message(message.chat.id, "❗ Ob-havo ma'lumotini olishda xatolik!")
            return

        t = d["main"]["temp"]
        f = d["main"]["feels_like"]
        des = d["weather"][0]["description"].title()

        text = (
            f"🌤 Погода в Ходженте:\n"
            f"Температура: {t}°C\n"
            f"Ощущается как: {f}°C\n"
            f"Описание: {des}"
        )

        bot.send_message(message.chat.id, text)

    except Exception as e:
        bot.send_message(message.chat.id, "⚠ Xatolik yuz berdi. Keyinroq urinib ko‘ring.")

bot.infinity_polling()
