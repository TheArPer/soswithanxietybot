
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
import logging
import random

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен бота и ID разрешенного пользователя
BOT_TOKEN = "8029084450:AAH4IUjx1rbibQObjJol-tgFIGGEF4szInk"
OWNER_ID = 6061172356

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Список советов и мотиваций
tips = [
    "Сделай глубокий вдох. Ты справишься.",
    "Не будь к себе строгим — ты уже делаешь максимум.",
    "Иногда лучший способ справиться — просто позволить себе отдохнуть.",
    "Проблемы — это временно. Ты сильнее, чем они.",
    "Ты не один. Я рядом."
]

motivations = [
    "Ты молодец, что не сдаешься.",
    "Ты растешь каждый день, даже если не замечаешь этого.",
    "Мир нуждается в тебе именно таким, какой ты есть.",
    "Двигайся в своем темпе. Главное — не останавливаться.",
    "Ты способен на большее, чем думаешь."
]

# Проверка пользователя
async def check_owner(message: Message):
    if message.from_user.id != OWNER_ID:
        await message.answer("Извини, этот бот только для моего создателя.")
        return False
    return True

@dp.message(Command("start"))
async def start(message: Message):
    if not await check_owner(message): return
    await message.answer(
        "Привет, это твой личный антистресс-бот **MyBestHelper**.

"
        "Вот что я умею:
"
        "/calm — техника дыхания
"
        "/tip — совет от меня
"
        "/journal — выплесни мысли
"
        "/mood — поделись настроением
"
        "/motivate — мотивашка"
    )

@dp.message(Command("calm"))
async def calm(message: Message):
    if not await check_owner(message): return
    await message.answer("Давай вместе подышим:

Вдохни на 4...
Задержи на 7...
Выдохни на 8...

Повтори это 3 раза. Ты молодец.")

@dp.message(Command("tip"))
async def tip(message: Message):
    if not await check_owner(message): return
    await message.answer(random.choice(tips))

@dp.message(Command("motivate"))
async def motivate(message: Message):
    if not await check_owner(message): return
    await message.answer(random.choice(motivations))

@dp.message(Command("journal"))
async def journal(message: Message):
    if not await check_owner(message): return
    await message.answer("Напиши сюда всё, что у тебя внутри. Я не буду сохранять — просто выговорись.")

@dp.message(Command("mood"))
async def mood(message: Message):
    if not await check_owner(message): return
    await message.answer("Как ты сейчас себя чувствуешь по шкале от 1 до 10?
(1 — ужасно, 10 — отлично)")

@dp.message()
async def default_response(message: Message):
    if not await check_owner(message): return
    await message.answer("Я тебя слышу. Просто знай: ты не один.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
