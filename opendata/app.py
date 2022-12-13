import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
   "http://data.seoul.go.kr/dataList/10754/S/2/datasetView.do"
)

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df = pd.read_csv('./opendata/data.csv', encoding='cp949')
st.write(df)
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()
titanic.tail()
titanic.info()
titanic.describe()
sns.histplot(data=titanic, x='age')
sns.histplot(data=titanic, x='age', bins=10)
sns.kdeplot(data=titanic, x='age')