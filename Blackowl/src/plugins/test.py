from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

test = on_command('test')

@test.handle()
async def h_r(bot:Bot,event:GroupMessageEvent,state: T_State):
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'你好'
    msg = Message(msg)
    await test.finish(msg)
