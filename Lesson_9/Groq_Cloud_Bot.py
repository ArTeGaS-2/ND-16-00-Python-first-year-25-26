import httpx
from telegram import Update
from telegram.ext import (Application,
                        CommandHandler,
                        MessageHandler,
                        ContextTypes,
                        filters)

# Ключ API
GROCLOUD_API_KEY = ""
# URL API
GROCLOUD_ENDPOINT = 'https://api.groq.com/openai/v1/chat/comletions'

async def start(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """ Обробник команди /start """
    context.user_data["history"] = [{"role": "system",
        "content":"Ти корисний асистент. Відповідаєш Українською"}]
    await update.message.reply_text(
        "Привіт! Починаємо спілкування. Напиши щось.")
    
async def chat(update: Update, context:ContextTypes.DEFAULT_TYPE):
    """ Обробник текстових повідомлень """
    user_input = update.message.text.strip()

    # Історія діалогу
    history = context.user_data.get("history", [])
    # Додаємо історію повідомлень користувача
    history.append({"role": "user", "context": user_input})

    # Формуємо JSON_payload для запиту до Groqcloud
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": history}
    
    headers = {
        "Authorization": f"Bearer {GROCLOUD_API_KEY}",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                GROCLOUD_ENDPOINT, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            reply = data["choices"][0]["message"]["content"].strip()
            history.append({"role": "assistant", "content": reply})

            await update.message.reply_text(reply)
        except Exception as e:
            await update.message.reply_text(f"Виникла проблема: {e}")