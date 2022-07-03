import pandas
pandas.read_json("re.json").to_excel("re.xlsx")
'''
json_file = eval('{"id": 1875, "date": "2022-06-29 22:42:22", "reactions": []}, {"id": 1874, "date": "2022-06-29 22:42:22", "reactions": [{"emoji": "🥰", "count": 6}, {"emoji": "👏", "count": 1}]}')
df = pandas.DataFrame(json_file).to_excel("excel.xlsx")'''