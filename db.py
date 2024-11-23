import sqlite3
import json
import random
import requests
import aiohttp
import asyncio, json, logging, qrcode, random, re, sqlite3, string, datetime
from datetime import datetime as dt
from io import BytesIO
import string
from config import *
import time
con = sqlite3.connect("db.db")
cur = con.cursor()
import yookassa
from yookassa import Payment
import uuid

LOGIN_DATA = {"username": "admin", "password": "npGrnheQ9X#Ubr26"}

yookassa.Configuration.account_id = 491169
yookassa.Configuration.secret_key = "live_zWItd6thDccyUAHYaUlul6dr1T_EHQ8H1uVMjwEjUq8"
async def check(payment_id):
    print(payment_id)
    payment = await yookassa.Payment.find_one(payment_id)
    if payment.status == 'succeeded':
        return payment.metadata
    else:
        return False

cur.execute("""CREATE TABLE IF NOT EXISTS list (
        id TEXT,
        balance TEXT,
        ref TEXT,
        refbal TEXT,
        config TEXT
    )""")


cur.execute("""CREATE TABLE IF NOT EXISTS servers (
        ip TEXT   
    )""")


cur.execute("""CREATE TABLE IF NOT EXISTS cfg (
        id TEXT,
        vless TEXT,
        email TEXT
        
    )""")
con.commit()
con.close()
class Database:
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()

    def get_stream_settings(self, email):
        query = """
            SELECT
                i.protocol AS prt,
                i.port AS pot,
                json_extract(i.stream_settings, '$.network') AS net,
                json_extract(i.stream_settings, '$.security') AS secur,
                json_extract(i.stream_settings, '$.realitySettings.settings.publicKey') AS pbk,
                json_extract(i.stream_settings, '$.realitySettings.settings.fingerprint') AS fp,
                json_extract(i.stream_settings, '$.realitySettings.serverNames[0]') AS sni,
                json_extract(i.stream_settings, '$.realitySettings.shortIds[0]') AS sid
            FROM
                inbounds i
            JOIN
                client_traffics ct ON i.id = ct.inbound_id
            WHERE
                ct.email = ?;
        """
        self.cursor.execute(query, (email,))
        return self.cursor.fetchall()

    def get_ids_by_email(self, email):
        query = """
            SELECT settings
            FROM inbounds
            WHERE settings LIKE '%\"email\": "{}\"%'""".format(email)
        self.cursor.execute(query)
        settings = [row[0] for row in self.cursor.fetchall()]
        client_ids = []
        for setting in settings:
            setting_data = json.loads(setting)
            for client in setting_data['clients']:
                if client['email'] == email:
                    client_ids.append(client['id'])
        return client_ids

    def get_client_traffics_by_email(self, email):
        query = """
            SELECT email, up, down, expiry_time, total
            FROM client_traffics
            WHERE email = ?"""
        self.cursor.execute(query, (email,))
        results = self.cursor.fetchall()
        return results
    

def print_and_convert_to_unix(days_offset):
    current_unix_time_in_seconds = int(time.time())
    
    # Прибавляем дни (в секундах)
    seconds_in_offset = days_offset * 24 * 60 * 60
    future_unix_time_in_seconds = current_unix_time_in_seconds + seconds_in_offset
    
    # Преобразуем будущее Unix время в миллисекунды
    future_unix_time_in_milliseconds = future_unix_time_in_seconds * 1000
    
    return future_unix_time_in_milliseconds
def getref(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = cur.execute(f"SELECT ref FROM list WHERE id = ?",(id,)).fetchone()[0]
    con.commit()
    con.close()
    return(a)
def test(valeur):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM answers WHERE id = {valeur}")
    con.commit()
    con.close()
    
def checkcfg(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    try:
        a = cur.execute(f"SELECT vless FROM cfg WHERE id  = {id}").fetchone()[0]
    except:
        a = None
    con.commit()
    con.close()
    print(a)
    
    return(a)
    
def getactualdata(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = cur.execute(f"SELECT email FROM cfg WHERE id  = {id}").fetchone()[0]
    con.commit()
    con.close()
    return(a)
def getipfromemail(mail):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    print(mail)
    a = cur.execute(f"SELECT vless FROM cfg WHERE email  = (?)",(mail,)).fetchone()[0]
    con.commit()
    con.close()
    return(a.split("@")[1].split(":")[0])
def getbalance(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = cur.execute(f"SELECT balance FROM list WHERE id  = {id}").fetchone()[0]
    con.commit()
    con.close()
    return(a)
def addbal(id,val):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = int(getbalance(id))
    print(a)
    cur.execute("UPDATE list SET balance = ? WHERE id = ? ",(a+int(val),id))
    con.commit()
    con.close()
def addrefbal(id,val):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = int(refbala(id))
    cur.execute("UPDATE list SET refbal = ? WHERE id = ? ",(val+a,id))
    con.commit()
    con.close()
def refbala(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    list = cur.execute(f"SELECT refbal FROM list WHERE id = {id}").fetchone()[0]
    con.commit()
    con.close()
    return(list)


def minref(id,val):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = refbala(id)
    cur.execute(f"UPDATE list SET refbal = (?) WHERE id = (?)",(int(a)-int(val), id))
    con.commit()
    con.close()


def test1(id,value,mtext):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO answers VALUES(?,?,?)",(id,value,mtext))
    con.commit()
    con.close()

def test2(id):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    list = cur.execute(f"SELECT answer FROM answers WHERE id = '{id}'").fetchall()
    con.commit()
    con.close()
    return list


def trialcheck(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (id,))
    user = cursor.fetchone()
    return(user)

def addclient(id,mail):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (telegram_id, email) VALUES (?, ?)", (id, mail))
    con.commit()
    con.close()


def addserverinlist(ip):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO servers VALUES(?)", (ip,))
    con.commit()
    con.close()
    


def serverslist():
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    a = cursor.execute("SELECT ip FROM servers").fetchall()
    con.commit()
    con.close()
    return(a)

    
async def create(amount, chat_id, email, items):
    """
    Создание платежа с учетом данных для формирования чека.
    
    :param amount: Сумма платежа
    :param chat_id: ID пользователя Telegram
    :param email: Email пользователя для отправки чека
    :param items: Список товаров (массив словарей с данными о товарах)
    """
    id_key = str(uuid.uuid4())  # Идемпотентный ключ для уникальности запроса
    
    # Формирование тела запроса с данными чека
    payment_data = {
        "amount": {
            "value": f"{amount:.2f}",  # Сумма платежа
            "currency": "RUB"
        },
        "capture": True,
        "confirmation": {
            "type": "redirect",  # Пользователь будет перенаправлен на страницу оплаты
            "return_url": "https://t.me/DikaVPN_bot"
        },
        "description": f"Пополнение баланса для {chat_id}",
        "metadata": {
            "chat_id": chat_id
        },
        "receipt": {
            "customer": {
                "email": email  # Email пользователя
            },
            "items": items  # Товары, передаваемые в чеке
        }
    }

    # Создание платежа через YooKassa
    payment = await Payment.create(payment_data, id_key)

    return payment.confirmation.confirmation_url, payment.id




def generate_key():
    
    part1 = ''.join(random.choices(string.digits, k=5))
    part2 = ''.join(random.choices(string.ascii_lowercase, k=5))
    key = f"{part1}{part2}"
    print(key)
    return(key)


def dbcfg(vless,mail):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO cfg (vless, email) VALUES (?, ?)", (id, vless,mail))
    con.commit()
    con.close()

def checkuser(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    user = cursor.execute("SELECT balance FROM list WHERE id=?", (id,))
    a  = (user.fetchone())
    print(a)
    if a != None:
        con.close()
        return(True)
        
    else: 
        con.close()       
        return(False)
    


def addfreecfg(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute(f"UPDATE list SET config = 1 WHERE id = '{id}'")
    con.commit()
    con.close()
def adduserref(id,ref):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO list  VALUES (?, ?, ?, ?, ?)", (id, "0",ref,"0",""))
    con.commit()
    con.close()
def adduser(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO list  VALUES (?, ?, ?, ?, ?)", (id, "0","","0","0"))
    con.commit()
    con.close()

def getvless(id):
    print(id)
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    a = cursor.execute(f"SELECT vless FROM cfg WHERE email = '{id}'").fetchone()[0]
    con.close()
    return(a)


def selectcfg(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    a = cursor.execute(f"SELECT email FROM cfg WHERE id = '{id}'").fetchall()
    con.close()
    return(a)


def refuser(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    a = cursor.execute(f"SELECT COUNT(id) FROM list WHERE ref = {id}").fetchone()[0]
    con.close()
    return(a)

def checkfree(id):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    a = cursor.execute(f"SELECT config FROM list WHERE id = {id}").fetchone()
    con.close()
    return(a)

def savecfg(id,vless,mail):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO cfg VALUES(?,?,?)",(id,vless,mail))
    con.commit()
    con.close()


def checkbal(id,val):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    bal = getbalance(id)
    con.commit()
    con.close()
    if int(bal) >= val:
        return(True)
    else:
        return(False)
    
def minbal(id,val):
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    bal = getbalance(id)
    newbalance = int(int(bal)-int(val))
    cursor.execute("UPDATE list SET balance = (?) WHERE id  = ?",(newbalance,id))
    con.commit()
    con.close()

def getkeys():
    con = sqlite3.connect("db.db")
    cursor = con.cursor()
    keys = cursor.execute("SELECT email FROM cfg").fetchall()
    return(keys)






def addcfg(id, tarif):
    
    key = generate_key()
    
def get_ids_by_email(self, email):
        query = """
            SELECT settings
            FROM inbounds
            WHERE settings LIKE '%\"email\": "{}\"%'""".format(email)
        self.cursor.execute(query)
        settings = [row[0] for row in self.cursor.fetchall()]
        client_ids = []
        for setting in settings:
            setting_data = json.loads(setting)
            for client in setting_data['clients']:
                if client['email'] == email:
                    client_ids.append(client['id'])
        return client_ids


def generate_config(client_id, email, prt=None, pot=None, pbk=None, fp=None, sni=None, sid=None, net=None, secur=None):
    if prt is None or pot is None or pbk is None or fp is None or sni is None or sid is None:
        db = Database(DATABASE)
        stream_settings = db.get_stream_settings(email)
        if stream_settings:
            prt, pot, net, secur, pbk, fp, sni, sid = stream_settings[0]
        else:
            return ""
    config = f"{prt}://{client_id}@{SERVER_IP}:{pot}?type={net}&security={secur}&pbk={pbk}&fp={fp}&sni={sni}&sid={sid}&spx=%2F#{email}"
    return config


async def add_client_request(client_id,mail,time):
    url,session = await takeip()
    print("ADD CLIENT",url,session,client_id,mail)
    # Формирование данных для запроса
    payload = {
        "id": 2,
        "settings": json.dumps({
            "clients": [{
                "id": f"{client_id}_{mail}",
                "flow": "xtls-rprx-vision",
                "email": str(mail),
                "limitIp": 0,
                "totalGB": 0,
                "expiryTime": time,
                "enable": True,
                "tgId": "",
                "subId": "",
                "reset": 0
            }]
        })
    }

    # Заголовки запроса, включая куки
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': f'{session}'
        
    }
    print(url)
    finurl = f"http://{url}:22054/panel/inbound/addClient"
    # Отправка POST-запроса
    response = requests.post(finurl, headers=headers, json=payload)
    print(response.text)
    #cfgsvae(client_id,mail)
    return(url,session)




async def testcfgonweek(client_id,mail):
    url,session = await takeip()
    print("ADD CLIENT",url,session,client_id,mail)
    # Формирование данных для запроса
    payload = {
        "id": 1,
        "settings": json.dumps({
            "clients": [{
                "id": f"{client_id}_{mail}",
                "flow": "xtls-rprx-vision",
                "email": str(mail),
                "limitIp": 0,
                "totalGB": 0,
                "expiryTime": 604800000,
                "enable": True,
                "tgId": "",
                "subId": "",
                "reset": 0
            }]
        })
    }

    # Заголовки запроса, включая куки
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Cookie': f'{session}'
        
    }
    print(url)
    finurl = f"http://{url}:22054/panel/inbound/addClient"
    # Отправка POST-запроса
    response = requests.post(finurl, headers=headers, json=payload)
    print(response.text)
    print(url, session)
    #cfgsvae(client_id,mail)
    return(url, session)




def cfgsvae(id,cfg):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    cur.execute("INSERT INTO cfg (vless, email) VALUES (?,?)",(cfg,id))
    con.commit()
    con.close()
    

def send_cfg(idcfg,idclient):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    stream_settings = get_stream_settings(idcfg)
    if stream_settings:
        prt, pot, net, secur, pbk, fp, sni, sid = stream_settings[0]
    else:
        return ""
    config = f"{prt}://{idclient}@{SERVER_IP}:{pot}?type={net}&security={secur}&pbk={pbk}&fp={fp}&sni={sni}&sid={sid}&spx=%2F#fsdfsdfsdf"
    con.commit()
    con.close()
    return (config)
        
   

def get_stream_settings(email):
        con = sqlite3.connect("db.db")
        cur = con.cursor()
        query = """
            SELECT
                i.protocol AS prt,
                i.port AS pot,
                json_extract(i.stream_settings, '$.network') AS net,
                json_extract(i.stream_settings, '$.security') AS secur,
                json_extract(i.stream_settings, '$.realitySettings.settings.publicKey') AS pbk,
                json_extract(i.stream_settings, '$.realitySettings.settings.fingerprint') AS fp,
                json_extract(i.stream_settings, '$.realitySettings.serverNames[0]') AS sni,
                json_extract(i.stream_settings, '$.realitySettings.shortIds[0]') AS sid
            FROM
                inbounds i
            JOIN
                client_traffics ct ON i.id = ct.inbound_id
            WHERE
                ct.email = ?;
        """
        cur.execute(query, (email,))
        return cur.fetchall()
def getipbymail(mail):
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    try:
        a = cur.execute("SELECT vless FROM cfg WHERE email = (?)",(mail,)).fetchone()[0]
        ip = a.split("@")[1].split(":")[0]
        con.commit()
        con.close()
        return(ip)
    except:
        pass


async def listall(ip, session, email):
    # Формируем URL для получения данных
    url = f"http://{ip}:22054/panel/api/inbounds/list"

    # Заголовки для запроса
    headers = {
        "Accept": "application/json",
        "Cookie": f"lang=ru-RU; 3x-ui={session}"
    }

    # Выполнение GET-запроса
    response = requests.get(url, headers=headers)
    
    # Получаем данные в формате JSON
    data = response.json()
    print(data)
    # Ищем клиента с указанным email
    for obj in data.get('obj', []):
        for client in obj.get('clientStats', []):
            if client.get('email') == email:
                expiry_time_ms = client.get('expiryTime')

                # Если есть поле expiryTime
                if expiry_time_ms:
                    # Преобразуем время в миллисекундах в дату
                    seconds = expiry_time_ms / 1000
                    date = datetime.datetime.fromtimestamp(seconds)
                    
                    day_month = date.strftime('%d.%m')

                    print(f"Email: {email}, Expiry Date: {day_month}")
                    return day_month
                else:
                    print(f"Email: {email} найден, но дата окончания не указана.")
                    return None
    print(f"Email: {email} не найден.")
    return None





async def sessionid(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=LOGIN_DATA) as response:
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
                

    except Exception as e:
        bot_logger.error(f"Exception during login: {e}")
        return None

async def takeip():
    a = serverslist()
    print(a)
    for i in a:
        
        url1 = f"http://{i[0]}:22054/login"

        session =f"3x-ui={await sessionid(url1)}" 
   
        url = f"http://{i[0]}:22054/panel/api/inbounds/list"
        # Заголовки для запроса
        headers = {
            "Accept": "application/json",
            "Cookie": f"lang=ru-RU; {session}"
        }

        # Выполнение GET-запроса
        response = requests.get(url, headers=headers)

        # Выводим статус и текст ответа для диагностики
        #print(f"Статус ответа: {response.status_code}")
        #print(response.json())
        data = response.json()
        k = 0
        # Проверяем, успешен ли запрос
        if data.get("success"):
                # Флаг для отслеживания, найден ли email

            for inbound in data.get("obj", []):
                # Преобразуем строки "settings" и "streamSettings" обратно в JSON
                try:
                    settings_json = json.loads(inbound.get("settings", "{}"))
                    print(settings_json['clients'])
                    #for i in settings_json['clients']['email']:
                        
                        #print(i)
                    
                    for client in settings_json['clients']:
                        if 'email' in client:
                            print(client['email'])
                            k+=1
                    
                except:
                    print('error')
            print("k = ", k)
            if k < maxusers:
                return(i[0],session)
            else:
                print('error server')


def allusers():
    con = sqlite3.connect("db.db")
    cur = con.cursor()
    a = cur.execute("SELECT COUNT(id) FROM cfg").fetchone()[0]
    con.commit()
    con.close()
    return(a)

def createcfgbymail(url,session_id,mail):
    
    
    # Заголовки для запроса
    headers = {
        "Accept": "application/json",
        "Cookie": f"lang=ru-RU; {session_id}"
    }
    finurl = f"http://{url}:22054/panel/inbound/list"
    # Отправка POST-запроса
    response = requests.post(finurl, headers=headers)
    # Проверяем, что ответ возвращается в формате JSON
    if response.headers.get("Content-Type") == "application/json; charset=utf-8":
        try:
            # Попытка декодировать JSON
            data = response.json()
            
            # Проверяем, успешен ли запрос
            if data.get("success"):
                target_email = mail  # Используем переданный email
                found = False  # Флаг для отслеживания, найден ли email

                for inbound in data.get("obj", []):
                    # Преобразуем строки "settings" и "streamSettings" обратно в JSON
                    try:
                        settings_json = json.loads(inbound.get("settings", "{}"))
                        stream_settings_json = json.loads(inbound.get("streamSettings", "{}"))
                    except json.JSONDecodeError as e:
                        
                        continue

                    # Выводим полученные настройки для диагностики
                    
                    # Извлечение параметров
                    clients = settings_json.get("clients", [])
                    for client in clients:
                        email_client = client.get("email")  # email клиента
                        client_flow = client.get("flow")
                        if email_client == target_email:
                            found = True
                            client_id = client.get("id")  # id клиента
                            port = inbound.get("port")  # port
                            network = stream_settings_json.get("network")  # network
                            security = stream_settings_json.get("security")  # security

                            # Извлечение publicKey из settings внутри realitySettings
                            public_key = stream_settings_json.get("realitySettings", {}).get("settings", {}).get("publicKey")  # publicKey
                            server_name = stream_settings_json.get("realitySettings", {}).get("serverNames", [])[0] if stream_settings_json.get("realitySettings", {}).get("serverNames") else None  # первый элемент из serverNames
                            short_id = stream_settings_json.get("realitySettings", {}).get("shortIds", [])[0] if stream_settings_json.get("realitySettings", {}).get("shortIds") else None  # первый элемент из shortIds
                            fingerprint = stream_settings_json.get("realitySettings", {}).get("fingerprint", "random")  # fingerprint

                            # Вывод значений
                            
                            vless_url = f"vless://{client_id}@{url}:{port}?type={network}&security={security}&pbk={public_key}&fp={fingerprint}&sni={server_name}&sid={short_id}&spx=%2F&flow={client_flow}#{email_client}"
                            print(vless_url)
                            return(vless_url)  # Выход из внутреннего цикла после нахождения email
                            
                if not found:
                    print(f"Email '{target_email}' не найден.")
            else:
                print("Запрос не удался.")
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON.")
    else:
        print("Ответ не в формате JSON.")

def construatecfg(mail_sender,session,ip,id,val):
    # Заголовки для запроса
    headers = {
        "Accept": "application/json",
        "Cookie": f"lang=ru-RU; 3x-ui={session}"
    }
    finurl = f"http://{ip}:22054/panel/inbound/list"
    # Отправка POST-запроса
    response = requests.post(finurl, headers=headers)
    # Выполнение GET-запроса
    
    print(f"Статус ответа: {response.status_code}")

    # Проверяем, что ответ возвращается в формате JSON
    if response.headers.get("Content-Type") == "application/json; charset=utf-8":
        try:
            # Попытка декодировать JSON
            data = response.json()
            with open('response_data.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
           
            
            
            # Перебираем каждый объект внутри "obj"
            
                # Перебираем всех клиентов внутри "clientStats"
                
            # Пример получения нужных переменных
            for inbound in data.get("obj", []):
                for client in inbound.get("clientStats", []):
                    if client.get("email") == mail_sender:
                    # Извлекаем строку settings и streamSettings
                        settings_json = json.loads(inbound.get("settings", "{}"))
                        a = settings_json.get("clients")[0].get("id")
                        print(a)
                        b= settings_json.get("clients")[0].get("flow")
                        c= settings_json.get("clients")[0].get("email")
                        d=settings_json.get("clients")[0].get("limitIp")
                        e=settings_json.get("clients")[0].get("totalGB")
                        f=client.get("expiryTime")
                       
                        g=settings_json.get("clients")[0].get("enable")
                        h=settings_json.get("clients")[0].get("tgId")
                        i=settings_json.get("clients")[0].get("subId")
                        j=settings_json.get("clients")[0].get("reset")

                        ext = client.get("expiryTime")
                        # Выводим переменные для проверки
                        url = f"http://{ip}:22054/panel/inbound/updateClient/{id}_{mail_sender}"
                        print(url,session)
                        # Сессионные куки
                        cookies = {
                            "3x-ui": f"{session}",
                            "lang": "ru-RU"
                        }

                        # Заголовки запроса
                        headers = {
                            "Accept": "application/json",
                            "Content-Type": "application/json"
                        }
                        
                        newext = ext + (val * 86400000)
                        print(ext,newext)
                        data = {
                            "id": 2,
                            "settings": json.dumps({
                                "clients": [{
                                    "id": f"{id}_{mail_sender}",
                                    "flow": b,
                                    "email": f"{mail_sender}",
                                    "limitIp": d,
                                    "totalGB": e,
                                    "expiryTime": newext,
                                    "enable": g,
                                    "tgId": "",
                                    "subId": f"{i}",
                                    "reset": j
                                }]
                            }, indent=4)}
                        print(data)
                        response = requests.post(url, headers=headers, cookies=cookies, json=data)

                        # Выводим статус и ответ сервера для диагностики
                        print(f"Статус ответа: {response.status_code}")
                        print(f"Ответ сервера: {response.text}")
                        return(True)

        except json.JSONDecodeError:
            print("Ответ не содержит корректный JSON.")
            return(False)
    else:   
        print("Ответ не в формате JSON. Получен заголовок Content-Type:", response.headers.get("Content-Type"))
        print("Текст ответа:", response.text)
        return(False)  # Печатаем текст ответа для диагностики
    
