import asyncio
import time
from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def cmd_start(client: Client, message):
      username = message.from_user.first_name
      await message.reply_text(f"Hi {username}")
            )    
                   
