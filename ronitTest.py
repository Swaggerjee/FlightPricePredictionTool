import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
file_path = '/Raw Data/Clean_Dataset.csv'  # Update this path
data = pd.read_csv(file_path)

# Data cleaning
data_cleaned = data.drop(columns=['Unnamed: 0'])

# Exploratory Data Analysis (EDA)
plt.figure(figsize=(10, 6))
sns.histplot(data_cleaned['price'], bins=50, kde=True)
plt.title('Distribution of Ticket Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='days_left', y='price', data=data_cleaned, alpha=0.5)
plt.title('Ticket Price vs. Days Left Until Flight')
plt.xlabel('Days Left')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='stops', y='price', data=data_cleaned)
plt.title('Ticket Price by Number of Stops')
plt.xlabel('Number of Stops')
plt.ylabel('Price')
plt.show()

plt.figure(figsize=(12, 8))
sns.boxplot(x='price', y='airline', data=data_cleaned)
plt.title('Ticket Prices Across Different Airlines')
plt.xlabel('Price')
plt.ylabel('Airline')
plt.show()

# Feature Engineering and Encoding
# One-hot encoding
one_hot_columns = ['departure_time', 'stops', 'arrival_time', 'class']
data_encoded = pd.get_dummies(data_cleaned, columns=one_hot_columns)

# Label encoding
label_encoder = LabelEncoder()
data_encoded['airline_encoded'] = label_encoder.fit_transform(data_encoded['airline'])
data_encoded['flight_encoded'] = label_encoder.fit_transform(data_encoded['flight'])
data_encoded['source_city_encoded'] = label_encoder.fit_transform(data_encoded['source_city'])
data_encoded['destination_city_encoded'] = label_encoder.fit_transform(data_encoded['destination_city'])

data_encoded.drop(columns=['airline', 'flight', 'source_city', 'destination_city'], inplace=True)

# Model Selection and Training
X = data_encoded.drop('price', axis=1)
y = data_encoded['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

linear_regression_model = LinearRegression()
linear_regression_model.fit(X_train, y_train)

y_pred = linear_regression_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse}, RMSE: {rmse}, MAE: {mae}, R^2: {r2}")

# Prediction Function (simplified example)
def predict_flight_price(airline, flight, source_city, departure_time, stops, arrival_time, destination_city, class_type, duration, days_left):
    # Example function to outline the process. Actual implementation would require encoding the inputs.
    pass