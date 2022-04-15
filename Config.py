from os import environ

class config(object):
       
       API_ID = int(environ.get("API_ID"))
       
       API_HASH = environ.get("API_HASH")
       
       BOT_TOKEN = environ.get("BOT_TOKEN")
       
