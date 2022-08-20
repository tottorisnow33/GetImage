import requests
from bs4 import BeautifulSoup
import os
import csv
import time
import urllib.error
import urllib.request


#参考URL
#https://qiita.com/kaito_111/items/5c1d7b7232a6da821728
#https://note.nkmk.me/python-download-web-images/

########################################
#ダウンロード & 保存
#参考URLから引用
########################################
def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


#テキストファイルからURL一覧読み込み
f = open('./input/input.txt', 'r')
URLlist = f.readlines()

print(URLlist)
#ページURLループ
for page_url_cnt in range(len(URLlist)):

  #ページ指定
  page_url = URLlist[page_url_cnt]

  #ページのイメージタグの一覧取得
  r = requests.get(page_url)
  soup = BeautifulSoup(r.text)
  img_tags = soup.find_all("img")

  #URL内部の画像URLをリストに格納
  str_img_urls_list = []
  for img_tag in img_tags:
    url = img_tag.get("src")

    #正しいフォーマット出でない場合スキップ
    if url == None: continue
    if("gif" in url): continue

    str_img_urls_list.append(url)

  #画像URLループ
  for cnt in range(len(str_img_urls_list)):
    str_img_url = str_img_urls_list[cnt]
    print(str_img_url)

    #画像ダウンロード
    download_file(str_img_url, "./output/" + str(page_url_cnt) + "_" + str(cnt) + ".png")
    time.sleep(1)

