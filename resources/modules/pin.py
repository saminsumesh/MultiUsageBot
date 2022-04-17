import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.helpers.admin_filter_m import admin_misc




@Client.on_message(filters.command("pin") & admin_misc)
async def pin(_, message: Message):
	chat_id = message.chat.id
	message_id = message_id
	if not message.reply_to_message:
		return
	await message.reply_to_message.pin(chat_id, message_id)
	await message.reply_text("Message have been pinned")
	
@Client.on_message(filters.command("unpin") & admin_misc)
async def unpin(_, message: Message):
	chat_id = message.chat.id
	message_id = message_id
	if not message.reply_to_message:
		return
	await message.reply_to_message.unpin(chat_id, message_id)
	await message.reply_text("Message have been unpinned")
