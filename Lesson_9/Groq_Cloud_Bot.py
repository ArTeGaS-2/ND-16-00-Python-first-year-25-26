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
GROCLOUD_ENDPOINT = 'https://api.groq.com/openai/v1/chat/completions'

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
    history = context.user_data.setdefault(
    "history",
    [{"role": "system", "content": "Ти корисний асистент. Відповідаєш Українською."}])
    # Додаємо історію повідомлень користувача
    history.append({"role": "user", "context": user_input})

        # --- SANITIZE HISTORY: прибрати будь-які зайві поля типу "context" ---
    cleaned = []
    for m in history:
        if isinstance(m, dict):
            cleaned.append({
                "role": m.get("role", "user"),
                "content": str(m.get("content", ""))  # тільки content
            })
        else:
            cleaned.append({"role": "user", "content": str(m)})

    history[:] = cleaned
    context.user_data["history"] = history


    # Формуємо JSON_payload для запиту до Groqcloud
    payload = {
        "model": "openai/gpt-oss-120b",
        "messages": history}
    
    headers = {
        "Authorization": f"Bearer {GROCLOUD_API_KEY}",
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient(timeout=30.0) as client:
        try:
            response = await client.post(GROCLOUD_ENDPOINT, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()

            reply = data["choices"][0]["message"]["content"].strip()
            history.append({"role": "assistant", "content": reply})
            await update.message.reply_text(reply)

        except httpx.HTTPStatusError as e:
            # Оце найважливіше: покаже реальну причину 400/401/429 і т.д.
            body = e.response.text
            await update.message.reply_text(
                f"HTTP {e.response.status_code}: {body[:3500]}"
            )

        except httpx.RequestError as e:
            await update.message.reply_text(f"Network error: {e}")

def main():
    TOKEN = ""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

    app.run_polling()

if __name__ == "__main__":
    main()