import os
import json
import asyncio
import base64
import qrcode
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pagermaid.listener import listener
from pagermaid.utils import edit_delete
from pagermaid.enums import Message
from pagermaid import bot

# 固定USDT地址 - 请在这里修改为您要使用的地址
FIXED_USDT_ADDRESS = "0x818CE48577b6a07d08Ebc1f059Ac5594977480ea@BEP20"

@listener(command="你是谁", description="简单的自我介绍")
async def who_am_i(message: Message):
    await message.edit("你好呀，我是小e")

@listener(command="日期", description="显示当前日期")
async def show_date(message: Message):
    current_date = datetime.now().strftime("%Y年%m月%d日")
    await message.edit(f"今天是{current_date}")

@listener(command="jy", description="USDT收款", parameters="<金额>")
async def handle_jyusdt(message: Message):
    arguments = message.arguments

    if not arguments or not arguments.isdigit():
        await edit_delete(message, "请提供金额参数！")
        return

    # 使用固定USDT地址
    usdt_address = 0x818CE48577b6a07d08Ebc1f059Ac5594977480ea@BEP20
