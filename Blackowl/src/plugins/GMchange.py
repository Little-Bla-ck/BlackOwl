from nonebot import on_notice
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot,Message, GroupDecreaseNoticeEvent,GroupIncreaseNoticeEvent

GMchange = on_notice()
@GMchange.handle()
async def _(bot:Bot,event:GroupIncreaseNoticeEvent,state:T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '进群就不要想走了哦~！！！'
    msg = Message(msg)
    await GMchange.finish(message=msg)

#群友退群
@GMchange.handle()
async def _(bot:Bot,event:GroupDecreaseNoticeEvent,state:T_State):
    user = event.get_user_id()
    at_ = "[CQ:at,qq={}]".format(user)
    msg = at_ + '这座城市又多了一位伤心人...'
    msg = Message(msg)
    await GMchange.finish(message=msg)