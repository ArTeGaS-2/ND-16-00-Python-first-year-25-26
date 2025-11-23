# pip install OpenAI

import openai
from telegram import Update
from telegram.ext import (Application,
                        CommandHandler,
                        MessageHandler,
                        ContextTypes,
                        filters)

openai.api_key = ""
TOKEN = ""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Починаємо спілкування. Напиши своє повідомлення:"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Обробник текстових повідомлень.
    Додає повідомлення користувача в історію, надсилає запит до OpenAI та повертає відповідь.
    """
    user_text = update.message.text
    try:
        # Асинхронно надсилаємо запит до OpenAI.
        response = openai.ChatCompletion.create(
            model="gpt-5.1",
            messages=[
                {"role": "system", "content": "Ти дівчина чарівниця."},
                {"role": "user", "content": user_text}
            ]
        )
        # Отримуємо відповідь від моделі.
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"Виникла помилка: {e}"
    await update.message.reply_text(reply)
def main():
    """Основан функція запуску боту"""
    TOKEN = "8007498060:AAEsmpsDhAACsZKlOBkGl8ltZG5Nhg8StRs"
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()