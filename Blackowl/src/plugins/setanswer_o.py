from nonebot import on_command
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent
from datetime import datetime
import json

setanswer_o = on_command('说话')

@setanswer_o.handle()
async def answerinput(bot:Bot,event:GroupMessageEvent,state:T_State):
    dataoutput = str(event.get_message()).strip()
    if dataoutput:
        dataoutput_list = dataoutput.split()
        state['command'] = dataoutput_list[0]
        #await setanswer_o.finish(f"database does not have {dataoutput_list[0]} command!")

@setanswer_o.got('command')
async def answeroutput(bot:Bot,event:GroupMessageEvent,state:T_State):
    with open("setanswer.json", "r",encoding = 'utf-8') as f:
        data = json.load(f)
    if state['command'] in data:
        msg = data[state['command']]
        await setanswer_o.finish(msg)
    else:
        await setanswer_o.finish(f"database does not have {state['command']} command!")