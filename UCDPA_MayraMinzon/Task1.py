import pandas as pd
import missingno as msno
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
sns.set()

    #Function to remove outliers
def remove_outliers(df, x):
    # Set Limits
    q25, q75 = np.percentile(df[x], 25), np.percentile(df[x], 75)
    iqr = q75 - q25
    cut_off = iqr * 1.5
    lower, upper = 1 ,  (q75 + cut_off)
    df = df[(df[x] < upper) & (df[x] > lower)]
    print('Outliers of "{}" are removed\n'.format(x))
    return df

    #Function to clean dataset of nan, Inf and missing cells for skewed datasets
def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


    #Import .csv file using Pandas DataFrame
dt = pd.read_csv(r"houses_data.csv")
df = pd.DataFrame(data=dt)

    #Merge dataframes
print(pd.merge(
    left = pd.DataFrame(data = pd.read_csv(r"houses_data_index.csv")),
    right = pd.DataFrame(data = pd.read_csv(r"houses_data.csv")),
    how = "inner",
    on = None,
    left_on = 'Index',
    right_on = 'Index',
    left_index = False,
    right_index = False,
    sort = True,
    suffixes=("_x", "_y"),
    copy=True,
    indicator = False,
    validate = None,
)
)

    #Filter data by city using Regex
regex = 'Seattle.*'
df_Seattle = df[df.city.str.match(regex)]

    #Change Price column from scientific notation to decimal
pd.options.display.float_format = '{:.6f}'.format

    #Sum houses sqrft
overall_house_size = df_Seattle['sqft_living'] + df_Seattle['sqft_above'] + df_Seattle['sqft_basement']
print(overall_house_size)

yr_built_sorted = df_Seattle.sort_values(by = 'yr_built')
msno.matrix(yr_built_sorted)

    #isolate and replace blank values in column price with average
print(df_Seattle.isna().sum())
msno.matrix(df_Seattle)

missing_price = df_Seattle[df_Seattle['price'].isna()]
price = df_Seattle[~df_Seattle['price'].isna()]

print(missing_price.describe())
print(price.describe())

price_average = df_Seattle['price'].mean()
df_Seattle_all_prices = df_Seattle.fillna({'price':price_average})
print(df_Seattle_all_prices.isna().sum())

    #Using iterators
for row in df_Seattle_all_prices.itertuples():
    print("df[" + str(row.Index) + "] - ['Price']=" + str(row.price) + " - ['Year Built']=" + str(row.yr_built) + " - ['Sqft Living']=" + str(row.sqft_living))

    #Call the function remove_outliers
houses_df = remove_outliers(df_Seattle_all_prices, 'price')
print(houses_df.head(5))

    #Data Counts
print(houses_df['price'].value_counts())
print(houses_df['bedrooms'].value_counts())
print(houses_df['statezip'].value_counts())
print(sns.heatmap(houses_df[["price", "bedrooms", "statezip"]].corr(), annot=True))

fig, axes = plt.subplots(2, 2, figsize=(18, 10))
sns.histplot(ax=axes[0, 0], x= 'price', data= houses_df);
sns.histplot(ax=axes[0, 1], x= 'bedrooms', data= houses_df);
sns.histplot(ax=axes[1, 0], x= 'statezip', data= houses_df);

print(houses_df['yr_built'].hist())

    #NumPy Correlation graphs
for i in houses_df.columns:
    if (houses_df[i].dtype ==  np.int64 ) | (houses_df[i].dtype ==  np.int32):
        sns.lmplot(x = i, y ='price', data = houses_df)
        plt.show()

    #Supervised learning
    #First it needs to convert city Data to Categorica; Data to get into model
df = houses_df
df = pd.get_dummies(df, drop_first=True)
clean_dataset(df)
print(df.head().T)

#arrange feature and label
X = df.drop('price', axis = 1).values
y = df.price.values

#Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

#Scale
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#Mean and standard deviation of X_train
print("Mean and Std Deviation", X_train.mean(), X_train.std())

    #Linear Regression Model and accuracy
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print("Linear Regression Training acc >> ", lin_reg.score(X_train, y_train))
print("Linear Regression Testing acc >>  ", lin_reg.score(X_test, y_test))

print("Y Intercept >>", lin_reg.intercept_)
print("X Coefficient >>", lin_reg.coef_)

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
plt.scatter(y_test, y_pred)
plt.ylabel('Price')
plt.xlabel('Actual vs Predicted Price')
plt.show();

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

    #Cross val Score
lin_reg = LinearRegression()
cvscores_10 = cross_val_score(lin_reg, X, y, cv= 10)
print("Cross val Score =", np.mean(cvscores_10))

    #Accuracy Boosting
xgb_reg = XGBRegressor()
xgb_reg.fit(X_train, y_train)
print("Boost Training accuracy: ", xgb_reg.score(X_train, y_train))
print("Boost Testing accuracy: ", xgb_reg.score(X_test, y_test))
cvscores_10 = cross_val_score(xgb_reg, X, y, cv= 10)
print("Cross val Score =", np.mean(cvscores_10))