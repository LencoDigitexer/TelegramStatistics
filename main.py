import configparser
import json
import pandas

import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import GetMessageReactionsList

# Считываем учетные данные
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

chat_id = -1001434363272
chat_name = "c/1434363272"

app = Client("my_account", api_id, api_hash)

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        peer = await app.resolve_peer(chat_id)
        
        print(peer)
        posts = []
        async for message in app.get_chat_history(chat_id=chat_id):

            print(message)
            reactions = []
            if message.reactions:
                for reaction in message.reactions:
                    print("Всего типов реацкий " + str(reaction))
                    reactions.append({
                     	"emoji":reaction.emoji,
                      	"count":reaction.count})
            posts.append({
                "id": message.id,
   				"reactions": reactions,
                "views":message.views})
            
        print(reactions)
        with open(str(chat_id) + '.json', 'w', encoding='utf8') as outfile:
         	json.dump(posts, outfile, ensure_ascii=False)
          
        re = []
        
        for data in posts:
            a = 0
            print("Всего типов реацкий " + str(len(data["reactions"])))
            for count in data["reactions"]:
                a = a + int(count["count"])
            print(a)  
            re.append({
						"id": "https://t.me/" + chat_name + "/" + str(data["id"]),
						"reactions": str(a),
      					"views": data["views"]})
   
        with open(str(chat_id) + '_re.json', 'w', encoding='utf8') as outfile:
            json.dump(re, outfile, ensure_ascii=False)
            
        pandas.read_json(str(chat_id) + '_re.json').to_excel(str(chat_id) + '_re.xlsx')



asyncio.run(main())