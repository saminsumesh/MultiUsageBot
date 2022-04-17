import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from resources.helpers.admin_filter_m import admin_misc

@Client.on_message(filters.command("pin", "!") & admin_misc)
async def pin(_, message: Message):
	if not message.reply_to_message:
		return
        await message.reply_to_message.pin()
        await message.reply("Sucessfully Pinned The Message")
	await asyncio.sleep(10)
	await message.delete()
		
@Client.on_message(filters.command("unpin", "!") & admin_misc)
async def unpin(_, message: Message):
	if not message.reply_to_message:
		return
	await message.reply_to_message.unpin()
	await message.reply_text("Successfully unpinned the message")
	await asyncio.sleep(10)
	await message.delete()
	
