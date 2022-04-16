import asyncio
from pyrogram import Client, filters
from pyrogram.types import *
from Config import config

@Client.on_message(filters.command("start"))
async def cmd_start(client: Client, message):
       await m.reply_sticker("CAACAgUAAxkBAAECR3tiWb91o93XJ4mkKyQwQkUFAoMrogACVwQAAuml6Fdl-rneiql81B4E", reply_to_message=reply_to_message.id
       )

@Client.on_message(filter.command("purge") & filters.group)
async def delete(client: Client, m: Messages):
       if message.chat.type not in (("supergroup" or "channel")):
              return
       
       status = await message.reply_text("This command only works on Groups or Supergroups")
       await asyncio.sleep(15)
       await message.delete()
       count_del = 0
       msg_id = []
       reply_to = message.reply_to_message
       
       if reply_to:
           users = await get_chat_member(message.chat.id, reply_to.from_user.id)
           if users.status == "administrator" or "creator":
      
               if reply_to:
                   for reply_msg_id in range(
                   message.reply_to_message.message_id, message.message_id):
                       msg_id.append(reply_msg_id)

                       if len(msg_id) == 4092:
                          await client.delete_messages(chat_id=message.chat.id, msg_id=msg_id, revoke=True)
                          count_del += len(msg_id)
                          msg_id = []

                          if len(msg_id) > 0:
                                await client.delete_messages(chat_id=message.chat.id, msg_id=msg_id, revoke=True)
                                count_del += len(msg_id)
                                await status.edit_text("Purge Started!!")
                                await asyncio.sleep(20)
                                await status.edit(f"deleted {count_del} messages")
                                await asyncio.sleep(15)
                                await status.delete()
                                                                    
@Client.on_message(filters.command("del") & filters.group)
async def del(client: Client, message):
      if message.chat.type not in (("supergroup" or "channel")):
            await message.reply("This message only works on Groups & Supergroup")
      else:
            try:
                  reply = message.reply_to_message
                  if reply:
                        admin_check = await get_chat_member(message.chat.id, reply.from_user.id)
                        if admin_check.status not in (("administrator" or "creator")):
                              await message.reply_text("You must me be atleast an admin to do that")
                  else:
                        await reply.message.delete()

@Client.on_inline_query()
async def google search(client: Client, update):
      results = google(update.query)
      answer = []
      for result in results:
            answer.append(
                  InlineQueryResultArticle(
                        title=result["title"], description=result["description"],
                        input_message=InputTextMessageContent(
                              message_text=result["text"]
                              disable_web_page_preview=True),
                   )
                 )
               )
                 await update.answer(answers)
                 
def google(query):
      r = requests.get(API + requote_uri(query))
      information = r.json()["results"][:50]
      results = []
      for info in information:
            text = f"**Title:** `{info['title']}`"
            text += f"\n**Description:** `{info['description']}`"
            text += f"\n**Made by @SaminSumesh**"
            results.append(
                  {
                        "title": info['title']
                        "description": info['description'],
                        "text": text,
                        "link": info['link']'
                  }
                  
            )
            return results


# work on progress need time to finish it
