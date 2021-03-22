from nonebot import on_command
from nonebot.adapters import Bot,Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message, GroupMessageEvent
from datetime import datetime
import json

'''
本插件通过 识别命令 来 允许用户 自定义创建 机器人对话内容
building————
'''

setanswer_i = on_command('test')

@setanswer_i.handle()
async def datainput(bot:Bot,event:GroupMessageEvent,state:T_State):
    datainput_list = str(event.get_message()).split()
    if datainput:
        state['operate'] = datainput_list[0]
        if len(datainput_list) == 3 and datainput_list[0] == '添加':
            state['command'] = datainput_list[1]
            state['answer'] = datainput_list[2]
            await setanswer_i.send('adding system is operating')
        elif len(datainput_list) == 2 and datainput_list[0] == '删除':
            state['command'] = datainput_list[1]
            await setanswer_i.send('deleting system is operating')
        elif len(datainput_list) == 1 and datainput_list[0] == '帮助':
            await setanswer_i.send('helping system is operating')
        else:
            await setanswer_i.finish('please check your input!')

@setanswer_i.got('operate','command','answer')
async def datadispose(bot:Bot,event:GroupMessageEvent,state:T_State):
    with open("setanswer.json", "r",encoding = 'utf-8') as f:
        data = json.load(f)
    if state['operate'] == '删除':
        if state['command'] not in data:
            await setanswer_i.reject(f"{state['command']} command is not exist!")
        else:
            del data[state['command']]
            with open("setanswer.json", "w",encoding = 'utf-8') as f:
                f.write(json.dumps(data,ensure_ascii=False))
            await setanswer_i.finish(f"{state['command']}' command has been deleted!")

    if state['operate'] == '添加':
        data[state['command']] = state['answer']
        with open("setanswer.json", "w",encoding = 'utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False))
        await setanswer_i.finish(f"command:{state['command']}\nanswer：{state['answer']}\n operate successfully!")