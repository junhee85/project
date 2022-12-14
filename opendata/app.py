import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips = sns.load_dataset('tips')
# st.write(tips)
st.write(
    '''
    #tips 데이터셋을 이용한 데이터 시각화
    ##tips 데이터
    '''
)
st.write(tips)
st.write(
    '''
    ### 총액의 빈도수
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.histplot(data=tips, x='total_bill')
st.pyplot(fig)
st.write(
    '''
    ### 식사 인원수
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.histplot(data=tips, x='size')
st.pyplot(fig)
st.write(
    '''
    ### 인원수와 팁의 상관관계
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.kdeplot(data=tips, x = 'total_bill')
sns.rugplot(data=tips, x = 'tip')
st.pyplot(fig)
st.write(
    '''
    ### 박스
    '''
)
fig = plt.figure(figsize=(8, 4))
sns.boxplot(x='size', y='total_bill', data=tips)
st.pyplot(fig)
st.write(
    '''
    ### 인원수에 따른 그래프
    '''
)
fig = sns.pairplot(tips, hue="size")
st.pyplot(fig)