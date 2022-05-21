# -*- coding: utf-8 -*-
import rw_json

alarm_list = []


def load_list(bot, api_id):
    result = rw_json.r_json()
    if result != "list.json NOT FOUND":
        for r in result:
            alarm_list.append(r)
    else:
        bot.sendMessage(api_id, result)

def main(bot, api_id):
    result = load_list(bot, api_id)
    