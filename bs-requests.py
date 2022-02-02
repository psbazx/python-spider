# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
import requests

headers = {'Referer':'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4', 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

def request_url(url):
   try:
       response = requests.get("https://movie.douban.com/top250?",headers=headers)
       if response.status_code == 200:
           return response.text
   except requests.RequestException:
       return None

def main(page):
   url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
   html = request_url(url)
   soup = BeautifulSoup(html, 'lxml')
   list = soup.find(class_='grid_view').find_all('li')
   for item in list:
       item_name = item.find(class_='title').string
       item_img = item.find('a').find('img').get('src')
       item_index = item.find(class_='').string
       item_score = item.find(class_='rating_num').string
       item_author = item.find('p').text
       item_intr = item.find(class_='inq').string

       # print('爬取电影：' + item_index + ' | ' + item_name +' | ' + item_img +' | ' + item_score +' | ' + item_author +' | ' + item_intr )
       print('爬取电影：' + item_index + ' | ' + item_name + ' | ' + item_score + ' | ' + item_intr)


if __name__ == "__main__":
    for i in range(0, 10):
        main(i)