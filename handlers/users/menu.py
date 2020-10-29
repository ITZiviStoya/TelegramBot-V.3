from aiogram import types
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: types.Message):
    await message.answer("Select from menu", reply_markup=menu)


@dp.message_handler(Text(equals=["Kotletki", "Makaroshki", "Pureshka"]))
async def get_food(message: types.Message):
    await message.answer(f"You chosen{message.text}. Ty",
                         reply_markup=types.ReplyKeyboardRemove())
