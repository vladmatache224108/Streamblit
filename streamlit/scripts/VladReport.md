# Report and Visualizations on green index and other factors that influence housing prices
- Vlad


---

## Introduction.
I have been tasked with gathering, cleaning and processing the following data:
- Green index;
- Livability index;
- House prices;
- Heat Stress scorre;
  
The gathering of the data has been done from openly available sources(ex: https://data.breda.nl/; https://allcharts.info/the-netherlands/borough-breda-centrum/#info_house-value).

My responsability has been to perform the EDA process on the gathered data and discover insights related to housing prices.

## Correlations.
For the following correlations I have used Spearman's correlation coefficient in order to better analyze non linear data such as the one gathered. And so I have created using code correlations.csv which contains the correlations between every feature gathered.

## Findings

The first interesting finding is the correlation between Green Score and House price.

![Imgur](https://i.imgur.com/vHs9zaj.png)

### Spearman's Corr for price and green_score  = 0.6917293233082705

Due to the strong positive relationship between the two we need to ask ourselves the following question: Is a neighbourhood being greener make the houses more expensive or is it a side effect of another feature?

In order to answer this question we need to take a deeper look at the available data.

So my first instinct is to assume that as the city develops there is less and less room for green spaces the closer you are to the centrum which is also the commerical hot spot of the city.

![Imgur](https://i.imgur.com/IZAc3nP.png)

### Spearman's Corr for  green_score  and  distance_from_centre_km  = 0.4586466165413533

The moderate positive correlation explains the fact that my theory is not entirely true and that other factors also influence green score. The reason for the correlation being moderate and not strong is that with an increase to foot traffic and car traffic around the centrum and/or central neighborhoods the municipality creates more green spaces to offset pollution and other negative factors.

The second theory regarding green index and house prices being correlated comes from analyzing the relationship between surface area of a neighbourhood and the price.

![Imgur](https://i.imgur.com/vHs9zaj.png)

### Spearman's Corr for price and area_sqkm  = 0.42136956999911945

The close to moderate correlation tells me that the second theory has some legs to stand on and so I decided to analyze the relation between surface area and green score.
![Imgur](https://i.imgur.com/aIM10Bz.png)

### Spearman's Corr for  green_score  and  area_sqkm  = 0.7233082706766917

## Conclusion.

This is very interesting to me as a strong positive relationship between surface area and green index and taking into account the effect that these two factors along side the distance from the centrum have on house price I can confidently say that the neighborhoods that are further away from the tightly packed streets of the centrum have more room for ammenities such as green spaces and that people are more inclined to build and purchase higher value homes due to the increased quality of life that this offers.

By looking at the graphs it is clear to see that the neighbourhood that is present in the top when sorting values by these factors is Hagebeemd which also happens to be amongst the highest valued neighborhoods for house prices.

From this analysis we can conclude that green score is indeed a good proxy for house prices as one clearly and strongly iinfluences the other.

