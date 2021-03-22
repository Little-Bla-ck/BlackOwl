from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent,PrivateMessageEvent
from datetime import datetime

help_system = on_command('帮助')

@help_system.handle()
async def helping(bot:Bot, event:PrivateMessageEvent, state:T_State):
    msg = '你好,这里是lucky!\n我现在会以下功能:\n关键词回复(只要你的句子中带有以下内容，我就会回复你啦！):\n早上好 中午好 下午好 晚上好'
    msg = msg + '\n命令词回复(请按照相应游戏后括号内的格式输入，<>内为选择输入的内容！请注意空格！):\n猜拳游戏(猜拳 <石头/剪刀/布>)'
    msg = Message(msg)
    await help_system.finish(msg)