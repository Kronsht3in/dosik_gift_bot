import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import BufferedInputFile  # <-- Импортируем новый класс

TOKEN = "8683122770:AAEUMZjVAbG2Ray3Fv4FHWOK8jn3WLtJrpA"
COMMENT_TEXT = """Не забывайте комментить и ставить реакции, ведь так вы повышаете шанс забрать халявного мишку 🤍

Носителей наших эмодзи и авок частенько радуем подарочками с росписью 🎁"""

# ЗАГРУЖАЕМ ФОТО КАК БАЙТОВЫЙ МАССИВ (РАБОТАЕТ ВСЕГДА)
try:
    with open("image.jpg", "rb") as photo_file:
        PHOTO_BYTES = photo_file.read()
    PHOTO_INPUT = BufferedInputFile(PHOTO_BYTES, filename="image.jpg")
    print("✅ Фото успешно загружено")
except FileNotFoundError:
    print("❌ Ошибка: файл image.jpg не найден!")
    PHOTO_INPUT = None

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаём кнопки
keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🎁 Повышенный приз", url="https://t.me/DosikGIFTS/11423")],
    [InlineKeyboardButton(text="⭐ Звезды от Досика", url="https://t.me/Dosik_stars_bot")],
    [InlineKeyboardButton(text="📺 Наш твич", url="https://www.twitch.tv/")],
    [InlineKeyboardButton(text="💬 Наш чатик", url="https://t.me/chatik_DOSIK")],
])

# Ссылки на эмодзи и авки
EMOJI_LINK = "https://t.me/addemoji/DOSIK_emoji"
AVATAR_LINK = "https://t.me/EMOJI_DOSIK"

@dp.message()
async def auto_comment(message: types.Message):
    # Не отвечаем сами себе
    if message.from_user.id == bot.id:
        return
    
    # Если сообщение является ответом на другое сообщение - это комментарий, пропускаем
    if message.reply_to_message is not None:
        print(f"⏩ Пропустил комментарий от {message.from_user.first_name}")
        return
    
    # Формируем текст со ссылками
    full_text = f"""{COMMENT_TEXT}

[Эмодзи]({EMOJI_LINK}) и [авы]({AVATAR_LINK}) — подписывайтесь, чтобы не пропустить раздачи 🎀"""
    
    # Отправляем ФОТО + текст + кнопки
    if PHOTO_INPUT:
        await message.reply_photo(
            photo=PHOTO_INPUT,
            caption=full_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    else:
        # Если фото не загрузилось, отправляем только текст
        await message.reply(
            full_text,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    print(f"✅ Ответил на пост от {message.from_user.first_name}")

async def main():
    print("🚀 Бот запущен!")
    print("📢 Отвечает только на новые посты (игнорирует комментарии)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
