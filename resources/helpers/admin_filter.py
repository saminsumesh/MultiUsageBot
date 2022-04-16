from pyrogram.types import *
      

async def admin_check(message: Message):
      if not message.from_user:
        return False
      
      if message.chat.type not in ["supergroup", "channel"]:
      	return False

      if message.from_user.id in [123456, 1468900900]:
        return True

      client = message._client 
      user_id = message.from_user.id
      chat_id = message.chat.id
      
      admin_status = await client.get_chat_members(chat_id, user_id)
      check_admin = ["administrator", "creator"]
      if admin_status not in check_admin:
      	return False
      else:
      	return True
