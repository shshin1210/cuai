from logging import NullHandler
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.lezhin.com'
# 레진코믹스 카테고리 별 url
category = ['/ko/romance?page=', '/ko/boys?page=', '/ko/drama?page=', '/ko/bl?page=']
category_num = [30, 22, 27, 21]

id_list = []
title_list = []
author_list = []
genre_list = []
story_list = []
platform_list = []
age_tmp = []
age_list = []
rate_list = []
complete_list = []
free_list = []
thumbnail_list = []
url_list = []
num = 0

for i in range(4):
    page_num = 0
    for page_num in range(category_num[i]):
        URL = url + category[i] + str(page_num) + '&sub_tags=all'
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(executable_path=r'C:/Users/82108/Downloads/chromedriver_win32/chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get(URL)

        sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sleep(1)

        tmp = soup.find('ul', {'id' : 'exhibit-sub-tags'})
        title = tmp.find_all('div', {'class' : 'lzComic__title'})
        author = tmp.find_all('div', {'class' : 'lzComic__artist'})
        thumbnail_tmp = []
        for srcset in tmp.find_all('picture', {'class' : 'lzComic__img'}):
            if srcset.find('source')['srcset'] != '//ccdn.lezhin.com/files/assets/blank.png':
                thumbnail_tmp.append(srcset.find('source')['srcset'])
            else:
                thumbnail_tmp.append(srcset.find('source')['data-srcset'])
        url_tmp = []
        for href in tmp.find_all('li', {'class' : 'lzComic__item'}):
            url_tmp.append(url + href.find('a')['href'])
        sleep(3)
        p = 0

        for j in range(len(title)):
            t = title[j].text
            if (t in title_list):
                p += 1
                continue

            id_list.append(num)
            num += 1
            title_list.append(t)
            author_list.append(author[j].text)
            platform_list.append('레진코믹스')
            complete_list.append('연재중')
            free_list.append('유료')
            rate_list.append('null')
            thumbnail_list.append(thumbnail_tmp[j])
            url_list.append(url_tmp[j])

            ##### Change Page #####
            ### 장르, 태그(줄거리), 연령대, 평점)
            driver.get(url_tmp[p])
            ### sleep(1)

            #page = WebDriverWait(driver, 10).until(
            #    EC.presence_of_all_elements_located(
            #        (By.CLASS_NAME, 'lzComic__link')
            #    )
            #)
            #page[p].click()
            sleep(3)
            p += 1
            
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            sleep(2)

            try:
                genre = soup.find('span', {'class' : 'comicInfo__category comicInfo__category--genre'})
                genre_list.append(genre.text)
                while (len(genre_list) != (num)):
                    del genre_list[-1]

            except Exception as e:
                genre_list.append('error')

            try:
                age = soup.find('span', {'class' : 'comicInfo__category comicInfo__category--etc'})
                age_tmp.append(age.text)
                while (len(age_tmp) != (num)):
                    del age_tmp[-1]
            except Exception as e:
                age_tmp.append('error')

            if '19' in age_tmp[j]:
                age_list.append(19)
            elif '15' in age_tmp[j]:
                age_list.append(15)
            else:
                age_list.append(0)

            try:
                story_tmp = soup.find('meta', {'name' : 'description'})
                story = str(story_tmp['content'])
                story = story.replace('<p>', '').replace('</p>', '').replace('<br/>', '\n')
                story_list.append(story)
            except Exception as e:
                story_list.append('error')

            #story = soup.find_all('p')
            #story = str(story[1])
            #story = story.replace('<p>', '').replace('</p>', '')

            driver.back()

            sleep(2)
            
            page_num += 1

    ##### 완결목록 분류 #####

##### 기다리면 무료 따로 분류 #####

total_data = pd.DataFrame()
total_data['id'] = id_list
total_data['title'] = title_list
total_data['author'] = author_list
total_data['genre'] = genre_list
total_data['platform'] = platform_list
total_data['story'] = story_list
total_data['age'] = age_list
total_data['rate'] = rate_list
total_data['complete'] = complete_list
total_data['free'] = free_list
total_data['thumbnail'] = thumbnail_list
total_data['website'] = url_list
total_data.to_csv('레진코믹스_웹툰_스토리 추가 ver 2.0.csv', encoding='utf-8-sig')