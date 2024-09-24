##IPL Auction 2022 Web Scraping Script

This Python script scrapes data from the IPL 2022 auction webpage and saves it to a CSV file using BeautifulSoup for HTML parsing and pandas for data manipulation.

Steps in the code:
Import Libraries:

requests is used to fetch the content of the webpage.
BeautifulSoup from bs4 helps parse the HTML data.
pandas is used to store and manipulate the scraped data.
Fetching the Web Page:

python
Copy code
r = requests.get(url)
The webpage is fetched using the requests library, and its HTML content is stored.

Parsing the HTML:

python
Copy code
soup = BeautifulSoup(r.text, "lxml")
The content is parsed with BeautifulSoup using the lxml parser.

Extracting the Table:

python
Copy code
table = soup.find("table", class_="ih-td-tab auction-tbl")
The table with auction data is found by specifying the class name.

Extracting Table Headers:

python
Copy code
title = table.find_all("th")
header = [i.text for i in title]
df = pd.DataFrame(columns=header)
The headers (column names) of the table are extracted and used to create a pandas DataFrame.

Extracting Table Rows and Data:

python
Copy code
rows = table.find_all("tr")
for i in rows[1:]:
    first_col = i.find_all("td")[0].find("div", class_="ih-pt-tbl")
    remove_spaces = first_col.text.strip() if first_col is not None else "N/A"
    data = [tr.text.strip() for tr in i.find_all("td")[1:]]
    row.insert(0, remove_spaces)
    df.loc[len(df)] = row
Each row of the table is iterated over. The player's name (first column) and the remaining columns are extracted, cleaned up (extra spaces removed), and appended to the DataFrame.

Saving the Data to CSV:

python
Copy code
df.to_csv("IPL Auction 2022.csv")
The extracted data is saved as a CSV file named IPL Auction 2022.csv.

