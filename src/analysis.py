import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/Housing_new.csv')

# Handle missing values
df['price'] = df['price'].fillna(df['price'].mean())
df['parking'].fillna(0, inplace=True)
df['bathrooms'] = df['bathrooms'].interpolate()

# Outlier detection
column = 'price'
Q1 = df[column].quantile(0.25)
Q3 = df[column].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR
outliers = df[(df[column] < lower_limit) | (df[column] > upper_limit)]

print("Outliers in", column)
print(outliers)
print(df.describe())

# Rename column
df = df.rename(columns={'price': 'Price_new'})

# Line Plot: Price vs Area
df.plot(x='Price_new', y='area', kind='line', title='Area vs Price', legend=True)
plt.xlabel('Price')
plt.ylabel('Area')
plt.grid(True)
plt.show()

# Scatter Plot: Price vs Area
plt.scatter(df['Price_new'], df['area'])
plt.title('Area and Price')
plt.xlabel('Price_new')
plt.ylabel('Area')
plt.grid(True)
plt.tight_layout()
plt.show()

# Pie Chart: Parking distribution
df['parking'].value_counts().plot(kind='pie', autopct='%1.1f%%', title='Distribution of Parking')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Histogram: Price distribution
df['Price_new'].plot(
    kind='hist',
    bins=20,
    title='Distribution of Price',
    color='skyblue',
    edgecolor='black',
    grid=True
)
plt.xlabel('Price')
plt.tight_layout()
plt.show()
