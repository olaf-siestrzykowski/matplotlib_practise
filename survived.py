import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('Data Manipulation in Python Master Python, Numpy & Pandas/titanic.csv')

survived_ratio = df[['Pclass', 'Survived']].groupby('Pclass').sum()

# Survived Bar Plot
sns.barplot(x=survived_ratio.index, y=survived_ratio['Survived'])

# Box Plot Survived by Age
sns.boxplot(x=df['Survived'], y=df['Age'])

# Sex by Age
sns.barplot(x=df['Sex'], y=df['Age'])

plt.show()
