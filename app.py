import streamlit as st
import pandas as pd

# タイトルの設定
st.header('レッスン4: データ入力と表示')

# テキスト入力
name = st.text_input('あなたの名前を入力してください')
if name:
    st.write(f'こんにちは、{name}さん！')

# 数値入力
age = st.number_input('あなたの年齢を入力してください', min_value=0, max_value=120, value=20)
st.write(f'あなたは{age}歳です。')

# 日付入力
date = st.date_input('日付を選択してください')
st.write(f'選択された日付: {date}')

# サンプルデータの作成
data = {
    '名前': ['太郎', '花子', '一郎'],
    '年齢': [25, 30, 35],
    '都市': ['東京', '大阪', '福岡']
}
df = pd.DataFrame(data)

# データフレームの表示
st.subheader('データフレームの表示')
st.dataframe(df)

# 表の表示
st.subheader('表の表示')
st.table(df)
