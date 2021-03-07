from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime

morning = on_command('早上好')

@morning.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    hour_num=datetime.now().hour
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    if hour_num >=7 and hour_num <=10:
        msg = at_+'早上好！'
    elif hour_num >=10:
        msg = at_+'现在已经不是早上了吧小猪崽！！！'
    else:
        msg = at_+'啊呜,你起的好早欸！'
    msg = Message(msg)
    await morning.finish(msg)

noon = on_command('中午好')

@noon.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    hour_num=datetime.now().hour
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    if hour_num >=7 and hour_num <=10:
        msg = at_+'宝贝，是不是睡眠不够脑袋不清楚了...现在是早晨！'
    elif hour_num >=10 and hour_num <= 14:
        msg = at_+'中午好！'
    elif hour_num <=7:
        msg = at_+'你是猫头鹰嘛！！我超喜欢猫头鹰！！主人也是...'
    elif hour_num >= 19:
        msg = at_+'睡午觉睡昏了吧小猪崽！！！现在是晚上！'
    else:
        msg = at_+'现在是下午茶时间，要来喝杯茶么?'
    msg = Message(msg)
    await noon.finish(msg)
