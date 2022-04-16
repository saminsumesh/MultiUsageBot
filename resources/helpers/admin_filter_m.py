from pyrogram import filters
from resources.helpers.admin_filter import admin_check

async def admin_filt(filter, client, message):
	return (
		not message.edit_date
		and await admin_check(message)
		)
admin_misc = filters.create(func=admin_filt, name="AdminMisc")
