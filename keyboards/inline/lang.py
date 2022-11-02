from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

laguage =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"),
        InlineKeyboardButton(text="🇹🇷 Türk", callback_data="turk")
    ]
]
)

laguageuz =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha ✅", callback_data="uzb"),
        InlineKeyboardButton(text="🇹🇷 Türk", callback_data="turk")
    ]
]
)

laguageen =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English ✅", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"),
        InlineKeyboardButton(text="🇹🇷 Türk", callback_data="turk")
    ]
]
)

laguageru =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺 Русский ✅", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"),
        InlineKeyboardButton(text="🇹🇷 Türk", callback_data="turk")
    ]
]
)

laguagetk =InlineKeyboardMarkup(
inline_keyboard=[
    [
        InlineKeyboardButton(text="🇬🇧 English", callback_data="eng"),
        InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus")
    ],
    [
        InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"),
        InlineKeyboardButton(text="🇹🇷 Türk ✅", callback_data="turk")
    ]
]
)