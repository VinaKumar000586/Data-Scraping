import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
##print(r)

soup=BeautifulSoup(r.text,"lxml")
##print(soup)

table = soup.find("table", class_="ih-td-tab auction-tbl")  # Use class_ instead of Class_
title=table.find_all("th")
#print(title)

header = []
for i in title:
     name = i.text
     header.append(name)

print(header)

## Crerate the dataframe
df=pd.DataFrame(columns=header)
print(df)

##extractring the data.

rows=table.find_all("tr")
for i in rows[1:]:
    # Find the first column with class 'ih-pt-tbl'
    first_col = i.find_all("td")[0].find("div", class_="ih-pt-tbl")
    
    # Check if the div is found
    if first_col is not None:
        remove_spaces = first_col.text.strip()  # Strip any extra spaces
    else:
        remove_spaces = "N/A"  # Or some placeholder if the element isn't found

    # Get the remaining columns
    data = i.find_all("td")[1:]
    row = [tr.text.strip() for tr in data]  # Strip any extra spaces
    
    # Insert the first extracted value into the row
    row.insert(0, remove_spaces)
    
    # Append the row to the DataFrame
    df.loc[len(df)] = row


#create the csv file
df.to_csv("IPL Auction 2022.csv")