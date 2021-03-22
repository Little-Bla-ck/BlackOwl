from nonebot import on_command,on_keyword
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent,PrivateMessageEvent
from datetime import datetime
from random import randint

Mora_Game = on_command('猜拳')

@Mora_Game.handle()
async def Mora(bot:Bot, event:PrivateMessageEvent, state:T_State):
    randomnumber = randint(1,3)
    playerinput = str(event.get_message())
    if playerinput == '剪刀' or playerinput == '石头' or playerinput == '布':
        if playerinput =='剪刀':
            if randomnumber == 1:
                msg = '我出布！可恶，小看你了。'
            elif randomnumber == 2:
                msg = '我出石头！轻轻松松。'
            else:
                msg = '我出剪刀！嘿嘿，是平局。'
        elif playerinput == '石头':
            if randomnumber == 1:
                msg = '我出布！轻轻松松。'
            elif randomnumber == 2:
                msg = '我出石头！嘿嘿，是平局。'
            else:
                msg = '我出剪刀！可恶，小看你了。'
        else:
            if randomnumber == 1:
                msg = '我出布！嘿嘿，是平局。'
            elif randomnumber == 2:
                msg = '我出石头！可恶，小看你了。'
            else:
                msg = '我出剪刀！轻轻松松。'
    else:
        msg = '请检查输入哦，我看不懂唉！'
    await Mora_Game.finish(msg)