# -*- coding: utf-8 -*-
import telegram
import time
import json
import parse
import alarm

# https://api.telegram.org/bot5305251039:AAFefdvfz6AdklBt1-chInbBujW4MGSA5vo/sendMessage?chat_id=396797691&text=안녕하세요.
api_token = "5395071684:AAHlZb7dJTrOWq4ENVYAyn4pl0pDriIR8fQ"
api_id = "-1001622234032"
# "396797691" # 개인

bot = telegram.Bot(token=api_token)
msg_list = []


def reply(string):
    bot.sendMessage(api_id, string)


def read_json(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as err:
        print("위치에 없음")


def ignore_pre_msg():
    for u in bot.getUpdates():
        msg = u.message
        if msg is not None and msg['text'] is not None and len(msg['text']) > 0:
            msg_list.append(msg['message_id'])


def main():
    alarm.main(bot, api_id)
    ignore_pre_msg()

    title = bot.get_chat(api_id)['title']
    print(f"Listening {title}[{api_id}]...")

    while True:
        for u in bot.getUpdates():
            if u.message is None:
                continue
            msg = u.message.to_dict()
            # print(msg)
            if not 'text' in msg:
                continue
            if not msg['message_id'] in msg_list and str(msg['chat']['id']) == api_id:
                msg_list.append(msg['message_id'])
                print(msg['text'])
                parse.main(msg['text'], api_id, bot)
        time.sleep(1)
