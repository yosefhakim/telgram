import os
import telebot
import requests

# بيانات من متغيرات البيئة
TELEGRAM_TOKEN = os.getenv("7974540299:AAFmUEGNL4ZAH5S5aior5ohXmzUb8MC-jQo")
GEMINI_API_KEY = os.getenv("AIzaSyBUIrXSAGX2OmcRChAaB0mX_CTcDgt-lQA")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# دالة ترسل السؤال لجيميني وترجع الرد
def ask_gemini(question):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [{"parts": [{"text": question}]}]
    }

    res = requests.post(url, headers=headers, params=params, json=data)
    if res.status_code == 200:
        return res.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "حصل خطأ وأنا مش قادر أرد 😅"

# استقبال الرسائل من تيليجرام
@bot.message_handler(func=lambda message: True)
def reply(message):
    user_text = message.text
    answer = ask_gemini(user_text)
    bot.reply_to(message, answer)

bot.polling()
