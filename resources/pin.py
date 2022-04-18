from pyrogram import Client as client, filters




@client.on_message(filters.command("pin") & filters.group)
async def pin(client, message):
	chat_id = message.chat.id
	
	if not message.reply_to_message:
		return await message.reply_text("Please reply to a message")
	else:
		admin_check = await client.get_chat_members(chat_id, message.from_user.id)
		if admin_check.status not in "administrator" or "creator":
			await message.reply_text("You're not an admin of this group")
		else:
			await client.pin_chat_message(chat_id, message_id)
			return True
