# ADD goal when we have one
![this is an image](images/deda.png)
## GeoNinjas
### Panna Pfandler(225928), Wojciech Stachowiak(222679), Bogdan Matache(225108), Thijn van Oort(212396)
#### 23/06/2023 Breda University of Applied Sciences
    Introduction

## Overview

The project aims to utilize comprehensive data analysis to create a better living environment in Breda. By leveraging datasets provided by the municipality like green-index and livability score, publicly available police data on crimes and nuisances, as well as data on amenities and housing prices, our project focuses on four main goals. Firstly, we aim to provide recommendations for improving different neighborhoods within Breda by identifying areas that require attention and proposing targeted initiatives. Furthermore, we seek to assist individuals and families in finding suitable neighborhoods based on their specific requirements and preferences. Thirdly, we aim to reduce crime rates by analyzing crime data and developing effective strategies tailored to different types of crimes. Lastly, we aim to understand the factors that influence house prices in order to provide insights that inform decision-making in the real estate market. Through these goals, our project aims to enhance the overall livability, safety, and prosperity of Breda, making it an even better place to live, work, and thrive.


## The project impact
The project can have a significant impact on various stakeholders within the city of Breda. Here are some of the key groups that might be affected by the project:

- Residents: The primary beneficiaries of the project are the residents of Breda. The project's recommendations for improving neighborhoods, enhancing safety, and providing personalized recommendations for suitable living environments can directly impact the quality of life and well-being of residents.
- Local Authorities and Policymakers: The project's findings and recommendations can influence the decisions and actions of local authorities and policymakers. The insights gained from data analysis can inform urban planning, resource allocation, and policy development, enabling more effective and targeted interventions to enhance livability and safety in the city.
- Real Estate Industry Professionals: Professionals working in the real estate industry, such as real estate agents, developers, and investors, can be affected by the project. The analysis of factors influencing house prices and the availability of comprehensive neighborhood data can provide valuable insights for their decision-making processes.
- Community Organizations: Community organizations involved in neighborhood development, social initiatives, or advocacy work can be impacted by the project. The project's recommendations for neighborhood improvements and safety measures can align with the goals and objectives of these organizations, fostering collaboration and collective efforts towards enhancing the community.
- Visitors and Tourists: The project's focus on enhancing livability and safety can also have an indirect impact on visitors and tourists to Breda. The improvement of neighborhoods, public safety measures, and the overall attractiveness of the city can contribute to a positive visitor experience, potentially boosting tourism and economic growth.


## Benefits of the project

Some of the key benefits include:

- Improved Livability: By providing recommendations to enhance different neighborhoods, the project aims to improve the quality of life for residents. This can involve initiatives such as creating more parks, enhancing safety measures, and addressing specific neighborhood needs. Ultimately, the project aims to create more livable and attractive neighborhoods for residents to enjoy.
- Enhanced Safety: The project's analysis of crime rates and nuisances aims to develop targeted strategies for reducing different types of crimes. By understanding patterns and underlying causes, effective measures can be implemented to improve public safety. This contributes to creating a safer environment for residents and visitors alike.
- Informed Decision-Making: The project's analysis of factors influencing house prices and amenities can provide valuable insights to buyers, sellers, and real estate professionals. Understanding these factors allows for more informed decision-making in the real estate market, promoting transparency and efficiency. This benefits individuals and stakeholders involved in buying, selling, and investing in properties in Breda.
- Tailored Recommendations: Through the project's analysis, residents can benefit from personalized recommendations for finding suitable neighborhoods based on their specific requirements and preferences. This helps individuals and families make informed choices about where to live, considering factors such as safety, amenities, and overall quality of life.
- Collaboration and Stakeholder Engagement: The project encourages collaboration between local authorities, community organizations, and stakeholders involved in urban planning and development. By engaging different perspectives and involving key stakeholders, the project aims to create a sense of ownership and foster a collaborative approach towards enhancing Breda. This ensures that the project's recommendations align with the needs and aspirations of the community.
- Data-Driven Decision-Making: The project demonstrates the power of data analytics in driving decision-making processes. By utilizing comprehensive datasets, the project provides evidence-based insights, enabling policymakers and stakeholders to make informed decisions and allocate resources effectively.

## Concerns about the project:

While the project aims to bring about positive changes, there are several potential problems or concerns that might arise. It is important to address these proactively to ensure the project's success and mitigate any negative consequences. Some potential problems and concerns include:

- Data Privacy and Security: Working with various datasets, including sensitive information such as crime data and personal information, raises concerns about data privacy and security. Ensuring robust data protection measures, anonymization techniques, and compliance with relevant data privacy regulations are essential to maintain the confidentiality and integrity of the data.
- Bias and Discrimination: Data analysis and decision-making processes must be carefully monitored to prevent biases from influencing the results or recommendations. Unintentional bias in the data or algorithms used for analysis could result in discriminatory outcomes or reinforce existing inequalities within neighborhoods. Regular audits and checks for bias, along with transparency in the methodology, can help mitigate these concerns.
- Ethical Use of Data: The project's use of data must adhere to ethical guidelines and principles. This includes obtaining appropriate permissions for data usage, ensuring data accuracy and integrity, and being transparent about the project's intentions and potential outcomes. Safeguarding against potential misuse or unintended consequences is critical to maintaining public trust.
- Missing Data: One of the challenges that may arise during the project is the presence of missing data within the datasets utilized. Missing data can potentially impact the accuracy and reliability of the analysis and subsequent recommendations. It is crucial to address this issue effectively to ensure the integrity of the project's findings.

        Important ethical aspects

# Algorithms 


# Sources 
## Datasets
- utils.geojson(Merged Dataset):
  - population.csv [Source](https://allcharts.info/the-netherlands/municipality-breda/)
  - lighting.geojson [Source](https://data.breda.nl/datasets/Breda::openbare-verlichting/explore?location=51.560642%2C4.774393%2C12.74)
  - work_locations.geojson [Source](https://data.breda.nl/datasets/Breda::werklocaties/explore?location=51.557428%2C4.771700%2C12.80)
  - sport_buildings.geojson [Source](https://data.breda.nl/datasets/Breda::sportaccomodaties/explore?location=51.574031%2C4.776141%2C13.16)
  - Buurten.geojson [Source](https://data.breda.nl/datasets/Breda::buurten/explore?location=51.564294%2C4.764872%2C12.31)
- jobs_by_buurt.csv(Merged:'population.csv' and 'Buurten.geojson')
- neighbourhood_index.csv(Merged)  
  - livability_score.csv(Provided by municipality of Breda)
  - green_score.csv(Provided by municipality of Breda)
- nuisance.csv [Source](https://data.politie.nl/#/Politie/nl/dataset/47024NED/table?ts=1685526475975)
- crime_by_type.csv [Source](https://data.politie.nl/#/Politie/nl/dataset/47018NED/table?ts=1685526622753)
- drugchords.csv [Source](https://www.google.com/maps?hl=en&q=alchol+store)

## Quality of Data
The datasets used in this project are sourced from reliable and official websites such as the municipality of Breda and the Dutch police. The datasets for lighting, work locations, sport buildings, and neighborhoods are obtained from the municipality of Breda's website, which is a trustworthy source. As they are official sources, the data's accuracy and reliability can be assumed. However, we still need to check for possible gaps in the data and ensure that it's consistent.(lighting.geojson, work_locations.geojson, sport_buildings.geojson, Buurten.geojson)

The dataset for the neighborhood index is extracted from the SQL server of the municipality of Breda. This database is a reliable reference for this type of data, and its accuracy and reliability can be expected. (livability_score.csv, green_score.csv)

As for the datasets for nuisance and crime by type, they are from the Dutch police website, which is considered a reputable source of crime data. The quality of the data can be trusted to a certain extent.(nuisance.csv and crime_by_type.csv)

## Visualization

We will deliver a comprehensive set of deliverables that include interactive dashboards (machine learning model embedded) and a detailed report. These deliverables will empower stakeholders and decision-makers with the necessary information to make informed choices and drive positive change within the city.

- Interactive Dashboards: An interactive dashboard will be developed, incorporating the visualizations and providing stakeholders with a dynamic and user-friendly interface to explore the data. The dashboard will allow users to interact with the data, customize views, and access personalized recommendations. By embedding a machine learning model, the dashboard will offer tailored suggestions based on the analyzed data, further enhancing its functionality and usefulness for decision-making.
- Comprehensive Report: Alongside the visual deliverables, a comprehensive report will be provided. The report will offer an in-depth analysis of the data, methodologies utilized, key findings, and actionable recommendations. It will serve as a valuable resource for stakeholders, providing a detailed understanding of the insights derived from the data analysis. The report will also outline the project's objectives, methodology, data sources, and limitations, ensuring transparency and accountability.

## Access

The data utilized in this project encompasses a combination of sources, including data provided by the municipality of Breda and open resources. The accessibility of the data is subject to specific conditions and agreements set forth by the respective sources.

Regarding the data provided by the municipality of Breda, access is granted to the project team based on collaboration agreements and data sharing protocols established between the project stakeholders and the municipality. The team ensures that the data is handled in accordance with the agreed-upon terms and conditions, maintaining its confidentiality and using it solely for the intended purposes of the project.

In the case of data obtained from open resources, such as publicly available datasets and online platforms, access is granted based on the terms of use and licenses provided by the data sources. The project team adheres to the terms and conditions specified by these sources, respecting any restrictions or guidelines for data usage and attribution.


Access monitoring and control for the data used in this project are primarily the responsibility of the respective websites and data sources from which the information was obtained. These websites employ their own mechanisms and protocols to regulate access to the data they provide. As the project team, we rely on the access control measures implemented by these websites to ensure the integrity and security of the data.

## Responsibility
## Communication
## Transparency
## Privacy
## Bias

    Ethical aspects that are not applicable to your project's context
## Anonymization
The collected data for this project has been sourced from open resources, as well as data provided by the municipality of Breda. It is important to note that all data, including the municipality-provided data, has been received in an anonymous format. The data has undergone thorough anonymization processes prior to its integration into the project. Anonymization is a crucial step in ensuring the protection of individual privacy by removing or obfuscating personally identifiable information. This approach aligns with best practices in data handling and complies with applicable legal and ethical requirements. By utilizing anonymized data from both open resources and the municipality, we can maintain the privacy and confidentiality of individuals while still extracting valuable insights and conducting meaningful analyses. The anonymization of the data helps to mitigate the risk of re-identification and unauthorized access, ensuring that the project operates in a responsible and ethical manner.
## Sharing, reusing and repurposing

