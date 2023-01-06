import streamlit as st
import pandas as pd 
import plotly.express as px

st.title("Streamlit Demo")
st.subheader("by 久保幹雄")

# '''
# ### 文字列はマークダウン言語

# 通常のテキスト
# '''

df = px.data.iris()
# df

# x = 10
# 'x =', x  

st.write("何でも書ける")

st.markdown("## マークダウンで書く $x^2$")

st.write(df.head())

# st.table(df.head())

st.write(px.scatter(df,x="sepal_length",y="sepal_width",color="species"))

if st.button('Say hello'):
    st.write('こんにちわ')
else:
    st.write('Goodbye')

# agree = st.checkbox('チェックしてください')
# if agree:
#     st.write('Great!')

# fruit = st.radio(label="好きなフルーツは？",options =["バナナ","りんご","いちご"],index=1)
# st.write(fruit)

# option = st.selectbox('今日はなにする?', ('なわとび', '野球', 'ゲーム') )
# st.write('よし ', option, " をしよう！")

# def f(i):
#     play = ('なわとび', '野球', 'ゲーム')
#     return play[i]

# option = st.selectbox('今日はなにする?', (0,1,2), format_func= f )
# st.write('よし ', option, " をしよう！")

# options = st.multiselect('何色が好き？',options= ['Green', 'Yellow', 'Red', 'Blue'], default=['Yellow', 'Red'])
# st.write('You selected:', options)

# age = st.slider('何歳?', min_value=0, max_value=130, value=25)
# st.write(age)
from datetime import datetime, date, time
# interval = st.slider("計画期間は?", value=(datetime(2019, 1, 1, 9, 30),
# datetime(2020, 1, 1, 9, 30)),format="MM/DD/YY - hh:mm")

# color = st.select_slider('色を選んでね',options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

# title = st.text_input('お名前は？', value='ななしのごんべえ')

# number = st.number_input('数字を入れてね', min_value=1.0, max_value=10.0, value=5.0, step=0.1)

# d = st.date_input("誕生日は？",date(2019, 7, 6))

# alarm = st.time_input('アラームセット', time(8, 45))

# uploaded_file = st.file_uploader("ファイル選択")

# text_contents = '''This is some text'''
# st.download_button('ダウンロード', text_contents)

# add_selectbox = st.sidebar.selectbox("連絡方法は?", ("Email", "Home phone", "Mobile phone"))
# col1, col2 = st.columns([1,2])
# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg",use_column_width=True)
# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg",use_column_width=True)

# with st.form("入力フォーム"):
#     name = st.text_input("名前")
#     height = st.number_input("身長")
#     male = st.checkbox("男性?")
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write(name, height, male)

# import time
# if st.button("Progress Test"):
#     my_bar = st.progress(0)
#     for percent_complete in range(100):
#         time.sleep(0.051)
#         my_bar.progress(percent_complete + 1)

#     with st.spinner('ちょっとまってね'):
#         time.sleep(3)
#         st.balloons()

# placeholder = st.empty()
# placeholder.text("Hello")
# if st.button("消す！"):
#     placeholder.empty()


# if 'counter' not in st.session_state:
#     st.session_state['counter'] = 0

# def add_one():
#     st.session_state['counter'] +=1

# st.button("押してね", on_click=add_one)
# st.write(st.session_state['counter'])

# age = st.number_input(label="年齢は？", min_value = 0, max_value=200,
#               value = 20, step =1, format="%d", key="age_input")
# st.write(st.session_state)
# st.write(st.session_state.age_input, st.session_state["age_input"])


import time
# @st.cache
# def f(input):
#     time.sleep(3)
#     return input*10
# st.write(f(10))  #3秒かかる
# st.write(f(100)) #これも3秒かかる
# st.write(f(10))  #キャッシュされているので一瞬で終わる

# import random
# @st.cache(allow_output_mutation=True) # 返値が変わる場合は，この引数をTrueにする
# def g(input):
#     time.sleep(3)
#     return input*random.random()

# st.write(g(10))  #3秒かかる
# st.write(g(100)) #これも3秒かかる
# st.write(g(10))  #キャッシュされているので一瞬で終わる（ただし最初と同じ乱数を返す）


#データフレームのハッシュ値をidとする．
# @st.cache(hash_funcs={pd.DataFrame: id})
# def h(data):
#     time.sleep(3)
#     return data.values

# df = px.data.iris()

# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report

# st_profile_report(ProfileReport(df))

# import hiplot as hip
# df = px.data.iris()

# hip.Experiment.from_iterable(df.to_dict("records")).display_st()
