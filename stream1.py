import streamlit as st
import pandas as pd
import numpy as np
st.title('My first App')

st.write('データフレーム')
df_data = pd.DataFrame({
    '1st column': [1, 2, 3, 4],
    '2nd column': [4, 5, 6, 7]})
st.write(df_data)
"""
#　my first App
##　こんな感じ
"""

if st.checkbox('show DataFrame'):
    chart_df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c']
                            )
    st.line_chart(chart_df)
