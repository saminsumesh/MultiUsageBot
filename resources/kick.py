from pyrogram import Client, filters
      from time import time
      
@Client.on_message(filters.command("kick") & filters.group)
async def kick(client, message):
     user_id = message.reply_to_message.from_user.id
     chat_id = message.chat.id
     reply_m = message.reply_to_message
     if reply_m:
           user = await client.get_chat_memebers(message.chat.id, reply_m.from_user.id)
     else:
           await message.reply_text("Please reply to a message")
                  
           if user.status not in ("administrator" or "creator"):
               await message.reply_text("Sorry you're not an admin")
           else:
               await client.ban_chat_member(chat_id, user_id,  int(time()) + 400)
               await message.reply_text("One has turned into bytes")
                        
