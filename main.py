# from db import *
# import utils
# from datetime import datetime
# from aiogram import Bot, Dispatcher, types
# from aiogram.types import ParseMode
# from aiogram import executor
# from config import *
# from keyboards import *
# import time
# import asyncio, json, logging, qrcode, random, re, sqlite3, string, datetime
# from datetime import datetime as dt
# from io import BytesIO
# from aiogram import Bot, Dispatcher, executor, types
# from aiogram.types import ParseMode, User
# from aiogram.types.message import ContentType
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from aiogram.dispatcher.filters.state import State, StatesGroup
# from aiogram.dispatcher import FSMContext
# from logging.handlers import RotatingFileHandler
# import aiohttp
# from config import TOKEN
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# import asyncio
# import datetime

# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot, storage=MemoryStorage())
# variable = utils.Variable()


# @dp.message_handler(commands=['admin'])
# async def admin_panel(message: types.Message):
#     if message.chat.id == admin_id:
#         a = allusers()
#         await bot.send_message(message.chat.id, f"АДМИН ПАНЕЛЬ\n\nВСЕГО КОНФИГОВ {a}",reply_markup=kb_admin_panel)

# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     add = checkuser(message.chat.id)
#     if add:
#         await bot.send_photo(chat_id=message.chat.id,photo=open('start.png', 'rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

#     else:
       
#         referral_code = message.text[7:]
#         print(referral_code)
#         if len(referral_code)>2:
#             adduserref(message.chat.id,referral_code)
#         else:
#             adduser(message.chat.id)
        
#         await bot.send_message(message.chat.id, f"Привет! {message.from_user.username}\nВижу ты тут впервые. У нас для ТЕБЯ подарочный впн на 7 ДНЕЙ\nНажми кнопку ниже что бы им воспользоваться",reply_markup=kb_next)
        





# @dp.callback_query_handler(lambda call: True)
# async def print_all_commands(call: types.CallbackQuery):
#     if call.data == "try3":
#       session_id = await login()
#       if session_id:
#           telegram_id = call.message.from_user.id
          
#           user = trialcheck(telegram_id)

#           if user:
#               await call.message.answer("❌ Вам уже выдавался пробный период 🧐")
#               bot_logger.info(f"Пользователь {telegram_id} попытался повторно использовать пробный период.")
#           else:
#               id_vless = 1
#               email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
#               expiry_time = -259200000
#               await call.message.answer(f"✅ Пробный период активирован! \nВаш логин: {email}")
#               #await add_client(call.message, email, expiry_time, id_vless, call.message.from_user.id)
#               bot_logger.info(f"Пользователь {call.message.from_user.id} начал использовать пробный период.")
#       else:
#           await call.message.answer("❌ Ошибка аутентификации.")
#           bot_logger.error("Ошибка аутентификации при попытке начала пробного периода.")
#     elif call.data == "freeevpn":
#         await bot.send_message(call.message.chat.id,"Подпишись на наш Телеграмм канал и сразу получи бесплатный VPN",reply_markup=kbkanal)
#     elif call.data == "podpiska":
#         try:
#             a = getactualdata(call.message.chat.id)
#             print(a)
#             ip = getipfromemail(a)
#             url = f"http://{ip}:22054/login"
#             session = await sessionid(url)
#             day = await listall(ip, session, a)
#             if day != None:
#                 kb_prodlenye = types.InlineKeyboardMarkup(row_width=1)
#                 kp1 = types.InlineKeyboardButton(text="📆 1 МЕСЯЦ - 149",callback_data=f"t1_{a}")
#                 kp2 = types.InlineKeyboardButton(text="📆 3 МЕСЯЦА - 339",callback_data=f"t2_{a}")
#                 kp4 = types.InlineKeyboardButton(text="📆 ГОД - 1139",callback_data=f"t4_{a}")
#                 backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
#                 kb_prodlenye.add(kp1,kp2,kp4,backbtn)
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Активно до {day}\nПродление доступно по кнопкам ниже",reply_markup=kb_prodlenye,parse_mode="html")
#             else:
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Подписки нет, приобрести можно по кнопкам ниже",reply_markup=kb_tarif,parse_mode="html")
#         except:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Подписки нет, приобрести можно по кнопкам ниже",reply_markup=kb_tarif,parse_mode="html")

    
#     elif call.data == "mycfg":
#         cfgs = selectcfg(call.message.chat.id)
#         print(cfgs)
#         keyboard = InlineKeyboardMarkup()
        
#         # Перебираем массив кортежей
#         for item in cfgs:
#             # item[0] содержит текст и callback_data
#             button = InlineKeyboardButton(text=item[0], callback_data=item[0])
#             keyboard.add(button)
#         backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
#         keyboard.add(backbtn)
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>🍏 АКТИВНЫЕ VPN ПОДКЛЮЧЕНИЯ</b>",reply_markup=keyboard,parse_mode="html")
#     elif call.data == "donech":
#         free = checkfree(call.message.chat.id)
#         print(free)
#         if free != "1":
#             result =  await is_user_subscribed(call.message.chat.id)
#             if result:
#                 unoxxx = print_and_convert_to_unix(7)
#                 mail = generate_key()
#                 url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
#                 print(url,session)
#                 vless_cfg = createcfgbymail(url,session,mail)
#                 savecfg(call.message.chat.id,vless_cfg,mail)
#                 addfreecfg(call.message.chat.id)
#                 await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_instss,parse_mode="html")
#             else:
#                 await bot.answer_callback_query(callback_query_id=call.id,text= "Вы не подписались на Telegram КАНАЛ",show_alert = True)
        
#         else:
#             await bot.send_message(call.message.chat.id,"Вы уже получили пробный VPN")
#     elif call.data == "backsts_1":
#         await bot.send_photo(chat_id=call.message.chat.id,photo=open('start.png', 'rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

    
#     elif call.data == "balance":
#         bal = int(getbalance(call.message.chat.id))
#         await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"👤 Ваш id {call.message.chat.id}\n\n<b>💰 Баланс  {bal}</b>\n",reply_markup=kb_balance,parse_mode='html')
#     elif call.data == "addcash":
#         # await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"Введите сумму пополнения",reply_markup=kb_back,parse_mode='html')
#         await bot.edit_message_caption(
#         chat_id=call.message.chat.id,
#         message_id=call.message.message_id,
#         caption="Выберите сумму пополнения или введите вручную:",
#         reply_markup=kb_back,
#         parse_mode='html'
#         )
#         variable.set_action(call.message.chat.id, 2)

#     elif call.data == "addcfg":
        
#         await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>ВЫБЕРЕТЕ ВАРИАНТЫ ПОДПИСКИ 📝</b>",reply_markup=kb_tarif,parse_mode='html')
#     elif call.data == "addserver":
#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="НАПИШИТЕ IP СЕРВЕРА",reply_markup=kb_admin_back)
#         variable.set_action(call.message.chat.id,10)
#     elif call.data == "servers":
#         a = serverslist()
#         keyboard = InlineKeyboardMarkup()

#         # Перебираем массив кортежей
#         for item in a:
#             # item[0] содержит текст и callback_data
#             button = InlineKeyboardButton(text=item[0], callback_data=f"server_{item[0]}")
#             keyboard.add(button)
#         addserv = types.InlineKeyboardButton(text="ДОБАВИТЬ СЕРВЕР",callback_data="addserver")
#         backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backad")
#         keyboard.add(addserv).row(backbtn)


#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="СПИСОК АКТУАЛЬНЫХ СЕРВЕРОВ",reply_markup=keyboard)
#     elif call.data == "a_balance":
#         pass
    

#     elif call.data == "allreboot":
#         pass
#     elif call.data == "backad":
#         variable.set_action(call.message.chat.id, 0)
#         a = allusers()
        
#         await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"АДМИН ПАНЕЛЬ\n\nВСЕГО КОНФИГОВ {a}",reply_markup=kb_admin_panel)
#     elif call.data == "t1":
        
#         a = checkbal(call.message.chat.id, 149)
        
#         if a:
#             minbal(call.message.chat.id,149)
#             unoxxx = print_and_convert_to_unix(30)
#             mail = generate_key()
#             url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
#             print(url,session)
#             vless_cfg = createcfgbymail(url,session,mail)
#             savecfg(call.message.chat.id,vless_cfg,mail)
            
#             await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#         else:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        

#     elif call.data == "t2":
        
#         a = checkbal(call.message.chat.id, 339)
        
#         if a:
#             minbal(call.message.chat.id,339)
#             unoxxx = print_and_convert_to_unix(90)
#             mail = generate_key()
#             url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
#             print(url,session)
#             vless_cfg = createcfgbymail(url,session,mail)
#             savecfg(call.message.chat.id,vless_cfg,mail)
            
#             await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#         else:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        
#     elif call.data == "t3":
        
#         a = checkbal(call.message.chat.id, 619)
        
#         if a:
#             minbal(call.message.chat.id,619)
#             unoxxx = print_and_convert_to_unix(180)
#             mail = generate_key()
#             url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
#             print(url,session)
#             vless_cfg = createcfgbymail(url,session,mail)
#             savecfg(call.message.chat.id,vless_cfg,mail)
            
#             await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#         else:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        
#     elif call.data == "t4":
        
#         a = checkbal(call.message.chat.id, 1139)
        
#         if a:
#             minbal(call.message.chat.id,1139)
#             unoxxx = print_and_convert_to_unix(365)
#             mail = generate_key()
#             url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
#             print(url,session)
#             vless_cfg = createcfgbymail(url,session,mail)
#             savecfg(call.message.chat.id,vless_cfg,mail)
            
#             await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#         else:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
    

#     elif call.data =="h1":
#         await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="На данный момент собираем список часто задаваемых вопросов\n\nПри любом вопросе обратитесь к Саппорту",reply_markup=kb_back)
        
#     elif call.data == "tarif":
#       await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="<b>НА ВСЕХ ТАРИФАХ БЕЗЛИМИТНЫЙ ТРАФИК\n\nЧто вам предлагает наш VPN:\n\n🔒 Защита конфиденциальности: VPN шифрует все данные, передаваемые через интернет, что делает невозможным их перехват и чтение третьими лицами. \n📺 Доступ к заблокированному контенту: Обходите географические ограничения и получайте доступ к сайтам и сервисам, заблокированным в вашем регионе. \n🚀 Высокая скорость: Наши серверы расположены по всему миру, обеспечивая быстрое и стабильное соединение.\n🚫 Блокировка рекламы: Избавьтесь от назойливой рекламы и увеличьте скорость загрузки страниц.\n🛡️ Защита от вирусов: Наш VPN защищает ваше устройство от вредоносных программ и вирусов, которые могут попасть в систему через интернет.\n💻 Совместимость: VPN поддерживает все популярные операционные системы (Windows, MacOS, Linux, Android, iOS). \n\nСТОИМОСТЬ ТАРИФОВ:\n\n• 🗓 Месяц: 250 руб. \n• 🗓 Два месяца: 450 руб.\n• 🗓 Полгода: 1300 руб.\n• 🗓 Год: 2500 руб.</b>",reply_markup=kb_tarif,parse_mode="html")
#     elif call.data == "invite":
#         refbal = refbala(call.message.chat.id)
#         kolvoref = refuser(call.message.chat.id)
#         kb_ref_1 =  types.InlineKeyboardMarkup(row_width=1)
#         kr = types.InlineKeyboardButton(text="Вывод",callback_data="refvivod")
#         kpod = types.InlineKeyboardButton(text="ПОДЕЛИТЬСЯ",switch_inline_query=f"ПРЙДИ СЮДА ПАЖ {botname}?start={call.message.chat.id}")
#         backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
#         kb_ref_1.add(kr,kpod,backbtn)
        
#         await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'<b>ПАРТНЕРСКАЯ ПРОГРАММА\n\nУСЛОВИЯ:\n\nПри пополнении вашего реферала на любую сумму вы получаете 10% от суммы пополнения на ваш реферальный баланс, что бы вывести денежные средства нажмите ниже кнопку вывод и укажите сумму которую хотите вывести далее ваша заявка будет рассмотрена в течении 48 часов\n\nССЫЛКА </b><code>{botname}?start={call.message.chat.id}</code>\n\n<b>Ваш реферальный баланс {refbal}\n\nПриглашено {kolvoref}</b>',reply_markup=kb_ref_1,parse_mode="html")
#     elif call.data == "backststst":
#         variable.set_action(call.message.chat.id, 0)
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

#     elif call.data =="help":
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption="<b>Выберете пункт меню</b>",reply_markup=kb_help,parse_mode="html")
#     elif call.data == "backsts":
#         variable.set_action(call.message.chat.id, 0)
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")
#     elif call.data == "refvivod":
#         await bot.send_message(call.message.chat.id, "Введите сумму для вывода с реферальной программы и через пробел реквизиты\n\nПример (1000 79998783784 Сбербанк)",reply_markup=kb_backstst)
#         variable.set_action(call.message.chat.id,1)
#     elif call.data == "connect":
#         a = checkcfg(call.message.chat.id)
#         if a != None:
            
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>Ваша конфигурация\n\n<code>{a}</code></b>",reply_markup=kb_insts,parse_mode="html")
#         else:
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>У вас еще нет конфигурации выберете нужный тариф и нажмите кнопку ниже что бы получить конфигурацию</b>",reply_markup=kb_tarif,parse_mode="html")
    
#     elif call.data == "Ios":
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>1</b>",reply_markup=kb_back,parse_mode="html")
#     elif call.data == "Android":
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>2</b>",reply_markup=kb_back,parse_mode="html")
#     elif call.data == "Windows":
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>3</b>",reply_markup=kb_back,parse_mode="html")
#     elif call.data == "MacOs":
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>4</b>",reply_markup=kb_back,parse_mode="html")
    
#     elif call.data == "Ios_1":
#         await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>1</b>",reply_markup=kb_backststttttt,parse_mode="html")
#     elif call.data == "Android_1":
#         await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>2</b>",reply_markup=kb_backststttttt,parse_mode="html")
#     elif call.data == "Windows_1":
#         await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>3</b>",reply_markup=kb_backststttttt,parse_mode="html")
#     elif call.data == "MacOs_1":
#         await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>4</b>",reply_markup=kb_backststttttt,parse_mode="html")
    
#     elif call.data == "tarifs":
#         await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="<b>🗒 ТАРИФНЫЙ ПЛАН 🗒\n\n1 МЕСЯЦ - 149р\n\n3 МЕСЯЦА - 339р\n\nПОЛ ГОДА - 619р\n\nГОД - 1139р</b>",reply_markup=kb_back,parse_mode="html")

#     elif call.data == "startphoto":
#         await bot.send_photo(chat_id=call.message.chat.id, photo=open('start.png','rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

        
#     elif call.data == "backst":
#         variable.set_action(call.message.chat.id, 0)
#         await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")
#     else:
#         if call.data.startswith("check_"):
#             result = await check(call.data.split('_')[1])
#             val = call.data.split('_')[2]
#             if result:
#                 print(1)
#                 addbal(call.message.chat.id, val)
#                 await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Успешно зачислен баланс на сумму {val}",reply_markup=kb_backmain)
#                 a = getref(call.message.chat.id)
#                 addrefbal(a,int(int(val)//20))
#                 await bot.send_message(chat_id=a,text=f"Начислен реф баланс на сумму {int(val)//20}")
#             else:
#                 await bot.send_message(call.message.chat.id, "Ваша оплата еще не прошла\n\nЕсли возникли вопросы обратитесь к администрации",reply_markup=kb_admin)
        
#         elif call.data.startswith("prodl_"):
#             mail = call.data.split('_')[1]
#             a = getbalance(call.message.chat.id)
#             kb_prodlenye = types.InlineKeyboardMarkup(row_width=2)
#             kp1 = types.InlineKeyboardButton(text="📆 1 МЕСЯЦ - 149",callback_data=f"t1_{mail}")
#             kp2 = types.InlineKeyboardButton(text="📆 3 МЕСЯЦА - 339",callback_data=f"t2_{mail}")
#             kp3 = types.InlineKeyboardButton(text="📆 ПОЛГОДА - 619",callback_data=f"t3_{mail}")
#             kp4 = types.InlineKeyboardButton(text="📆 ГОД - 1139",callback_data=f"t4_{mail}")
#             backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
#             kb_prodlenye.add(kp1,kp2,kp3,kp4,backbtn)
#             await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"Выберете срок продления по конфигурации {mail}\n\nВаш баланс {a}",reply_markup=kb_prodlenye)
#         elif call.data.startswith("t1_"):
#             mail = call.data.split('_')[1]

#             a = checkbal(call.message.chat.id, 149)
#             if a:
#                 minbal(call.message.chat.id,149)
#                 unoxxx = print_and_convert_to_unix(30)
#                 url = getipbymail(mail)
#                 print(url)
#                 session = await sessionid(f"http://{url}:22054/login")
#                 vless_cfg = getvless(mail)
#                 ids = call.message.chat.id
#                 val = 30
#                 a = construatecfg(mail,session,url,ids,val)
#                 if a:
#                     await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 30 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#                 else:
#                     print("error updatecfg")
#             else:
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
            
#         elif call.data.startswith("t2_"):
#             mail = call.data.split('_')[1]

#             a = checkbal(call.message.chat.id, 339)
#             if a:
#                 minbal(call.message.chat.id,339)
#                 unoxxx = print_and_convert_to_unix(90)
#                 url = getipbymail(mail)
                
#                 session = await sessionid(f"http://{url}:22054/login")
#                 vless_cfg = getvless(mail)
#                 ids = call.message.chat.id
#                 val = 90
#                 print(123333333333333333333333333333333333333333333333)
#                 a = construatecfg(mail,session,url,ids,val)
#                 if a:
#                     await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 90 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#                 else:
#                     print("error updatecfg")
#             else:
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
#         elif call.data.startswith("t3_"):
#             mail = call.data.split('_')[1]

#             a = checkbal(call.message.chat.id, 619)
#             if a:
#                 minbal(call.message.chat.id,619)
#                 unoxxx = print_and_convert_to_unix(180)
#                 url = getipbymail(mail)
#                 print(url)
#                 session = await sessionid(f"http://{url}:22054/login")
#                 vless_cfg = getvless(mail)
#                 ids = call.message.chat.id
#                 val = 180
#                 a = construatecfg(mail,session,url,ids,val)
#                 if a:
#                     await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 180 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#                 else:
#                     print("error updatecfg")
#             else:
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
#         elif call.data.startswith("t4_"):
#             mail = call.data.split('_')[1]

#             a = checkbal(call.message.chat.id, 1139)
#             if a:
#                 minbal(call.message.chat.id,1139)
#                 unoxxx = print_and_convert_to_unix(365)
#                 url = getipbymail(mail)
#                 print(url)
#                 session = await sessionid(f"http://{url}:22054/login")
#                 vless_cfg = getvless(mail)
#                 ids = call.message.chat.id
#                 val = 365
#                 a = construatecfg(mail,session,url,ids,val)
#                 if a:
#                     await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 365 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
#                 else:
#                     print("error updatecfg")
#             else:
#                 await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        
#         else:
#             try:
#                 a = getvless(call.data)
#                 mail = a.split("#")[1]
#                 kb_connect = types.InlineKeyboardMarkup(row_width=1)
#                 kcc1 = types.InlineKeyboardButton(text="Инструкция",callback_data="ins")
#                 kcc2 = types.InlineKeyboardButton(text="ПОДКЛЮЧИТЬСЯ",url=f"https://vpn-connector.netlify.app/?url={a}")
#                 kcc3 = types.InlineKeyboardButton(text="Продлить",callback_data=f"prodl_{mail}")
#                 backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
#                 kb_connect.add(kcc1,kcc2,kcc3,backbtn)
#                 await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption= f"Ваша конфигурация \n\n<code>{a}</code>",reply_markup=kb_connect,parse_mode="html")
#             except:
#                 pass
# async def is_user_subscribed(user_id: int) -> bool:
#     try:
#         chat_member = await bot.get_chat_member(CHANNEL_ID, user_id)
#         return chat_member.status in ["member", "administrator", "creator"]
#     except Exception as e:
#         print(f"Ошибка: {e}")
#         return False



# @dp.message_handler(lambda message: True, content_types=['text', 'photo'])
# async def handle_text(message: types.Message):
#     text = message.text
#     action = int(variable.get_action(message.chat.id))

#     if action == 1:
#         try:
#             a = int(text.split(" ")[0])
#             print(212412412412214124412412,message.chat.id,refbala(str(message.chat.id)))
#             b = int(refbala(message.chat.id))
#             if a <= b:
#                 minref(message.chat.id,a)
#                 print("allokey")
#                 await bot.send_message(chat_id=partner_chat,text=f"Вывод Реферала {message.chat.id}\n\nНа сумму {a}\n\nПользователь @{message.from_user.username}")
#                 await bot.send_message(message.chat.id, f"Успешно создана заявка\nОжидайте ответа от администратора\nВаш реферальный баланс списан на сумму {a}",reply_markup=kb_backmain)
#             else:
#                 await bot.send_message(message.chat.id, "Не достаточно реф баланса",reply_markup=kb_backststttttt)
#                 variable.set_action(message.chat.id, 0)
#         except:
#             await bot.send_message(message.chat.id, "Не верно составлена заявка",reply_markup=kb_backststttttt)
#             variable.set_action(message.chat.id, 0)
#     elif action == 2:
#         try:
#             amount = int(text)
#             email = "963-52@mail.ru"  # Здесь нужно получить email пользователя
#             items = [
#             {
#                 "description": "Пополнение баланса",
#                 "quantity": 1,
#                 "amount": {
#                     "value": f"{amount:.2f}",
#                     "currency": "RUB"
#                 },
#                 "vat_code": 1
#             }
#         ]
        
#         # Создаем платеж с данными чека
#             payment_url, payment_id = await create(amount, message.chat.id, email, items)
#             # payment_url, payment_id = await create(amount, message.chat.id, email)
            

#             print(payment_url,payment_id)
            
#             kb_oplata = types.InlineKeyboardMarkup(row_width=1)
#             o1 = types.InlineKeyboardButton(text="ОПЛАТИТЬ",url=payment_url)
#             o2 = types.InlineKeyboardButton(text="ПРОВЕРИТЬ ОПЛАТУ",callback_data=f"check_{payment_id}_{message.text}")
#             o3 = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="startphoto")
#             kb_oplata.add(o1,o2,o3)
#             await bot.send_message(chat_id=message.chat.id,text="Оплатите по кнопке ниже, после этого проверьте оплату",reply_markup=kb_oplata)
#         except:
#             await bot.send_message(chat_id=message.chat.id,text="Не верно указана сумма пополнения",reply_markup=kb_backststttttt)

#     elif action == 10:
#         print(str(message.text))
#         addserverinlist(str(message.text))



# async def check_server():
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(SERVER_URL, ssl=False) as response:
#                 if response.status == 200:
#                     return "🟢 Сервер доступен"
#                 else:
#                     return "🔴 Сервер недоступен"
#     except aiohttp.ClientError:
#         return "🔴 Сервер в данный момент недоступен"



# #all func 
# async def login():
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.post(LOGIN_URL, data=LOGIN_DATA) as response:
#                 if response.status == 200:
#                     cookies = response.cookies
#                     session_id = cookies.get("3x-ui").value if "3x-ui" in cookies else None
#                     if session_id:
#                         bot_logger.info(f"Session ID: {session_id}")
#                         return session_id
#                     else:
#                         bot_logger.error("Session ID not found in cookies")
#                         return None
#                 else:
#                     bot_logger.error(f"Failed to log in, status code: {response.status}")
#                     return None
#     except:
#         print("HUETA")            




    


# if __name__ == '__main__':
#   # Запуск вашего цикла как асинхронной задачи
#     executor.start_polling(dp, skip_updates=True)

















































###################################################33

from db import *
import utils
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram import executor
from config import *
from keyboards import *
import time
import asyncio, json, logging, qrcode, random, re, sqlite3, string, datetime
from datetime import datetime as dt
from io import BytesIO
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode, User
from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from logging.handlers import RotatingFileHandler
import aiohttp
from config import TOKEN
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import datetime

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
variable = utils.Variable()


@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    if message.chat.id == admin_id:
        a = allusers()
        await bot.send_message(message.chat.id, f"АДМИН ПАНЕЛЬ\n\nВСЕГО КОНФИГОВ {a}",reply_markup=kb_admin_panel)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    add = checkuser(message.chat.id)
    if add:
        await bot.send_photo(chat_id=message.chat.id,photo=open('start.png', 'rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

    else:
       
        referral_code = message.text[7:]
        print(referral_code)
        if len(referral_code)>2:
            adduserref(message.chat.id,referral_code)
        else:
            adduser(message.chat.id)
        
        await bot.send_message(message.chat.id, f"Привет! {message.from_user.username}\nВижу ты тут впервые. У нас для ТЕБЯ подарочный впн на 7 ДНЕЙ\nНажми кнопку ниже что бы им воспользоваться",reply_markup=kb_next)
        





@dp.callback_query_handler(lambda call: True)
async def print_all_commands(call: types.CallbackQuery):
    if call.data == "try3":
      session_id = await login()
      if session_id:
          telegram_id = call.message.from_user.id
          
          user = trialcheck(telegram_id)

          if user:
              await call.message.answer("❌ Вам уже выдавался пробный период 🧐")
              bot_logger.info(f"Пользователь {telegram_id} попытался повторно использовать пробный период.")
          else:
              id_vless = 1
              email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))
              expiry_time = -259200000
              await call.message.answer(f"✅ Пробный период активирован! \nВаш логин: {email}")
              #await add_client(call.message, email, expiry_time, id_vless, call.message.from_user.id)
              bot_logger.info(f"Пользователь {call.message.from_user.id} начал использовать пробный период.")
      else:
          await call.message.answer("❌ Ошибка аутентификации.")
          bot_logger.error("Ошибка аутентификации при попытке начала пробного периода.")
    elif call.data == "freeevpn":
        await bot.send_message(call.message.chat.id,"Подпишись на наш Телеграмм канал и сразу получи бесплатный VPN",reply_markup=kbkanal)
    elif call.data == "podpiska":
        try:
            a = getactualdata(call.message.chat.id)
            print(a)
            ip = getipfromemail(a)
            url = f"http://{ip}:2053/login"
            session = await sessionid(url)
            day = await listall(ip, session, a)
            if day != None:
                kb_prodlenye = types.InlineKeyboardMarkup(row_width=1)
                kp1 = types.InlineKeyboardButton(text="📆 1 МЕСЯЦ - 79",callback_data=f"t1_{a}")
                kp2 = types.InlineKeyboardButton(text="📆 3 МЕСЯЦА - 229",callback_data=f"t2_{a}")
                kp4 = types.InlineKeyboardButton(text="📆 ГОД - 899",callback_data=f"t4_{a}")
                backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
                kb_prodlenye.add(kp1,kp2,kp4,backbtn)
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Активно до {day}\nПродление доступно по кнопкам ниже",reply_markup=kb_prodlenye,parse_mode="html")
            else:
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Подписки нет, приобрести можно по кнопкам ниже",reply_markup=kb_tarif,parse_mode="html")
        except:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption = f"Подписки нет, приобрести можно по кнопкам ниже",reply_markup=kb_tarif,parse_mode="html")

    elif call.data == "mycfg":
        cfgs = selectcfg(call.message.chat.id)
        print(cfgs)
        keyboard = InlineKeyboardMarkup()
        
        # Перебираем массив кортежей
        for item in cfgs:
            # item[0] содержит текст и callback_data
            button = InlineKeyboardButton(text=item[0], callback_data=item[0])
            keyboard.add(button)
        backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
        keyboard.add(backbtn)
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>🍏 АКТИВНЫЕ VPN ПОДКЛЮЧЕНИЯ</b>",reply_markup=keyboard,parse_mode="html")
    elif call.data == "donech":
        free = checkfree(call.message.chat.id)
        print(free)
        if free != "1":
            result =  await is_user_subscribed(call.message.chat.id)
            if result:
                unoxxx = print_and_convert_to_unix(7)
                mail = generate_key()
                url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
                print(url,session)
                vless_cfg = createcfgbymail(url,session,mail)
                savecfg(call.message.chat.id,vless_cfg,mail)
                addfreecfg(call.message.chat.id)
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_instss,parse_mode="html")
            else:
                await bot.answer_callback_query(callback_query_id=call.id,text= "Вы не подписались на Telegram КАНАЛ",show_alert = True)
        
        else:
            await bot.send_message(call.message.chat.id,"Вы уже получили пробный VPN")
    elif call.data == "backsts_1":
        await bot.send_photo(chat_id=call.message.chat.id,photo=open('start.png', 'rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

    
    elif call.data == "balance":
        bal = int(getbalance(call.message.chat.id))
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"👤 Ваш id {call.message.chat.id}\n\n<b>💰 Баланс  {bal}</b>\n",reply_markup=kb_balance,parse_mode='html')
    elif call.data == "addcash":
        # await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"Введите сумму пополнения",reply_markup=kb_back,parse_mode='html')
        await bot.edit_message_caption(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        caption="Выберите сумму пополнения или введите вручную:",
        reply_markup=kb_select_amount,
        parse_mode='html'
        )
        variable.set_action(call.message.chat.id, 2)

    elif call.data == "addcfg":
        
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>ВЫБЕРЕТЕ ВАРИАНТЫ ПОДПИСКИ 📝</b>",reply_markup=kb_tarif,parse_mode='html')
    elif call.data == "addserver":
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="НАПИШИТЕ IP СЕРВЕРА",reply_markup=kb_admin_back)
        variable.set_action(call.message.chat.id,10)
    elif call.data == "servers":
        a = serverslist()
        keyboard = InlineKeyboardMarkup()

        # Перебираем массив кортежей
        for item in a:
            # item[0] содержит текст и callback_data
            button = InlineKeyboardButton(text=item[0], callback_data=f"server_{item[0]}")
            keyboard.add(button)
        addserv = types.InlineKeyboardButton(text="ДОБАВИТЬ СЕРВЕР",callback_data="addserver")
        backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backad")
        keyboard.add(addserv).row(backbtn)


        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="СПИСОК АКТУАЛЬНЫХ СЕРВЕРОВ",reply_markup=keyboard)
    elif call.data == "a_balance":
        pass
    

    elif call.data == "allreboot":
        pass
    elif call.data == "backad":
        variable.set_action(call.message.chat.id, 0)
        a = allusers()
        
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"АДМИН ПАНЕЛЬ\n\nВСЕГО КОНФИГОВ {a}",reply_markup=kb_admin_panel)
    elif call.data == "t1":
        
        a = checkbal(call.message.chat.id, 79)
        
        if a:
            minbal(call.message.chat.id,79)
            unoxxx = print_and_convert_to_unix(30)
            mail = generate_key()
            url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
            print(url,session)
            vless_cfg = createcfgbymail(url,session,mail)
            savecfg(call.message.chat.id,vless_cfg,mail)
            
            await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
        else:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        

    elif call.data == "t2":
        
        a = checkbal(call.message.chat.id, 229)
        
        if a:
            minbal(call.message.chat.id,229)
            unoxxx = print_and_convert_to_unix(90)
            mail = generate_key()
            url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
            print(url,session)
            vless_cfg = createcfgbymail(url,session,mail)
            savecfg(call.message.chat.id,vless_cfg,mail)
            
            await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
        else:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        
    elif call.data == "t3":
        
        a = checkbal(call.message.chat.id, 899)
        
        if a:
            minbal(call.message.chat.id,899)
            unoxxx = print_and_convert_to_unix(180)
            mail = generate_key()
            url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
            print(url,session)
            vless_cfg = createcfgbymail(url,session,mail)
            savecfg(call.message.chat.id,vless_cfg,mail)
            
            await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
        else:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        
    elif call.data == "t4":
        
        a = checkbal(call.message.chat.id, 899)
        
        if a:
            minbal(call.message.chat.id,899)
            unoxxx = print_and_convert_to_unix(365)
            mail = generate_key()
            url,session = await add_client_request(call.message.chat.id,mail,unoxxx)
            print(url,session)
            vless_cfg = createcfgbymail(url,session,mail)
            savecfg(call.message.chat.id,vless_cfg,mail)
            
            await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Ваш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
        else:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
    

    elif call.data =="h1":
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="На данный момент собираем список часто задаваемых вопросов\n\nПри любом вопросе обратитесь к Саппорту",reply_markup=kb_back)
        
    elif call.data == "tarif":
      await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="<b>НА ВСЕХ ТАРИФАХ БЕЗЛИМИТНЫЙ ТРАФИК\n\nЧто вам предлагает наш VPN:\n\n🔒 Защита конфиденциальности: VPN шифрует все данные, передаваемые через интернет, что делает невозможным их перехват и чтение третьими лицами. \n📺 Доступ к заблокированному контенту: Обходите географические ограничения и получайте доступ к сайтам и сервисам, заблокированным в вашем регионе. \n🚀 Высокая скорость: Наши серверы расположены по всему миру, обеспечивая быстрое и стабильное соединение.\n🚫 Блокировка рекламы: Избавьтесь от назойливой рекламы и увеличьте скорость загрузки страниц.\n🛡️ Защита от вирусов: Наш VPN защищает ваше устройство от вредоносных программ и вирусов, которые могут попасть в систему через интернет.\n💻 Совместимость: VPN поддерживает все популярные операционные системы (Windows, MacOS, Linux, Android, iOS). \n\nСТОИМОСТЬ ТАРИФОВ:\n\n• 🗓 Месяц: 79 руб. \n• 🗓 Два месяца: 299 руб.\n• 🗓 Полгода: 459 руб.\n• 🗓 Год: 899 руб.</b>",reply_markup=kb_tarif,parse_mode="html")
    elif call.data == "invite":
        refbal = refbala(call.message.chat.id)
        kolvoref = refuser(call.message.chat.id)
        kb_ref_1 =  types.InlineKeyboardMarkup(row_width=1)
        kr = types.InlineKeyboardButton(text="Вывод",callback_data="refvivod")
        kpod = types.InlineKeyboardButton(text="ПОДЕЛИТЬСЯ",switch_inline_query=f"ПРИЙДИ СЮДА ПАЖ {botname}?start={call.message.chat.id}")
        backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
        kb_ref_1.add(kr,kpod,backbtn)
        
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f'<b>ПАРТНЕРСКАЯ ПРОГРАММА\n\nУСЛОВИЯ:\n\nПри пополнении вашего реферала на любую сумму вы получаете 10% от суммы пополнения на ваш реферальный баланс, что бы вывести денежные средства нажмите ниже кнопку вывод и укажите сумму которую хотите вывести далее ваша заявка будет рассмотрена в течении 48 часов\n\nССЫЛКА </b><code>{botname}?start={call.message.chat.id}</code>\n\n<b>Ваш реферальный баланс {refbal}\n\nПриглашено {kolvoref}</b>',reply_markup=kb_ref_1,parse_mode="html")
    elif call.data == "backststst":
        variable.set_action(call.message.chat.id, 0)
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

    elif call.data =="help":
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption="<b>Выберете пункт меню</b>",reply_markup=kb_help,parse_mode="html")
    elif call.data == "backsts":
        variable.set_action(call.message.chat.id, 0)
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")
    elif call.data == "refvivod":
        await bot.send_message(call.message.chat.id, "Введите сумму для вывода с реферальной программы и через пробел реквизиты\n\nПример (1000 79998783784 Сбербанк)",reply_markup=kb_backstst)
        variable.set_action(call.message.chat.id,1)
    elif call.data == "connect":
        a = checkcfg(call.message.chat.id)
        if a != None:
            
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>Ваша конфигурация\n\n<code>{a}</code></b>",reply_markup=kb_insts,parse_mode="html")
        else:
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"<b>У вас еще нет конфигурации выберете нужный тариф и нажмите кнопку ниже что бы получить конфигурацию</b>",reply_markup=kb_tarif,parse_mode="html")
    
    elif call.data == "Ios":
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>1</b>",reply_markup=kb_back,parse_mode="html")
    elif call.data == "Android":
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>2</b>",reply_markup=kb_back,parse_mode="html")
    elif call.data == "Windows":
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>3</b>",reply_markup=kb_back,parse_mode="html")
    elif call.data == "MacOs":
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>4</b>",reply_markup=kb_back,parse_mode="html")
    
    elif call.data == "Ios_1":
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>1</b>",reply_markup=kb_backststttttt,parse_mode="html")
    elif call.data == "Android_1":
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>2</b>",reply_markup=kb_backststttttt,parse_mode="html")
    elif call.data == "Windows_1":
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>3</b>",reply_markup=kb_backststttttt,parse_mode="html")
    elif call.data == "MacOs_1":
        await bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="<b>4</b>",reply_markup=kb_backststttttt,parse_mode="html")
    
    elif call.data == "tarifs":
        await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption="<b>🗒 ТАРИФНЫЙ ПЛАН 🗒\n\n1 МЕСЯЦ - 79р\n\n3 МЕСЯЦА - 229р\n\nГОД - 899р</b>",reply_markup=kb_back,parse_mode="html")

    elif call.data == "startphoto":
        await bot.send_photo(chat_id=call.message.chat.id, photo=open('start.png','rb'),caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")

        
    elif call.data == "backst":
        variable.set_action(call.message.chat.id, 0)
        await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption="<b>👋 Привет! Рады приветствовать вас в нашей VPN-семье!\n\nТеперь вы можете наслаждаться безопасным и свободным доступом к интернету без ограничений.\n\n🚀 Наши серверы обеспечивают высокую скорость и надежность, а ваша конфиденциальность всегда будет под защитой. </b>",reply_markup=keyboard_start,parse_mode="html")
    else:
        if call.data.startswith("check_"):
            result = await check(call.data.split('_')[1])
            val = call.data.split('_')[2]
            valueRef = int(int(val/100) * 30)
            if result:
                print(1)
                addbal(call.message.chat.id, val)
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=f"Успешно зачислен баланс на сумму {valueRef}",reply_markup=kb_backmain)
                a = getref(call.message.chat.id)
                addrefbal(a,valueRef)
                await bot.send_message(chat_id=a,text=f"Начислен реф баланс на сумму {valueRef}")
            else:
                await bot.send_message(call.message.chat.id, "Ваша оплата еще не прошла\n\nЕсли возникли вопросы обратитесь к администрации",reply_markup=kb_admin)
        
        elif call.data.startswith("prodl_"):
            mail = call.data.split('_')[1]
            a = getbalance(call.message.chat.id)
            kb_prodlenye = types.InlineKeyboardMarkup(row_width=2)
            kp1 = types.InlineKeyboardButton(text="📆 1 МЕСЯЦ - 79",callback_data=f"t1_{mail}")
            kp2 = types.InlineKeyboardButton(text="📆 3 МЕСЯЦА - 229",callback_data=f"t2_{mail}")
            kp3 = types.InlineKeyboardButton(text="📆 ПОЛГОДА - 459",callback_data=f"t3_{mail}")
            kp4 = types.InlineKeyboardButton(text="📆 ГОД - 899",callback_data=f"t4_{mail}")
            backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
            kb_prodlenye.add(kp1,kp2,kp3,kp4,backbtn)
            await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id, caption=f"Выберете срок продления по конфигурации {mail}\n\nВаш баланс {a}",reply_markup=kb_prodlenye)
        elif call.data.startswith("t1_"):
            mail = call.data.split('_')[1]

            a = checkbal(call.message.chat.id, 79)
            if a:
                minbal(call.message.chat.id,79)
                unoxxx = print_and_convert_to_unix(30)
                url = getipbymail(mail)
                print(url)
                session = await sessionid(f"http://{url}:2053/login")
                vless_cfg = getvless(mail)
                ids = call.message.chat.id
                val = 30
                a = construatecfg(mail,session,url,ids,val)
                if a:
                    await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 30 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
                else:
                    print("error updatecfg")
            else:
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
            
        elif call.data.startswith("t2_"):
            mail = call.data.split('_')[1]

            a = checkbal(call.message.chat.id, 229)
            if a:
                minbal(call.message.chat.id,229)
                unoxxx = print_and_convert_to_unix(90)
                url = getipbymail(mail)
                
                session = await sessionid(f"http://{url}:2053/login")
                vless_cfg = getvless(mail)
                ids = call.message.chat.id
                val = 90
                print(123333333333333333333333333333333333333333333333)
                a = construatecfg(mail,session,url,ids,val)
                if a:
                    await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 90 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
                else:
                    print("error updatecfg")
            else:
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        elif call.data.startswith("t3_"):
            mail = call.data.split('_')[1]

            a = checkbal(call.message.chat.id, 459)
            if a:
                minbal(call.message.chat.id,459)
                unoxxx = print_and_convert_to_unix(180)
                url = getipbymail(mail)
                print(url)
                session = await sessionid(f"http://{url}:2053/login")
                vless_cfg = getvless(mail)
                ids = call.message.chat.id
                val = 180
                a = construatecfg(mail,session,url,ids,val)
                if a:
                    await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 180 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
                else:
                    print("error updatecfg")
            else:
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        elif call.data.startswith("t4_"):
            mail = call.data.split('_')[1]

            a = checkbal(call.message.chat.id, 899)
            if a:
                minbal(call.message.chat.id,899)
                unoxxx = print_and_convert_to_unix(365)
                url = getipbymail(mail)
                print(url)
                session = await sessionid(f"http://{url}:2053/login")
                vless_cfg = getvless(mail)
                ids = call.message.chat.id
                val = 365
                a = construatecfg(mail,session,url,ids,val)
                if a:
                    await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id, caption = f"Успешно продлен на 365 дней\n\nВаш конфиг<code>\n\n{vless_cfg}</code>\n\nчто бы подключить нажмите ниже для перехода в нужную инструкцию",reply_markup=kb_insts,parse_mode="html")
                else:
                    print("error updatecfg")
            else:
                await bot.edit_message_caption(chat_id=call.message.chat.id, message_id=call.message.message_id,caption =  f"Не хватает средств пополните баланс по кнопке ниже",reply_markup=kb_popln)
        

        elif call.data.startswith("amount_"):
            if call.data == "amount_manual":
                await bot.send_message(
                    call.message.chat.id, 
                    "Введите сумму пополнения вручную:",
                    reply_markup=kb_back
                )
                variable.set_action(call.message.chat.id, 2)  # Устанавливаем состояние для ручного ввода
            else:
                # Получаем сумму из callback_data
                amount = int(call.data.split("_")[1])
                email = "example@mail.com"  # Здесь нужно получить email пользователя
                items = [
                    {
                        "description": "Пополнение баланса",
                        "quantity": 1,
                        "amount": {
                            "value": f"{amount:.2f}",
                            "currency": "RUB"
                        },
                        "vat_code": 1
                    }
                ]

                # Создаем платеж
                payment_url, payment_id = await create(amount, call.message.chat.id, email, items)
                kb_oplata = InlineKeyboardMarkup(row_width=1)
                kb_oplata.add(
                    InlineKeyboardButton(text="ОПЛАТИТЬ", url=payment_url),
                    InlineKeyboardButton(text="ПРОВЕРИТЬ ОПЛАТУ", callback_data=f"check_{payment_id}_{amount}"),
                    InlineKeyboardButton(text="НАЗАД ◀️", callback_data="startphoto")
                )

                await bot.send_message(
                    chat_id=call.message.chat.id,
                    text="Оплатите по кнопке ниже, после этого проверьте оплату",
                    reply_markup=kb_oplata
                )
        else:
            try:
                a = getvless(call.data)
                mail = a.split("#")[1]
                kb_connect = types.InlineKeyboardMarkup(row_width=1)
                kcc1 = types.InlineKeyboardButton(text="Инструкция",callback_data="ins")
                kcc2 = types.InlineKeyboardButton(text="ПОДКЛЮЧИТЬСЯ",url=f"https://vpn-connector.netlify.app/?url={a}")
                kcc3 = types.InlineKeyboardButton(text="Продлить",callback_data=f"prodl_{mail}")
                backbtn = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="backst")
                kb_connect.add(kcc1,kcc2,kcc3,backbtn)
                await bot.edit_message_caption(chat_id=call.message.chat.id,message_id=call.message.message_id,caption= f"Ваша конфигурация \n\n<code>{a}</code>",reply_markup=kb_connect,parse_mode="html")
            except:
                pass
async def is_user_subscribed(user_id: int) -> bool:
    result = await bot.get_chat_member(CHANNEL_ID, user_id)  # Замените на реальный ID пользователя
    print(f"Подписан ли пользователь: {result}")
    try:
        chat_member = await bot.get_chat_member(CHANNEL_ID, user_id)
        print(chat_member)
        print(chat_member.status)
        return chat_member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(f"Ошибка: {e}")
        return False





@dp.message_handler(lambda message: True, content_types=['text', 'photo'])
async def handle_text(message: types.Message):
    text = message.text
    action = int(variable.get_action(message.chat.id))

    if action == 1:
        try:
            a = int(text.split(" ")[0])
            print(212412412412214124412412,message.chat.id,refbala(str(message.chat.id)))
            b = int(refbala(message.chat.id))
            if a <= b:
                minref(message.chat.id,a)
                print("allokey")
                await bot.send_message(chat_id=partner_chat,text=f"Вывод Реферала {message.chat.id}\n\nНа сумму {a}\n\nПользователь @{message.from_user.username}")
                await bot.send_message(message.chat.id, f"Успешно создана заявка\nОжидайте ответа от администратора\nВаш реферальный баланс списан на сумму {a}",reply_markup=kb_backmain)
            else:
                await bot.send_message(message.chat.id, "Не достаточно реф баланса",reply_markup=kb_backststttttt)
                variable.set_action(message.chat.id, 0)
        except:
            await bot.send_message(message.chat.id, "Не верно составлена заявка",reply_markup=kb_backststttttt)
            variable.set_action(message.chat.id, 0)
    elif action == 2:
        try:
            amount = int(text)
            email = "963-52@mail.ru"  # Здесь нужно получить email пользователя
            items = [
            {
                "description": "Пополнение баланса",
                "quantity": 1,
                "amount": {
                    "value": f"{amount:.2f}",
                    "currency": "RUB"
                },
                "vat_code": 1
            }
        ]
        
        # Создаем платеж с данными чека
            payment_url, payment_id = await create(amount, message.chat.id, email, items)
            # payment_url, payment_id = await create(amount, message.chat.id, email)
            

            print(payment_url,payment_id)
            
            kb_oplata = types.InlineKeyboardMarkup(row_width=1)
            o1 = types.InlineKeyboardButton(text="ОПЛАТИТЬ",url=payment_url)
            o2 = types.InlineKeyboardButton(text="ПРОВЕРИТЬ ОПЛАТУ",callback_data=f"check_{payment_id}_{message.text}")
            o3 = types.InlineKeyboardButton(text="НАЗАД ◀️",callback_data="startphoto")
            kb_oplata.add(o1,o2,o3)
            await bot.send_message(chat_id=message.chat.id,text="Оплатите по кнопке ниже, после этого проверьте оплату",reply_markup=kb_oplata)
        except:
            await bot.send_message(chat_id=message.chat.id,text="Не верно указана сумма пополнения",reply_markup=kb_backststttttt)

    elif action == 10:
        print(str(message.text))
        addserverinlist(str(message.text))


async def check_server():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(SERVER_URL, ssl=False) as response:
                if response.status == 200:
                    return "🟢 Сервер доступен"
                else:
                    return "🔴 Сервер недоступен"
    except aiohttp.ClientError:
        return "🔴 Сервер в данный момент недоступен"



#all func 
async def login():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(LOGIN_URL, data=LOGIN_DATA) as response:
                if response.status == 200:
                    cookies = response.cookies
                    session_id = cookies.get("3x-ui").value if "3x-ui" in cookies else None
                    if session_id:
                        bot_logger.info(f"Session ID: {session_id}")
                        return session_id
                    else:
                        bot_logger.error("Session ID not found in cookies")
                        return None
                else:
                    bot_logger.error(f"Failed to log in, status code: {response.status}")
                    return None
    except:
        print("HUETA")            




    


if __name__ == '__main__':
  # Запуск вашего цикла как асинхронной задачи
    executor.start_polling(dp, skip_updates=True)

