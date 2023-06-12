# %%
import geopandas as gpd
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import normalize
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import tree
from matplotlib import pyplot as plt

# %%
# reading the data file
df = gpd.read_file('data_merged\\full_join.geojson')

# %%
# adding aditional columns needed for the modeling
df = df.assign(
    density = df['inhabitants'] / df['area_sqkm'],
    crime_and_nuisance = df['Total felonies'] + df['Total nuisance registrations']
)

# %%
# chosing the predictiors and saving it to a dataframe
df = pd.DataFrame(df[['sport_building_count',
                    'distance_from_centre_km',
                    'green_score',
                    'livability_score',
                    'jobs_count',
                    'proximity_score',
                    'density',
                    'crime_and_nuisance',
                    'price_2022']])

# %%
# replacing 28 missing values in 'crime_and_nuisance' column with the average
df['crime_and_nuisance'] = df['crime_and_nuisance'].fillna(value=df['crime_and_nuisance'].mean())

# %%
# getting rid of 3 rows with missing values
df = df.dropna()

# %%
# splitting the data into input and output
X = df.drop('price_2022', axis=1)
y = df[['price_2022']]

# %%
# saving the column names
colls = X.columns

# %%
# normalizing the input values
X = normalize(X)

# %%
# splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# %%
# preparing hyperparameters for a grid search
params = {
    'n_estimators': [x for x in range(1, 20)],
    'max_depth': [x for x in range(1, 20)]
}

# %%
# instantiating a random forest model
model = RandomForestRegressor(random_state=42, criterion='squared_error')

# %%
# instantiating the grid search and passing the hyperparameters to tune
searcher = GridSearchCV(model, param_grid=params, scoring=r2_score, n_jobs=4, verbose=2, refit=True)

# %%
# hyperparameter tuning using grid search object
searcher.fit(X_train, y_train)

# %%
# checking the best hyperparameters
model = searcher.best_estimator_

# %%
searcher.best_params_

# %%
y_pred = model.predict(X_test)

# %%
# evaluating the model with r2 score and mean square error
r2_score(y_test, y_pred)

# %%
mean_squared_error(y_test, y_pred)

# %%
# displaying the model (only one tree worked the best)
plt.figure(figsize=(10,10))
_ = tree.plot_tree(model.estimators_[0], feature_names=colls, filled=False)


