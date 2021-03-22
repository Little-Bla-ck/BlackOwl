from nonebot import on_command, on_keyword
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent

'''
本插件使用关键字来实现机器人自动识别用户语句中的关键词来进行自动回复
'''

ahthis = on_keyword('啊这阿哲')

@ahthis.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    if '说话' not in str(event.get_message()):
        if '啊这' in str(event.get_message()) or '阿哲' in str(event.get_message()):
            id = str(event.get_user_id())
            at_ = "[CQ:at,qq={}]".format(id)
            msg = at_+'你好笨唉，是听不懂说什么嘛...'
            msg = Message(msg)
            await ahthis.finish(msg)

allthis = on_keyword('就这')

@allthis.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    if '说话' not in str(event.get_message()):
        if '就这' in str(event.get_message()):
            id = str(event.get_user_id())
            at_ = "[CQ:at,qq={}]".format(id)
            msg = at_+'你行你上啊喂(#`O′)！'
            msg = Message(msg)
            await allthis.finish(msg)

zthyyds = on_keyword('张泰豪thgg')

@zthyyds.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    if '说话' not in str(event.get_message()):
        if '张泰豪' in str(event.get_message()) or 'thgg' in str(event.get_message()):
                msg = "[CQ:face,id=2]"+'永远滴神！！！'
                msg = Message(msg)
                await zthyyds.finish(msg)

ysjx = on_keyword('有手就行')

@ysjx.handle()
async def h_r(bot:Bot, event:GroupMessageEvent,state:T_State):
    if '说话' not in str(event.get_message()):
        if '有手就行' in str(event.get_message()):
            id = str(event.get_user_id())
            at_ = "[CQ:at,qq={}]".format(id)
            msg = at_+'别骂了别骂了555~'+"[CQ:face,id=5]"
            msg = Message(msg)
            await ysjx.finish(msg)
