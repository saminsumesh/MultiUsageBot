import asyncio
from pyrogram import Client, filters
from time import time
      
@Client.on_message(filters.command("kick") & filters.group)
async def kick(client, message):
     user_id = message.from_user.id
     chat_id = message.chat.id
     reply_m = message.reply_to_message
     if reply_m:
           user_client = await client.get_chat_members(chat_id, user_id)
           admin_check = ["creator", "administrator"]
           if user_client.status not in admin_check:
               await message.reply_text("Sorry you're not an admin")
           else:
               await client.ban_chat_member(chat_id, user_id,  int(time()) + 400)
               await message.reply_text("One has turned into bytes")
     else:
           dd=await message.reply_text("Please reply to a message")
           await asyncio.sleep(6)
           await dd.delete()
                        
