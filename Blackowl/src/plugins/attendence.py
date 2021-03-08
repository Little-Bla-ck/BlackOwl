from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime
import json
import math

attendence = on_command('签到')
sighed = [0,0,0,0,0]
# 0:id
# 1:money
# 2:sigh_days

@attendence.handle()
async def sigh(bot:Bot, event:GroupMessageEvent, state:T_State):
    id = str(event.get_user_id())
    with open("C:\Coding\Python\kqhttp\\group_data.json", "r",encoding = 'utf-8') as f:
        data = list(json.load(f))
    for i in range(0, len(data)):
        lipu = data[i]
        if str(lipu[0]) == id:
            lipu[2] = lipu[2] + 1
            lipu[1] = lipu[1] + int(money_cul(lipu[2]))
            msg = f'亲爱的群成员({id}),签到成功(*^▽^*)~\n你已经连续签到{lipu[2]}天\n今天签到获得硬币{int(money_cul(lipu[2]))}\n账户内硬币数：{lipu[1]}'
            await attendence.finish(msg)
    
    sighed[0] = id
    sighed[2] = 1
    sighed[1] = int(money_cul(sighed[2]))
    
    data.append(sighed)
    msg = f'亲爱的群成员({id}),签到成功(*^▽^*)~\n你已经连续签到{sighed[2]}天\n今天签到获得硬币{int(money_cul(sighed[2]))}\n账户内硬币数：{sighed[1]}'
    with open("C:\Coding\Python\kqhttp\\group_data.json", "w",encoding = 'utf-8') as f:
        f.write(json.dumps(data))
    await attendence.finish(msg)

    




def money_cul(days):
    if days == 1:
        return 1;
    days = float(days)
    money = 10 * math.log(days * 0.06 + 1)
    return int(money)