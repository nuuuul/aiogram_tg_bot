from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards.client_kb import kb_client, inkb, ikb_client_menu, ikb_search, ikb_links, ikb_back
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
from data_base import sqlite_db
from aiogram.dispatcher.filters import Text

answ = dict()

#@dp.message_handler(commands=['Начать', 'Задать_вопрос'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id,
                               text = 'Добро пожаловать\n'
                               'Это тестовый бот для демонстрации и экпериментов\n'
                               'Ничего особенного в нем нет, но код оставлю открытым (можно найти на гитхабе)'
                               '.......................................................... \n'
                               '                                                          _nuul',
                               reply_markup= ikb_client_menu)
        await message.delete()
    except:
        await message.reply("Общение с ботом через ЛС, напишите ему:\nhttps://t.me/lalalallatestbot")

#@dp.message_handler(commands=['Указать_город'])
async def command_SetCity(message : types.Message):
    await bot.send_message(message.from_user.id, 'мне похуй', reply_markup=ReplyKeyboardRemove())

#@dp.message_handler(commands=['DataBase'])
async def DataBase_command(message : types.Message):
    await sqlite_db.sql_read(message)


#Вызов инлайн кнопки
#@dp.message_handler(Text(startswith='like_'))
async def test_command(message : types.Message):
    await message.answer('Лизер лучший репер россии', reply_markup=inkb)

#Тест инлайн кнопки
#@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали', show_alert=True)


########################inline client keyboard callbacks##################

# @dp.callback_query_handler(text = 'search')
async def search_call(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Раздел в разработке',
                                  reply_markup=ikb_search)
    await callback.message.delete()

# @dp.callback_query_handler(text = 'db')
async def db_call(callback : types.CallbackQuery):
    await sqlite_db.sql_read(callback)
    await callback.message.answer(text = 'Раздел дополняется', reply_markup=ikb_back)
    await callback.message.delete()

# @dp.callback_query_handler(text = 'links')
async def links_call(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Ссылки: ', reply_markup=ikb_links)
    await callback.message.delete()

# @dp.callback_query_handler(text = 'description')
async def desc_call(callback : types.CallbackQuery):
    await callback.message.answer('database: SQLite\n'
                                  'bot_id: lalalallatestbot\n'
                                  'framework: aiogram\n'
                                  'code by _nuul', reply_markup=ikb_back)
    await callback.message.delete()

# @dp.callback_query_handler(text = 'start')
async def start_call(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Добро пожаловать\n'
                           'Это тестовый бот для демонстрации и экпериментов\n'
                           'Ничего особенного в нем нет, но код оставлю открытым (можно найти на гитхабе)'
                           '.......................................................... \n'
                           '                                                          _nuul',
                           reply_markup= ikb_client_menu)
    await callback.message.delete()

# @dp.callback_query_handler(text = 'kb_open')
async def kb_call(callback : types.CallbackQuery):
    await callback.answer(text='клавиатура открыта')
    await callback.message.answer(text=':)' , reply_markup=kb_client)


########################kb_search callbacks##########################

# @dp.callback_query_handler(text = ['city', 'activity', 'price'])
async def search_kb_call(callback : types.CallbackQuery):
    await sqlite_db.sql_read_param(callback)





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'Начать'])
    dp.register_message_handler(command_SetCity, commands=['Указать_город'])
    dp.register_message_handler(DataBase_command, commands=['DataBase'])
    dp.register_message_handler(test_command, commands='test')

    dp.register_callback_query_handler(www_call, Text(startswith='like_'))
    dp.register_callback_query_handler(search_call, text = 'search')
    dp.register_callback_query_handler(db_call, text = 'db')
    dp.register_callback_query_handler(links_call, text = 'links')
    dp.register_callback_query_handler(desc_call, text='description')
    dp.register_callback_query_handler(start_call, text = 'start')
    dp.register_callback_query_handler(kb_call, text = 'kb_open')

    dp.register_callback_query_handler(search_kb_call, text = ['city', 'activity', 'price'])