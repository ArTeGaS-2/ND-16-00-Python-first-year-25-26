# pip install OpenAI

import openai
from telegram import Update
from telegram.ext import (Application,
                        CommandHandler,
                        MessageHandler,
                        ContextTypes,
                        filters)

openai.api_key = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обробник команди /start.
    Ініціалізує історію діалогу для користувача та надсилає вітальне повідомлення.
    """
    # Ініціалізуємо історію, додаючи системне повідомлення, яке задає тон діалогу.
    context.user_data["history"] = [{"role": "system", "content": "You are a helpful assistant."}]
    await update.message.reply_text(
        "Привіт! Починаємо спілкування з моделлю o4-mini від OpenAI. Напиши своє повідомлення:"
    )

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обробник текстових повідомлень.
    Додає повідомлення користувача в історію, надсилає запит до OpenAI та повертає відповідь.
    """
    user_input = update.message.text.strip()
    
    # Отримуємо поточну історію діалогу або створюємо нову, якщо її немає.
    history = context.user_data.get("history", [])
    # Додаємо повідомлення користувача до історії.
    history.append({"role": "user", "content": user_input})
    
    try:
        # Асинхронно надсилаємо запит до OpenAI.
        response = await openai.ChatCompletion.acreate(
            model="gpt-4o-mini",
            messages=history
        )
        # Отримуємо відповідь від моделі.
        reply = response.choices[0].message.content.strip()
        # Додаємо відповідь моделі до історії діалогу.
        history.append({"role": "assistant", "content": reply})
        
        # Надсилаємо відповідь користувачу.
        await update.message.reply_text(reply)
    except Exception as e:
        # У разі помилки виводимо повідомлення про помилку.
        await update.message.reply_text(f"Виникла помилка: {e}")