# import requests
# import pandas as pd

# def get_stock_price(code, startdate, enddate):
#   url = "https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={}&requestType=1&startTime={}&endTime={}&timeframe=day".format(code,startdate, enddate)

#   #symbol = 종목코드

#   res = requests.get(url)
#   li = eval(res.text.replace("\n","").replace("\t",""))

#   return pd.DataFrame(columns=li[0], data=li[1:])


# get_stock_price('005930','20240801','20240826')
# #각각 type별로 변환해주면 나중에 좋음. 날짜는 날짜, 숫자, 실수형 등

# import streamlit as st
# import datetime as dt

# st.title('주식 차트')

# sd = st.date_input("조회 시작일을 선택해주세요.", dt.datetime(2024,1,1))


##############정답 코드######################

#뉴스와 블로그 수집... 시간 남으면 하기

#정답 코드는 stock_chart.py

import streamlit as st 
import datetime as dt
import requests
import pandas as pd

# with st.sidebar:
#     st.page_link('page1.py', label='뉴스수집기', icon='🔥')

st.set_page_config(page_title='주식 차트 페이지', page_icon=':shark:') #tab title
st.title('주식 차트')

def get_stockprice(code, sdt, edt) :
  URL = "https://m.stock.naver.com/front-api/external/chart/domestic/info?symbol={0}&requestType=1&startTime={1}&endTime={2}&timeframe=day".format(code, sdt, edt)
  print(URL)
  res = requests.get(URL)
  li = eval(res.text.replace("\n","").replace("\t",""))
  return pd.DataFrame(columns=li[0],data=li[1:])



sd = st.date_input("조회 시작일을 선택해 주세요", dt.datetime(2024, 1, 1))
ed = st.date_input("조회 종료일을 선택해 주세요", dt.datetime(2024, 1, 1))
code = st.text_input('종목코드를 입력해주세요.')

if sd and ed and code :
    df = get_stockprice(code, sd.strftime('%Y%m%d'), ed.strftime('%Y%m%d')) #string from data time
    st.dataframe(df)
    
    st.line_chart(df['종가'])
    st.bar_chart(df['거래량'])