from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

ahthis = on_command('啊这')

@ahthis.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'你好笨唉，是听不懂说什么嘛...'
    msg = Message(msg)
    await ahthis.finish(msg)

allthis = on_command('就这')

@allthis.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'你行你上啊喂(#`O′)！'
    msg = Message(msg)
    await allthis.finish(msg)

zthyyds = on_command('张泰豪')

@zthyyds.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    msg = '永远滴神！！！'
    msg = Message(msg)
    await zthyyds.finish(msg)

ysjx = on_command('这不有手就行')

@ysjx.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    id = str(event.get_user_id())
    at_ = "[CQ:at,qq={}]".format(id)
    msg = at_+'别骂了别骂了555~'
    msg = Message(msg)
    await ysjx.finish(msg)
