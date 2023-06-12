import pandas as pd
import geopandas as gpd
import numpy as np
import os


def plot_below(dataframe,column1, column2):
        data = 'C:/Users/bogda/Documents/GitHub/2022-23d-1fcmgt-reg-ai-01-group-team9/Code & Data/data_merged/full_join.geojson'

        data = gpd.read_file(data)


        data = data.drop(['geometry','price_2015', 'price_2016', 'price_2017',
                'price_2018', 'price_2019', 'price_2020', 'price_2021',
                'Encroachment on public order', 'Fraud (other)', 'Horizontal Fraud',
                'Human trafficking', 'Nature and landscape', 'Quality of life (other)',
                'Road (other)', 'Spatial planning', 'Special Laws',
                'Transport of hazardous substances', 'Under the influence (water)',
                'Air (other)', 'Animals', 'Arms Trade', 'Building materials',
                'Cybercrime', 'Discrimination', 'Domestic Violation',
                'Fire/Explosion','Fireworks', 'Food safety', 'Home theft/burglary',
                'Immigration care','Most', 'Motor Vehicle Theft', 'Murder, Manslaughter',
                'Neighbor rumor (relationship problems)', 'Open violence (person)','Other property crimes',
                'People smuggling', 'Pesticides','Pickpocketing', 'Robbery', 'Shoplifting', 'Soil',
                'Structure of the Environmental Management Act','Theft from/from motor vehicles',
                'Theft/burglary of companies, etc.','Thefts (water)', 'Threat',  'Under the influence (air)',
                'Under the influence (road)','Vertical Fraud', 'Waste', 'Water',
                'Youth nuisance report','Nuisance drifters', 'Noise nuisance catering',
                'Noise nuisance event', 'Other noise nuisance', 'Childcare',
                'Education', 'Health and well-being', 'Hospitality', 'Retail',
                ], axis = 1)

        data = data.replace(np.nan, 0)
        data = dataframe[['neighborhood', column1, column2]]
        st.line_chart(data)
        st.text("Spearman's Corr for price and",column1, ' =',data[column1].corr(data[column2], method='spearman'))