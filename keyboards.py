from aiogram import types
from config import *


kb_admin_panel = types.InlineKeyboardMarkup(row_width=2)
ka1 = types.InlineKeyboardButton(text="СЕРВЕРА",callback_data="servers")
ka2 = types.InlineKeyboardButton(text="БАЛАНС",callback_data="a_balance")
ka3 = types.InlineKeyboardButton(text="РЕБУТ ВСЕГО",callback_data="allreboot")
kb_admin_panel.add(ka1,ka2,ka3)



kb_admin_back = types.InlineKeyboardMarkup(row_width=2)
kab1 = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backad")
kb_admin_back.add(kab1)


keyboard_start = types.InlineKeyboardMarkup(row_width=2)
k1 = types.InlineKeyboardButton(text="ПОДКЛЮЧЕНИЕ",callback_data="connect")
k2 = types.InlineKeyboardButton(text="ПОДПИСКА",callback_data="podpiska")
k3 = types.InlineKeyboardButton(text="БАЛАНС",callback_data="balance")
k4 = types.InlineKeyboardButton(text="ПРИГЛАСИТЬ",callback_data="invite")
k5 = types.InlineKeyboardButton(text="ПОМОЩЬ",callback_data="help")
keyboard_start.add(k1).row(k2,k3).row(k4).row(k5)

kb_konf = types.InlineKeyboardMarkup(row_width=1)
kf1 = types.InlineKeyboardButton(text="АКТИВНЫЕ ПОДПИСКИ",callback_data="mycfg")
kf2 = types.InlineKeyboardButton(text="ПРИОБРЕСТИ ПОДПИСКУ",callback_data="addcfg")
backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
kb_konf.add(kf1,kf2,backbtn)


kb_admin = types.InlineKeyboardMarkup(row_width=1)
kb_admin1 = types.InlineKeyboardButton(text="👨‍💻 АДМИНИСТРАЦИЯ 👨‍💻",url=support)
kb_admin.add(kb_admin1)




kb_back = types.InlineKeyboardMarkup(row_width=1)
backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
kb_back.add(backbtn)
kb_backmain = types.InlineKeyboardMarkup(row_width=1)
backbtnmain = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="startphoto")
kb_backmain.add(backbtnmain)

kb_insts = types.InlineKeyboardMarkup(row_width=2)
kis1 = types.InlineKeyboardButton(text="🍏 IOS",url="https://teletype.in/@flashvpn/Ios")
kis2 = types.InlineKeyboardButton(text="🤖 ANDROID",url="https://teletype.in/@flashvpn/Android")
kis3 = types.InlineKeyboardButton(text="🪟 WINDOWS",url="https://teletype.in/@flashvpn/Windows")
kis5 = types.InlineKeyboardButton(text="💻 MacOS",url="https://teletype.in/@flashvpn/MacOs")
backbtns = types.InlineKeyboardButton(text="ГЛАВНАЯ ◀️",callback_data="backsts")
kb_insts.add(kis1,kis2,kis3,kis5).row(backbtns)


kb_backststttttt = types.InlineKeyboardMarkup(row_width=1)
backbtns = types.InlineKeyboardButton(text="ГЛАВНАЯ ◀️",callback_data="backsts_1")
kb_backststttttt.add(backbtns)
kb_help= types.InlineKeyboardMarkup(row_width=1)
kh1 = types.InlineKeyboardButton(text="Частые вопросы",callback_data="h1")
kh2 = types.InlineKeyboardButton(text="Саппорт",url=support)
backbtns = types.InlineKeyboardButton(text="ГЛАВНАЯ ◀️",callback_data="backsts")
kb_help.add(kh1,kh2,backbtns)

kb_instss = types.InlineKeyboardMarkup(row_width=2)
kis1s = types.InlineKeyboardButton(text="🍏 IOS",url="https://telegra.ph/IOS-Nastrojka-11-24-3")
kis2s = types.InlineKeyboardButton(text="🤖 ANDROID",url="https://telegra.ph/Android-Nastrojka-11-24")
kis3s = types.InlineKeyboardButton(text="🪟 WINDOWS",url="https://telegra.ph/Windows-nastrojka-11-24")
kis5s = types.InlineKeyboardButton(text="💻 MacOS",url="https://telegra.ph/MacOs-Nastrojka-11-24")
backbtns = types.InlineKeyboardButton(text="ГЛАВНАЯ ◀️",callback_data="backsts_1")
kb_instss.add(kis1s,kis2s,kis3s,kis5s).row(backbtns)

kb_tarif = types.InlineKeyboardMarkup(row_width=1)
kt1 = types.InlineKeyboardButton(text="📆 1 МЕСЯЦ - 79",callback_data="t1")
kt2 = types.InlineKeyboardButton(text="📆 3 МЕСЯЦА - 229",callback_data="t2")
kt4 = types.InlineKeyboardButton(text="📆 ГОД - 899",callback_data="t4")
backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
kb_tarif.add(kt1,kt2,kt4,backbtn)


kb_balance = types.InlineKeyboardMarkup(row_width=1)
kbal1 = types.InlineKeyboardButton(text="Пополнить",callback_data="addcash")
backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
kb_balance.add(kbal1,backbtn)


kb_next =  types.InlineKeyboardMarkup(row_width=1)
kbnnne = types.InlineKeyboardButton(text="ПОЛУЧИТЬ",callback_data="freeevpn")
kb_next.add(kbnnne)


kbkanal  = types.InlineKeyboardMarkup(row_width=1)
kan1 = types.InlineKeyboardButton(text="КАНАЛ",url="https://t.me/dikavpn")
kan2 = types.InlineKeyboardButton(text="ПОДПИСАЛСЯ",callback_data="donech")
kbkanal.add(kan1,kan2)


kb_popln = types.InlineKeyboardMarkup(row_width=1)
kpp1 = types.InlineKeyboardButton(text="Пополнить",callback_data="addcash")
backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
kb_popln.add(kpp1,backbtn)

kb_ref =  types.InlineKeyboardMarkup(row_width=1)
kr = types.InlineKeyboardButton(text="Вывод",callback_data="refvivod")
kb_ref.add(kr,backbtn)



kb_backstst =  types.InlineKeyboardMarkup(row_width=1)
backbtnstst = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backststst")
kb_backstst.add(backbtnstst)





kb_select_amount = types.InlineKeyboardMarkup(row_width=3)
kb_select_amount.add(
    types.InlineKeyboardButton(text="79 руб.", callback_data="amount_79"),
    types.InlineKeyboardButton(text="229 руб.", callback_data="amount_229"),
    types.InlineKeyboardButton(text="899 руб.", callback_data="amount_899")
)
kb_select_amount.add(
    types.InlineKeyboardButton(text="Ввести вручную", callback_data="amount_manual"),
    types.InlineKeyboardButton(text="НАЗАД ◀️", callback_data="backst")
)