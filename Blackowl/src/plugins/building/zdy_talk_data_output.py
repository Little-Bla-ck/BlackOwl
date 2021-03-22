from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime
import json

zdy_talk = on_command('对话')

@zdy_talk.handle()
async def talk_return_get(bot: Bot, event: GroupMessageEvent, state: T_State):
    raw_args = str(event.get_message()).strip()
    if raw_args:
        arg_list = raw_args.split()
        state['command'] = arg_list[0]

    

@zdy_talk.got('command', 'return')
async def talk_return(bot: Bot, event: GroupMessageEvent, state: T_State):
    with open("zdy_talk_data.json", "r",encoding = 'utf-8') as f:
        data = json.load(f)
    if state['command'] not in data:
        await zdy_talk.finish("没有找到此命令，试试新建一个吧~")
    id = str(event.get_user_id())
    # at_ = "[CQ:at,qq={}]".format(id)
    msg = data[state['command']]
    await zdy_talk.finish(msg)

'''
    QQ表情无法正常显示
    聊天过程中命令同音字兼容
'''