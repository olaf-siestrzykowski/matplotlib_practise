import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Data Manipulation in Python Master Python, Numpy & Pandas/iris.csv')

x_axis = df.index
y_axis = df['petal.length']

# Scatter Plot
sns.scatterplot(x=x_axis, y=y_axis, hue=df['variety'])

# Strip Plot
sns.stripplot(x=df['variety'], y=df['petal.length'])

# Distribution Plot
sns.distplot(df['petal.length'])

# Histogram Plot
sns.histplot(df['petal.length'])

# Box Plot
sns.boxplot(x=df['petal.length'])

# Count Plot
sns.countplot(df['variety'])

# Pie Chart
labels = ['Setosa', 'Versicolor', 'Virginica']
plt.pie(df['variety'].value_counts(), labels=labels)

plt.show()
