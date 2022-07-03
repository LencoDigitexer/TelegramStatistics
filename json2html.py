from tabulate import tabulate
import json


with open('-1001276508753.json') as f:
    table = json.load(f)
    
print(table)

emoji = 0

tables = [['id', 'reactions']]
posts = []


for data in table:
    print(data)
    a = 0
    print("Всего типов реацкий " + str(len(data["reactions"])))
    for count in data["reactions"]:
        a = a + int(count["count"])
    print(a)  
    posts.append({
                "id": "https://t.me/tyan_channel/" + str(data["id"]),
   				"reactions": str(a)})

with open('re.json', 'w', encoding='utf8') as outfile:
    json.dump(posts, outfile, ensure_ascii=False)

'''
html = tabulate(tables, tablefmt='html')

with open('index.html', 'w') as the_file:
    the_file.write(html)'''