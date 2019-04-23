#!/usr/bin/env python
# coding: utf-8

#01. 라이브러리 Import
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re


#02. Dictionary 생성

sunroof_dict = {}
sunroof_dict['avg_monthly_bill'] =[]
sunroof_dict['coverage_percentage'] =[]
sunroof_dict['kW_size'] =[]
sunroof_dict['ft2_size'] =[]


#03. 크롬 드라이버 통해 Source Page로 이동

#크롬 드라이버 실행
driver = webdriver.Chrome('c:/development/chromedriver.exe')

#URL 설정
url='https://www.google.com/get/sunroof/building/34.0544888/-118.30090559999996/#?f=buy'

#해당 URL로 이동
driver.get(url)


#04. Page Source 전체 수집 후 파싱

html = driver.page_source
bs = BeautifulSoup(html, "html.parser")


#05. 각 항목 수집

#월 평균 전기료
avg_monthly_bill_tmp = bs.select("md-select-value")[0].text
avg_monthly_bill = re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", avg_monthly_bill_tmp)
sunroof_dict['avg_monthly_bill'].append(int(avg_monthly_bill[0]))

#전기 사용량 중 패널로 커버 가능한 정도(단위 : %)
coverage_percentage_tmp = bs.select("p.md-body")[1].text
coverage_percentage = re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", coverage_percentage_tmp)
sunroof_dict['coverage_percentage'].append(float(coverage_percentage[0]))

#kW size
kW_size_tmp = bs.select("div.recommended-kw")[0].text
kW_size = re.findall(r"(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", kW_size_tmp)
sunroof_dict['kW_size'].append(float(kW_size[0]))

#ft2 size
ft2_size_tmp = bs.select("div.recommended-area")[0].text
ft2_size = re.findall(r"\d+", ft2_size_tmp)
sunroof_dict['ft2_size'].append(int(ft2_size[0]))



sunroof_df = pd.DataFrame.from_dict(sunroof_dict)



sunroof_df
