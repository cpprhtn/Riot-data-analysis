import requests
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

faker_opgg_url = 'https://www.op.gg/summoner/userName=Hide%20on%20bush'

options = Options()

driver = webdriver.Chrome(
     options=options
     )
driver.get(faker_opgg_url)
driver.maximize_window()
# wait = WebDriverWait(driver, 1)

# queue_select = Select(driver.find_element_by_css_selector('select.SelectMatchTypes'))
# queue_select = driver.find_element(By.CSS_SELECTOR,'css-inknuf')
while True:
    try:
        driver.find_element_by_css_selector('.more').click()
        # 게임 로딩, html 코드 변경까지 여유 시간을 1초 가집니다.
        time.sleep(1)
        
    # 에러가 나면(페이지에서 '더 보기' 버튼이 없을 경우) while문을 탈출합니다.
    except Exception as e:
        pass
        break

# 게임이 모두 로딩된 페이지의 html 코드를 faker_total_html로 저장합니다.
faker_total_html = driver.page_source

# selenium이 제어하는 크롬을 종료합니다.
driver.quit()

faker_total_soup = BeautifulSoup(faker_total_html, 'html.parser')
print(faker_total_soup)

# 결과가 들어갈 빈 리스트를 만듭니다.
faker_champions = []
faker_kills = []
faker_deaths = []
faker_assists = []
faker_results = []

# 전체 html 코드 중 우리가 원하는 selector를 만족하는 것만 가져오기
faker_total_games_html = faker_total_soup.select('div.css-164r41r.esvl4yu0 div.game-content')

# 그렇게 가져온 html 코드의 element 개수 == 끝까지 로딩된 모든 게임 수 출력
total_game_len = len(faker_total_games_html)
print(total_game_len)

# 각 게임에 대해 웹 페이지에 기재된 스탯을 찾아서(selector 사용) 결과 리스트에 append하기
for i in range(total_game_len):
    faker_champions.append(''.join(s for s in list(faker_total_games_html[i].select_one('div.info div.champion div.icon').find('img')['alt'])))
    faker_kills.append(list(faker_total_games_html[i].select_one('div.kda div.k-d-a').find('span'))[0])
    faker_deaths.append(list(faker_total_games_html[i].select_one('div.kda div.k-d-a span.d'))[0])
    faker_assists.append(list(faker_total_games_html[i].select_one('div.kda div.k-d-a').find_all('span')[2])[0])
    faker_results.append(list(faker_total_games_html[i].select_one('div.game div.result'))[0])


faker_total_df = pd.DataFrame([faker_champions,
                                faker_results,
                                faker_kills,
                                faker_deaths,
                                faker_assists],
                               index = ['champion', 'result', 'kills', 'deaths', 'assists']).T

faker_total_df.to_csv('faker_total_df.csv', index=False)
df = pd.read_csv('faker_total_df.csv')