from nonebot import on_command,on_keyword
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent,PrivateMessageEvent
from datetime import datetime

'''
本插件通过 关键字 来 识别用户语句中的关键字命令 以 触发机器人打招呼的对话
————更新 不同时间触发不同对话内容！
————更新 可以识别语句中的关键词来触发对话!
'''

morning = on_keyword('早上好')

@morning.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    if '早上好' in str(event.get_message()):
        hour_num=datetime.now().hour
        id = str(event.get_user_id())
        at_ = "[CQ:at,qq={}]".format(id)
        if hour_num >=7 and hour_num <=10:
            msg = at_+'早上好！！今天也是元气满满的一天呢！！'
        elif hour_num >=10:
            msg = at_+'现在已经不是早上了吧小猪崽！！！'
        else:
            msg = at_+'啊呜,你起的好早欸！'
        msg = Message(msg)
        await morning.finish(msg)

noon = on_keyword('中午好')

@noon.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    if '中午好' in str(event.get_message()):
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

afternoon = on_keyword('下午好')

@afternoon.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    if '下午好' in str(event.get_message()):
        hour_num=datetime.now().hour
        id = str(event.get_user_id())
        at_ = "[CQ:at,qq={}]".format(id)
        if hour_num >=7 and hour_num <=10:
            msg = at_+'宝贝，是不是睡眠不够脑袋不清楚了...现在是早晨！'
        elif hour_num >=10 and hour_num <= 14:
            msg = at_+'快去睡午觉吧宝贝！'
        elif hour_num <=7:
            msg = at_+'你是猫头鹰嘛！！我超喜欢猫头鹰！！主人也是...'
        elif hour_num >= 19:
            msg = at_+'睡午觉睡昏了吧小猪崽！！！现在是晚上！'
        else:
            msg = at_+'现在是下午茶时间，要来喝杯茶么?'
        msg = Message(msg)
        await afternoon.finish(msg)

evening = on_keyword('晚上好')

@evening.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    if '晚上好' in str(event.get_message()):
        hour_num=datetime.now().hour
        id = str(event.get_user_id())
        at_ = "[CQ:at,qq={}]".format(id)
        if hour_num >=7 and hour_num <=10:
            msg = at_+'宝贝，是不是睡眠不够脑袋不清楚了...现在是早晨！'
        elif hour_num >=10 and hour_num <= 14:
            msg = at_+'快去睡午觉吧宝贝！'
        elif hour_num <=7:
            msg = at_+'你是猫头鹰嘛！！我超喜欢猫头鹰！！主人也是...'
        elif hour_num >= 19:
            msg = at_+'晚上好呀！今天也是收获满满的一天呢！！'
        else:
            msg = at_+'明明还没有到晚上呢！让我再睡会儿！！'
        msg = Message(msg)
        await evening.finish(msg)