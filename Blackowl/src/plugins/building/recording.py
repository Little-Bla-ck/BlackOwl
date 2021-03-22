from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message,GroupMessageEvent
from datetime import datetime
import json

recording = on_command('记录')
