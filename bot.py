import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = "🔥 Спасибо за пост!"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def auto_comment(message: types.Message):
    # Не отвечаем сами себе
    if message.from_user.id == bot.id:
        return
    
    # Если сообщение является ответом на другое сообщение - это комментарий, пропускаем
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий от {message.from_user.first_name}")
        return
    
    # Иначе - это новый пост, отвечаем
    await message.reply(COMMENT_TEXT)
    print(f"✅ Ответил на пост от {message.from_user.first_name}")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает только на новые посты (игнорирует комментарии)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())