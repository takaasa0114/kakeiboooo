dectionary={"1月":"B","2月":"C","3月":"D","4月":"E","5月":"F","6月":"G","7月":"H","8月":"I","9月":"J","10月":"K","11月":"L","12月":"M"}
import numpy as np
import pandas as pd
import streamlit as st
import openpyxl as op
excel=op.load_workbook(R"C:\Users\takaa\OneDrive\デスクトップ\Python系フォルダ\Book2.xlsx")
kakeibo=excel['Sheet1']
df=pd.read_excel(R"C:\Users\takaa\OneDrive\デスクトップ\Python系フォルダ\Book2.xlsx")
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
columns=dectionary[month]
a=columns+"3"
b=columns+"4"
c=columns+"5"
d=columns+"6"
e=columns+"7"
f=columns+"8"
g=columns+"9"
h=columns+"10"
i=columns+"11"
j=columns+"12"
k=columns+"13"
l=columns+"14"
m=columns+"15"
baito_square=kakeibo[a]
siokuri_square=kakeibo[b]
syuunyuu_square=kakeibo[c]
water_square=kakeibo[d]
elandgas_square=kakeibo[e]
food_square=kakeibo[f]
clothe_square=kakeibo[g]
medical_square=kakeibo[h]
days_square=kakeibo[i]
trance_square=kakeibo[j]
others_square=kakeibo[k]
sisyutu_square=kakeibo[l]
total_square=kakeibo[m]
if st.button('確定する'):
    st.success("セーブしました")
#Excelに書き込み
    baito_square.value+=work
    siokuri_square.value+=siokuri
    syuunyuu_square.value+=syuunyuu
    water_square.value+=water
    elandgas_square.value+=elandgas
    food_square.value+=food
    clothe_square.value+=clothe
    medical_square.value+=medical
    days_square.value+=days
    trance_square.value+=trance
    others_square.value+=others
    sisyutu_square.value+=sisyutu
    total_square.value+=syuunyuu-sisyutu
    excel.save(R"C:\Users\takaa\OneDrive\デスクトップ\Python系フォルダ\Book2.xlsx")
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
data=[int(water_square.value),int(elandgas_square.value), int(food_square.value), int(clothe_square.value),int(medical_square.value),int(days_square.value), int(trance_square.value) ,int(others_square.value)]
idx=["水道代","ガス、電気代","食費","衣服代","医療費","日用品","運賃","雑費"]
col=["2022"]
df1 = pd.DataFrame(data=data, index=idx, columns=col)
st.line_chart(df1)
if st.button('表示する'):
    st.table(df)
    if st.button('表示しない'):
        st.empty()