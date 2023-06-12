import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

add_logo("streamlit/logo.png", height=180)




title = st.title('Neighbourhood Index')
caption = st.caption('-Team GeoNinjas')



st.subheader('Project Vision')


st.markdown("# Our four main goals:")
st.markdown("1.	Breda is a diverse city with unique neighborhoods, each with its own charm and character. However, there is always room for improvement. By conducting a thorough analysis of the different neighborhoods, we can identify areas that require attention and propose recommendations to enhance them. This could involve initiatives such as improving green-index by creating more parks in that specific area, enhancing public safety for example by sending more police officers in that neighboothood, or creating public safe bike zones on those areas where the highest number of thefts are detected.")
st.markdown("2.	Identifying suitable neighborhoods based on specific requirements. Whether it's families looking for safe and child-friendly areas or young professionals seeking dynamic neighborhoods, we can utilize data and analytics to match residents with the neighborhoods that best meet their needs. This can involve evaluating factors such as access to amenities, the level of green index and the overall quality of life in each neighborhood. By providing tailored recommendations, we can help individuals and families find their ideal living environment within our city. (machine learning model embedded in a dashboard...)")
st.markdown("3.	The influence of various features on house prices. The real estate market is a significant contributor to the economy of Breda, and understanding the factors that influence house prices can be beneficial for both buyers and sellers. By analyzing data on factors such as location, proximity to key amenities, green spaces, crime rates, we can provide insights that inform decision-making in the real estate market.")
st.markdown("4.	While Breda is generally a safe place to live, we must strive for continuous improvement in reducing crime across various types. By utilizing data analysis and understanding the patterns and underlying causes of different crimes, we can develop targeted strategies to address them effectively. This can involve increasing the number of police officers or improving street lighting.")
