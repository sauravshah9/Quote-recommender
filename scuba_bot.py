import requests
import os
import time
import mysql.connector
import bs4
import lxml
import time
# from pymongo import MongoClient


def database_login() :
    command_data_base= mysql.connector.connect(
    host="localhost",
    user="root",
    password="saurav",
    database="quotes_db"
    )
    return(command_data_base)

command_data_base=database_login()
time.sleep(1)
mycursor=command_data_base.cursor()

url1 ="https://www.scuba.io/blog/48-analytics-quotes-experts"

header1 = {
    "authority": "www.scuba.io",
"method": "GET",
"path": "/blog/48-analytics-quotes-experts",
"scheme": "https",
 "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
# cookie: advanced_ads_browser_width=1263; advanced_ads_pro_server_info=%7B%22vc_cache_reset%22%3A0%7D; footer_closed=1; boxzilla_box_82996=true; advanced_ads_page_impressions=%7B%22expires%22%3A1991878432%2C%22data%22%3A2%7D
# if-modified-since: Thu, 16 Feb 2023 00:34:30 GMT
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "cross-site",
# "sec-fetch-user": "?1",
"sec-gpc": "1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

session = requests.session()
html1=session.get(url1,headers=header1,verify=False)
soup1=bs4.BeautifulSoup(html1.text,'lxml')
# print(soup1.encode('utf-8'))


quotes = soup1.find_all('p')
quotes_list = []
for data in quotes[9:69]:
    if "CEOs and Founders" or "Often becoming a VC" or "especially in the tech world" or "Product is at the heart of analytics" not in data.text:
        # print(data.text)
        quotes_list.append(data.text.strip())

# print(len(quotes_list))

authors = soup1.find_all('a')
authors_list = []

for auth in authors[50:100]:
    # print(auth.text)
    authors_list.append(auth.text.strip())

for x in range(0,10):
    authors_list.append("")

new_list = list(zip(quotes_list,authors_list))
# print(new_list)

sql_regi1="INSERT INTO scuba(quotes,author) VALUES (%s,%s)"
mycursor.executemany(sql_regi1, new_list)
print("insterted")
command_data_base.commit()