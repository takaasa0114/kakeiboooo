dectionary={"1月":"B","2月":"C","3月":"D","4月":"E","5月":"F","6月":"G","7月":"H","8月":"I","9月":"J","10月":"K","11月":"L","12月":"M"}

import pandas as pd
import streamlit as st

st.title('家計簿アプリ')
st.subheader("収支表")
month=st.selectbox("月を選択してください",["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"])
yosan=st.number_input('予算を入力してください',step=1)
work=st.number_input("アルバイト代",step=1)
siokuri=st.number_input("仕送り",step=1)
food=st.number_input("食費",step=1)
water=st.number_input("水道代",step=1)
elandgas=st.number_input('ガス、電気代',step=1)
clothe=st.number_input('衣服代',step=1)
medical=st.number_input('医療費',step=1)
days=st.number_input('日用品',step=1)
trance=st.number_input('運賃',step=1)
others=st.number_input('雑費',step=1)
syuunyuu=work+siokuri
sisyutu=food+water+elandgas+clothe+medical+days+trance+others
total=syuunyuu-sisyutu

baito_square=0
siokuri_square=0
syuunyuu_square=0
water_square=0
elandgas_square=0
food_square=0
clothe_square=0
medical_square=0
days_square=0
trance_square=0
others_square=0
sisyutu_square=0
total_square=0
if st.button('確定する'):
    st.success("セーブしました")
#Excelに書き込み
    baito_square+=work
    siokuri_square+=siokuri
    syuunyuu_square+=syuunyuu
    water_square+=water
    elandgas_square+=elandgas
    food_square+=food
    clothe_square+=clothe
    medical_square+=medical
    days_square+=days
    trance_square+=trance
    others_square+=others
    sisyutu_square+=sisyutu
    total_square+=syuunyuu-sisyutu
   
if st.button("リセット"):
    total=0
    syuunyuu=0
    sisyutu=0
    work=0
    food=0
    water=0
    siokuri=0
    elandgas=0
    clothe=0
    medical=0
    days=0
    trance=0
    others=0
col1,col2,col3,col4=st.columns(4)
col1.metric(label="収入",value=syuunyuu)
col2.metric(label="支出",value=sisyutu)
col3.metric(label="収支合計",value=total)
col4.metric(label="残り予算",value=yosan-sisyutu,delta="")
st.subheader('月別支出表')
data=[int(water_square),int(elandgas_square), int(food_square), int(clothe_square),int(medical_square),int(days_square), int(trance_square) ,int(others_square)]
idx=["水道代","ガス、電気代","食費","衣服代","医療費","日用品","運賃","雑費"]
col=["2022"]
df=pd.DataFrame({"水道代":[int(water_square)],
                 "ガス、電気代":[int(elandgas_square)],
                 "食費":[int(food_square)],
                 "衣服代":[int(clothe_square)],
                 "医療費":[int(medical_square)],
                 "日用品":[int(days_square)],
                 "運賃":[int(trance_square)],
                 "雑費":[int(others_square)]})
df1 = pd.DataFrame(data=data, index=idx, columns=col)
st.line_chart(df1)

st.table(df)
if st.button('表示しない'):
    st.empty()