import asyncio
import json
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes,
    CallbackQueryHandler, MessageHandler, filters,
    ConversationHandler
)
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import datetime
import telegram
import time
import gspread
from requests.exceptions import ConnectionError
from oauth2client.service_account import ServiceAccountCredentials
import logging
import sqlite3
import uuid

logging.basicConfig(level=logging.INFO)

def get_db_connection():
    return pymysql.connect(
        host="",
        user="",
        password="",
        database="",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def base36decode(s):
    try:
        return int(s, 36)
    except ValueError:
        return None

async def log_error(context, error_message):
    logging.error(f"Произошла ошибка: {error_message}")
    await context.bot.send_message(chat_id=588896602, text=f"Ошибка: {error_message}")

from telegram.error import TimedOut, NetworkError
import asyncio

async def send_telegram_message(context, chat_id, text):
    try:
        await context.bot.send_message(chat_id=chat_id, text=text)
    except TimedOut:
        print("Запрос к API Telegram завершился по таймауту.")
        await asyncio.sleep(5)
        await send_telegram_message(context, chat_id, text)
    except NetworkError as ne:
        print(f"Ошибка сети при отправке сообщения: {ne}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

import time

ADMIN_CHAT_ID = 588896602

import asyncio
import datetime

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    telegram_id = str(user.id)

    if update.message and update.message.chat.type in ["group", "supergroup"]:
        await update.message.reply_text(
            "Пожалуйста, используйте команду /start в личном сообщении со мной."
        )
        return
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT telegram_id FROM users WHERE telegram_id = ?', (telegram_id,))
    existing_user = cursor.fetchone()

    if existing_user:
        await main_menu(update, context)
    else:
        message_text = (
            """🎁 Привет! Ты в NFT Gift Market — месте, где цифровые подарки обретают вторую жизнь.
💎 Покупай и продавай NFT-подарки быстро и безопасно.
🚀 Всё просто: выбери — выстави — заработай.

🔐 Вход без лишних заморочек.
🧠 Умные фильтры и прозрачные сделки.
🔥 Лимитки, дропы и редкости — всегда под рукой.

Готов начать? Жми OPEN снизу и погнали!"""
        )
        chat_id = update.effective_chat.id
        message = await context.bot.send_message(
            chat_id=chat_id,
            text=message_text,
        )

        registration_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
        INSERT INTO Users (name, username, telegram_id, registrationdate)
        VALUES (?, ?, ?, ?)
        ''', (user.full_name, user.username or "", telegram_id, registration_date))
        conn.commit()

        await asyncio.sleep(5)

        await main_menu(update, context)

    if update.message:
        await update.message.delete()

    conn.close()

import string
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import CallbackContext

def to_base36(num: int) -> str:
    if num < 0:
        raise ValueError("Отрицательные числа не поддерживаются")
    
    chars = string.digits + string.ascii_uppercase
    base36 = ''
    
    if num == 0:
        return '0'
    
    while num > 0:
        num, i = divmod(num, 36)
        base36 = chars[i] + base36
    
    return base36

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not user:
        await update.message.reply_text("Не удалось определить пользователя.")
        return
    user_id = user.id
    try:
        obfuscated_id = to_base36(user_id)
    except ValueError as ve:
        await update.message.reply_text(f"Ошибка кодирования ID: {ve}")
        return
    shopurl = f"https://fluxgifts.ru.tuna.am/user/{obfuscated_id}"
    channel_url = "https://t.me/sickboips"
    chat_url = "https://t.me/sickboips"
    support_url = "https://t.me/sickboips"

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT telegram_id FROM admins WHERE telegram_id = ?', (str(user.id),))
    is_admin = cursor.fetchone() is not None
    conn.close()


    keyboard = [
        [InlineKeyboardButton("Открыть маркет", web_app=WebAppInfo(url=shopurl))],
        [InlineKeyboardButton("Информация", callback_data="info")],
        [InlineKeyboardButton("Подписаться на канал", url=channel_url)],
        [InlineKeyboardButton("Присоединиться к чату", url=chat_url)],
        [InlineKeyboardButton("Написать менеджеру", url=support_url)],
    ]
    if is_admin:
        admin_url = f"https://fluxgifts.ru.tuna.am/admin/{obfuscated_id}"
        keyboard.append([InlineKeyboardButton("Админ-меню", web_app=WebAppInfo(url=admin_url))])

    reply_markup = InlineKeyboardMarkup(keyboard)

    image_url = "https://sun9-41.userapi.com/impg/JV0FAQZqkz5gQYfEjRWMdvUpgc0XWu6Lg_WwwQ/jeM24YowtSs.jpg?size=500x500&quality=95&sign=f52ef6636e5dccf1f84d89a36357b082&type=album"

    if update.callback_query:
        message = await update.callback_query.message.reply_photo(
            photo=image_url,
            caption="Для того, чтобы открыть маркет, нажми OPEN снизу!",
            reply_markup=reply_markup
        )
    else:
        message = await update.message.reply_photo(
            photo=image_url,
            caption="Для того, чтобы открыть маркет, нажми OPEN снизу!",
            reply_markup=reply_markup
        )
    if 'last_message' in context.user_data:
        try:
            await context.bot.delete_message(
                chat_id=update.effective_chat.id,
                message_id=context.user_data['last_message']
            )
        except:
            pass
    context.user_data['last_message'] = message.message_id

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'check_subscription':
        await check_subscription(update, context)
    elif query.data == 'main_menu':
        await main_menu(update, context)
    elif query.data == 'info':
        await query.message.reply_text(
            "ℹ️ Информация о маркете:\n"
            "Здесь вы можете покупать и продавать NFT-подарки. Всё просто и безопасно!"
        )
    elif query.data == 'start':
        await start(update, context)

async def main_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == 'my_orders':
        await my_orders(update, context)
    elif query.data == 'draw':
        await draw(update, context)
    elif query.data == 'main_menu':
        await main_menu(update, context)

import datetime
import pytz
import numpy as np
import matplotlib.pyplot as plt
import tempfile
import os
import calendar
from telegram import Update
from telegram.ext import ContextTypes
orderschat = 588896602

async def user_response_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    logging.info(f"Message from {user_id}")
    
    if update.message.chat.type in ["group", "supergroup"]:
        return

    if 'awaiting_responses' in context.bot_data and context.bot_data['awaiting_responses'].get(user_id):
        try:
            await context.bot.forward_message(chat_id=ADMIN_CHAT_ID2, from_chat_id=update.effective_chat.id, message_id=update.message.message_id)
            logging.info(f"Message {user_id} reposted to admin (broadcast).")

            context.bot_data['awaiting_responses'][user_id] = False
            await update.message.reply_text("Ваше сообщение отправлено администрации. Спасибо!")

        except Exception as e:
            logging.error(f"Error broadcast-message {user_id}: {e}")
            await update.message.reply_text("Произошла ошибка при отправке вашего сообщения. Попробуйте позже.")
        return


    logging.info(f"Message {user_id} not in 'responses' and 'wishes'.")

    user_text = update.message.text.strip()
    chatgpt_answer = generate_chatgpt_response(user_text)

    await update.message.reply_text(chatgpt_answer)

def main():
    application = ApplicationBuilder().token("xxx").build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CallbackQueryHandler(button_handler, pattern='^(check_subscription|main_menu)$'))
    application.add_handler(CallbackQueryHandler(main_menu_handler, pattern='^(my_orders|cart|draw|main_menu)$'))
    application.add_handler(CallbackQueryHandler(start, pattern='^start$'))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, user_response_handler))

    application.run_polling()

if __name__ == '__main__':
    main()
