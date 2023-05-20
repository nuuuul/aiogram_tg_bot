from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,\
                            InlineKeyboardButton, InlineKeyboardMarkup



ib_load = InlineKeyboardButton(text = 'Загрузить', callback_data = 'load')
ib_delete = InlineKeyboardButton(text = 'Управление', callback_data = 'delete')
ib_cancel = InlineKeyboardButton(text = 'Выйти', callback_data = 'close')

ikb_case_admin = InlineKeyboardMarkup(row_width=2)
ikb_case_admin.row(ib_load, ib_delete).add(ib_cancel)


#Кнопки клавиатуры админа
button_load = KeyboardButton('/Загрузить')
button_delete = KeyboardButton('/Удалить')
button_cancel = KeyboardButton('/отмена')

kb_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).\
    add(button_load).add(button_delete).add(button_cancel)