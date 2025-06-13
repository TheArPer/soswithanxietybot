import asyncio
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode

# 🔐 Вставь свой токен ниже
TOKEN = '7219163362:AAHjbwOduZRMcgjKc7uP33xMLMbZgjSbpeQ'

# Список героев без сленга
heroes = [
    "Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe", "Bane", "Batrider",
    "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster", "Bristleback", "Broodmother", "Centaur Warrunner",
    "Chaos Knight", "Chen", "Clinkz", "Clockwerk", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dawnbreaker",
    "Dazzle", "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger", "Earth Spirit", "Earthshaker",
    "Elder Titan", "Ember Spirit", "Enchantress", "Enigma", "Faceless Void", "Grimstroke", "Gyrocopter", "Hoodwink",
    "Huskar", "Invoker", "Io", "Jakiro", "Juggernaut", "Keeper of the Light", "Kunkka", "Legion Commander",
    "Leshrac", "Lich", "Lifestealer", "Lina", "Lion", "Lone Druid", "Luna", "Lycan", "Magnus", "Marci", "Mars",
    "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Muerta", "Naga Siren", "Nature's Prophet",
    "Necrophos", "Night Stalker", "Nyx Assassin", "Ogre Magi", "Omniknight", "Oracle", "Outworld Destroyer",
    "Pangolier", "Phantom Assassin", "Phantom Lancer", "Phoenix", "Primal Beast", "Puck", "Pudge", "Pugna",
    "Queen of Pain", "Razor", "Riki", "Rubick", "Sand King", "Shadow Demon", "Shadow Fiend", "Shadow Shaman",
    "Silencer", "Skywrath Mage", "Slardar", "Slark", "Snapfire", "Sniper", "Spectre", "Spirit Breaker",
    "Storm Spirit", "Sven", "Techies", "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker",
    "Tiny", "Treant Protector", "Troll Warlord", "Tusk", "Underlord", "Undying", "Ursa", "Vengeful Spirit",
    "Venomancer", "Viper", "Visage", "Void Spirit", "Warlock", "Weaver", "Windranger", "Winter Wyvern",
    "Witch Doctor", "Wraith King"
]

# 🔘 Кнопка
def get_check_button():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔮 Проверить, кто я из Dota 2", callback_data="check_hero")]
    ])
    return keyboard

# 🚀 Инициализация
bot = Bot(token=TOKEN)
dp = Dispatcher()

# 🟢 Команда /start
@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(
        "👤 Какой ты персонаж из Dota 2?",
        reply_markup=get_check_button()
    )

# 🎲 Ответ на кнопку
@dp.callback_query(F.data == "check_hero")
async def check_hero(callback: types.CallbackQuery):
    hero = random.choice(heroes)
    await callback.message.answer(f"🧝 Ты — *{hero}*!", parse_mode=ParseMode.MARKDOWN, reply_markup=get_check_button())
    await callback.answer()  # Закрыть "загрузка..." в Telegram

# 🏁 Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
