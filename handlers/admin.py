from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.client_kb import ikb_client_menu



ID = None


class FSMAdmin(StatesGroup):
    activity = State()
    city = State()
    price = State()


#Получаем ID текущего модератора
#@dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message : types.Message):
    global ID 
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо???', reply_markup=admin_kb.ikb_case_admin)
    await message.delete()


#Начало диалога загрузки нового пункта меню
#@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.activity.set()
        await message.reply('Запишите активность')

#Выход из состояний
#@dp.message_handler(state="*", commands='отмена')
#@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message : types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')

#Запись первого ответа в словарь
#@dp.message_handler(state=FSMAdmin.activity)
async def load_activity(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['activity'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите город")

#Запись второго ответа в словарь
#@dp.message_handler(state=FSMAdmin.city)
async def load_city(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['city'] = message.text
        await FSMAdmin.next()
        await message.reply("Введите цену")


#Запись третьего ответа в словарь
#@dp.message_handler(state = FSMAdmin.price)
async def load_price(message : types.Message, state = FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)

        await sqlite_db.sql_add_command(state)
        await state.finish()

#Удаление итема из словаря
#@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} удалена', show_alert=True)


# @dp.callback_query_handler(text= 'load')
async def load_call(callback : types.CallbackQuery):
        if callback.message.from_user.id == ID:
            await FSMAdmin.activity.set()
            await callback.message.answer('Запишите активность')

# @dp.callback_query_handler(text = 'delete')
async def delete_call(callback : types.CallbackQuery):
    if callback.message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_message(callback.message.from_user.id, 
                                   f'Активность: {ret[1]}\nГород: {ret[0]}\nЦена: {ret[2]}')
            await bot.send_message(callback.message.from_user.id, 
                                   text='^^^', reply_markup=InlineKeyboardMarkup().\
                                   add(InlineKeyboardButton(f'Удалить {ret[1]}',
                                                            callback_data=f'del {ret[1]}')))
            
async def close_call(callback : types.CallbackQuery):
    await callback.message.answer(text = 'Добро пожаловать\n'
                           'Это тестовый бот для демонстрации и экпериментов\n'
                           'Ничего особенного в нем нет, но код оставлю открытым (можно найти на гитхабе)'
                           '.......................................................... \n'
                           '                                                          _nuul',
                           reply_markup= ikb_client_menu)
    await callback.message.delete()



#Регистритуем хендлеры
def register_handlers_admin(dp : Dispatcher):
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state="*", commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(load_activity, state = FSMAdmin.activity)
    dp.register_message_handler(load_city, state=FSMAdmin.city)
    dp.register_message_handler(load_price, state = FSMAdmin.price)
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))

    dp.register_callback_query_handler(load_call, text = 'load')
    dp.register_callback_query_handler(delete_call, text = 'delete')
    dp.register_callback_query_handler(close_call, text = 'close')