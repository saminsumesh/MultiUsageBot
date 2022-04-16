from pyrogram import Client, __version__
from pyrogram.raw.all import *
from Config import config

API_ID = config.API_ID
API_HASH = config.API_HASH
BOT_TOKEN = config.BOT_TOKEN

class Function(Client):
        
        
        def __init__(self):
                super().__init(
                        api_id=API_ID,
                        api_hash=API_HASH,
                        bot_token=BOT_TOKEN,
                        workers=50,
                        plugins={"root": "resources"},
                       )
        async def start(self):
               await super().start()
               me = await self.get_me()
               self.username = "@" + me.username
               print(f"{me.frist_name} with for Pyrogram v{__version__} (Layer {layer}) Started on {me.username}")

        async def stop(self, *args):
               super().stop()
               print("Bot stopped, Bye")

bot = Function()
bot.run()
