import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from matplotlib import pyplot as plt

st.title('Green Index and Livability Index by Neighbourhood')

DATA_URL = 'data/green_live.csv'

#@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)




grouped_data = data.groupby('year')['green_score','livability_score'].mean()
grouped_data = grouped_data.reset_index()

years = grouped_data['year'].astype('int').values.round(decimals = 2).tolist()
green_score = grouped_data['green_score'].values.round(decimals = 2).tolist()
live_score = grouped_data['livability_score'].values.tolist()

grouped_data['year'] = years
grouped_data['green_score'] = green_score
grouped_data['livability_score'] = live_score

a = st.text(grouped_data)

st.subheader('Average green_score by year')

st.line_chart(grouped_data, x = 'year', y = 'green_score')

st.subheader('Average livability_score by year')


fig, ax = plt.subplots()
ax.plot(grouped_data['year'],grouped_data['livability_score'])
ax.plot(grouped_data['year'],grouped_data['green_score'])
ax.set_yscale('log')
st.pyplot(fig)
#st.map(data)