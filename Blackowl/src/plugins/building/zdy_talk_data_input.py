from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime
import json

zdy_talk = on_command('自定义对话')
zdy_talk_data = {}


@zdy_talk.handle()
async def first_receive(bot: Bot, event: GroupMessageEvent, state: T_State):
    raw_args = str(event.get_message())
    if raw_args:
        arg_list = raw_args.split()
        await zdy_talk.send(arg_list)
        # 将参数存入state以阻止后续再向用户询问参数
        # 命令格式：/自定义对话 添加/删除 命令 回复
    state['manager'] = arg_list[0]
    if arg_list[0] == '删除':
        state['command'] = arg_list[1]
        if len(arg_list) != 2:
            await zdy_talk.finish("请检查你的输入，输入'自定义对话 帮助'查看操作手册~")
    if arg_list[0] == '添加':
        if len(arg_list) != 3:
            await zdy_talk.finish("请检查你的输入，输入'自定义对话 帮助'查看操作手册~")
        state['command'] = arg_list[1]
        state['return'] = arg_list[2]
    if arg_list[0] == '帮助':
        if len(arg_list) != 1:
            await zdy_talk.finish("请检查你的输入，输入'自定义对话 帮助'查看操作手册~")

@zdy_talk.got('manager', 'command', 'return')
async def command_produce(bot: Bot, event: GroupMessageEvent, state: T_State):
    with open("zdy_talk_data.json", "r",encoding = 'utf-8') as f:
        data = json.load(f)
    if state['manager'] == '删除':
        if state['command'] not in data:
            await zdy_talk.reject(f"未找到{state['command']}命令，请检查你的输入~")
        else:
            del data[state['command']]
            with open("zdy_talk_data.json", "w",encoding = 'utf-8') as f:
                f.write(json.dumps(data,ensure_ascii=False))
            await zdy_talk.finish(f"已删除'{state['command']}'命令~")
    
    if state['manager'] == '添加':
        data[state['command']] = state['return']
        with open("zdy_talk_data.json", "w",encoding = 'utf-8') as f:
            f.write(json.dumps(data,ensure_ascii=False))
        await zdy_talk.finish(f"命令：{state['command']}\n回复：{state['return']}\n已保存~")
    
    if state['manager'] == '帮助':
        await zdy_talk.send(f"命令格式：\n自定义对话 功能 命令 回复\n例：自定义对话 添加 你好 你好啊~\n功能列表：删除 添加 帮助\n")
        '''
        await zdy_talk.send("指令列表：\n")
        for command in data:
            await zdy_talk.send(f"'{command}':'{data[command]}'\n")
        '''
        await zdy_talk.finish()
    
