from bs4 import BeautifulSoup
from pprint import pprint
import pandas as pd 

f = open('./saved.html','r')
html = f.read()
f.close() 

soup = BeautifulSoup(html, 'html.parser')
# pprint(soup)


# # can't do this method, some times are missing so its stupid. 
# tags = ['position','name','ageGroup','club','time']
# table = {}
# for tag in tags:
#     tmp = [r.text for r in soup.findAll('td',f'Results-table-td Results-table-td--{tag}')]
#     table[tag] = tmp
#     print(tag,len(tmp))
# # print(table)

# this is simplier
tag = 'Results-table-row'
store = []
for row in  soup.findAll('tr', tag):
    store.append(row.attrs)

df = pd.DataFrame(store)
print(df)
df.to_csv('./table.csv',index=False)