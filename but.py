from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

b1 = KeyboardButton("Записаться на стирку")
b2 = KeyboardButton("Мои записи")
b3 = KeyboardButton("Отмена записи")
b4 = KeyboardButton("Список на стирку")

keybrd = ReplyKeyboardMarkup(resize_keyboard=True)

keybrd.add(b1).insert(b2).add(b3).insert(b4)

i1 = InlineKeyboardButton("19:00-20:00", callback_data="19:00-20:00")
i2 = InlineKeyboardButton("20:00-21:00", callback_data="20:00-21:00")
i3 = InlineKeyboardButton("21:00-22:00", callback_data="21:00-22:00")
i4 = InlineKeyboardButton("22:00-23:00", callback_data="22:00-23:00")
i5 = InlineKeyboardButton("23:00-00:00", callback_data="23:00-23:59")
i6 = InlineKeyboardButton("00:00-01:00", callback_data="23:59-01:00")

inlinekb1 = InlineKeyboardMarkup(row_width=3).add(i1, i2, i3, i4, i5, i6)
