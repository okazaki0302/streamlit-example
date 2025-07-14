import streamlit as st
import pandas as pd  # データ分析ライブラリ pandas
import numpy as np  # 数値計算ライブラリ

# タイトル表示
st.title('タクシー乗り場 in NewYork')

DATE_COLUMN = 'date/time'   #データの日時形式

# TODO: 以下の2行はチャットに貼っています。
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')   

# データを読み込む関数
# @st.cache と書くと、一度データを読み込んだら手元に保持し続けることで、再読み込みを高速化
@st.cache 
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)   # CSVデータをネットから読み込む。
    # 引数として受け取った nrowsの数だけ読み込む。

    # 列名を全て小文字にする
    lowercase = lambda x: str(x).lower()    # lambda の書き方は、ChatGPTに聞いてください。
    data.rename(lowercase, axis='columns', inplace=True)

    # 日時の列を datetime列に変換する
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])

    return data

data = load_data(100) # load_data関数を使って, 1万行データを読み込む

st.write(data)  # 表形式でデータを出力