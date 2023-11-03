import asyncio
import logging
from aiogram import Dispatcher, Bot, types
from aiogram.filters.command import Command
from config import API_KEY, MSG_START, MSG_COMMAND_LIST

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_KEY, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(MSG_START.format(message.from_user.full_name))


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer(MSG_COMMAND_LIST)


@dp.message(Command("money"))
async def cmd_money(message: types.Message):
    pass


@dp.message(Command("test"))
async def cmd_money(message: types.Message):
    for item in message.entities:
        print(item)


@dp.message(Command("stat"))
async def cmd_stat(message: types.Message):
    pass


@dp.message(Command("advice"))
async def cmd_advice(message: types.Message):
    pass


@dp.message(Command("change"))
async def cmd_change(message: types.Message):
    pass


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
