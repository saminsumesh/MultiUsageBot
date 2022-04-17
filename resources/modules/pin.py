import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.helpers.admin_filter_m import admin_misc


@Client.on_message(filters.command("pin") & admin_misc & filters.group)
async def pin(_, message: Message):
	chat_id = message.chat.id
	message_id = message_id
	if not message.reply_to_message:
		return
	await message.pin()
	await message.reply_text("Message have been pinned")
	
@Client.on_message(filters.command("unpin") & admin_misc & filters.group)
async def unpin(_, message: Message):
	chat_id = message.chat.id
	message_id = message_id
	if not message.reply_to_message:
		return
	await message.unpin()
	await message.reply_text("Message have been unpinned")
