from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime
import json
import math

attendence = on_command('签到')

@attendence.handle()
async def sigh(bot:Bot, event:GroupMessageEvent, state:T_State):
    id = int(event.get_user_id())
    sigh = [0,1,2,3,4]
    # 0:id
    # 1:money
    # 2:sigh_days
    with open("C:\PyProject\lucky\src\plugins\\group_data.json", "r",encoding = 'utf-8') as f:
        data = list(json.load(f))
    for i in range(0,len(data)):
        if data[i[0]] == id:
            data[i[2]] = data[i[2]] + 1
            data[i[1]] = data[i[1]] + money_cul(data[i[2]])
            msg = f'亲爱的群成员({id}),签到成功(*^▽^*)~\n你已经连续签到{data[i[2]]}天\n今天签到获得硬币{money_cul(data[i[2]])}\n账户内硬币数：{data[i[1]]}'
            await attendence.finish(msg)
    
    sigh[0] = id
    sigh[1] = 0
    sigh[2] = 1
    data.append(sigh)
    msg = f'亲爱的群成员({id}),签到成功(*^▽^*)~\n你已经连续签到{sigh[2]}天\n今天签到获得硬币{money_cul(sigh[2])}\n账户内硬币数：{sigh[1]}'
    await attendence.finish(msg)

    with open("C:\PyProject\lucky\src\plugins\\group_data.json", "w",encoding = 'utf-8') as f:
        f.write(json.dumps(data))




def money_cul(days):
    if days == 1:
        return 1;
    days = float(days)
    money = 10 * log(days * 0.06 + 1)
    return int(money)