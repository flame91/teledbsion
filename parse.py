# -*- coding: utf-8 -*-
import execute as db


def main(cmd, api_id, bot):
    cmd = str(cmd)
    if cmd[:3].upper() == 'ADD':
        start_sign = cmd.split(" ")[1][0]
        if not(start_sign == '"' or start_sign == "'"):
            print("쿼리절이 포함되어 있지 않거나 따옴표로 묶여있지 않습니다.")
        elif cmd.count(start_sign) <= 1:
            print("쿼리절의 따옴표가 너무 적습니다.")
        elif cmd.count(start_sign) >= 3:
            print("쿼리절의 따옴표가 너무 많습니다.")
        else:
            # if qry[-1] != ';':
            #     qry += ';'
            result = db.select(cmd.split(start_sign)[1])
            print(result)
            bot.sendMessage(api_id, str(result))

    elif cmd[:4].upper() == 'LIST':
        print("LIST 실행됨")
    elif cmd[:6].upper() == 'MODIFY':
        print("MODIFY 실행됨")
    elif cmd[:3].upper() == 'DEL':
        print("DEL 실행됨")
    elif cmd[:6].upper() == 'SELECT':
        result = db.select(cmd)
        print(result)
        bot.sendMessage(api_id, str(result))
    else:
        print("Invalid command")
