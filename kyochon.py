from bs4 import BeautifulSoup 
import urllib.request
import pandas as pd

result=[]

for sido in range(1, 18):
  for gu in range(1,45):
    try:
      Kyochon_url = 'https://www.kyochon.com/shop/domestic.asp?sido1=%s&sido2=%s&txtsearch='%(sido, gu)
      html = urllib.request.urlopen(Kyochon_url)
      soupKyochon = BeautifulSoup(html, 'html.parser')
      li_list = soupKyochon.select("div>div>div>div>ul.list>li")

      length = len(li_list)
      for i in range(0, length):
        store_name = li_list[i].strong.string
        a = li_list[i].em.get_text().strip().split('\r')[0]
        store_sido = a.split()[:2]
        store_sido = store_sido[0]+", "+store_sido[1]
        store_address =  li_list[i].em.get_text().strip().split('\r')[0]
        result.append([store_name]+[store_sido]+[store_address])
    except:
      pass

Kyochon_tbl = pd.DataFrame(result, columns = ('store', 'sido-gu', 'address'))
Kyochon_tbl.to_csv("kyochon.csv", encoding = "utf8", mode = "w", index = True)
