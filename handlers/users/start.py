from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command, Text
from loader import dp
from keyboards.default import menu


@dp.message_handler(Command("start"))
async def show_menu(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!' +
                         "\n Я - бот компании Живи Стоя \n Жмакай кнопку для инфы", reply_markup=menu)


@dp.message_handler(Text(equals="Почему живи стоя?"))
async def get_food(message: types.Message):
    await message.answer("Гиподинамия, ССД, гайморит, бла бла.. суставы,шея."
                         " Растущий стул, конторка.\nКомплиментарная пиццуля по пятницам")


@dp.message_handler(Text(equals="Код от дверей"))
async def get_food(message: types.Message):
    await message.answer("6709 или 0112 \n *Коды вымышленные и меняются каждый день")


@dp.message_handler(Text(equals="Сайт"))
async def get_food(message: types.Message):
    await message.answer("живистоя.рф")


@dp.message_handler(Text(equals="Адрес"))
async def get_food(message: types.Message):
    await message.answer("СПБ, ул. Тельмана д. 16.\nОриентир - бюст Тельмана, грязища и превосходный аромат пивзавода.")
