from os import environ 

class Config:
    API_ID = environ.get("19024658", "577678")
    API_HASH = environ.get("9c5b1808b35bc2ae8195351ece057576", "d2c6e01uuiuiouioiuiou0fc6d7a1be")
    BOT_TOKEN = environ.get("7111533028:AAG5SUFUpSP70l7bJqmDnRNzl-W8DfYR6c8", "70955...") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chhjgjkkjhkjhkjh@cluster0.xowzpr4.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
