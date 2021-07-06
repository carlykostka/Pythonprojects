from matplotlib import axes
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.io.formats import style
import mplcursors
from mpldatacursor import datacursor


df = pd.read_csv(r'/Users/carlykostka/Downloads/Provisional_COVID-19_Deaths_by_Sex_and_Age.csv', nrows=17) 
# print(df.head())

select_agegroup1 = df.loc[df['Age Group'] != 'All Ages']
df.drop(df.index[df['Age Group'] == 'All Ages'], inplace = True)
print(df[['Age Group', 'COVID-19 Deaths', 'Total Deaths']])

# Bar Graph
df.plot(kind='bar', x='Age Group', y=['COVID-19 Deaths', 'Total Deaths'], color=['red', 'blue'])
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45)
plt.title('COVID-19 Deaths and Total Deaths in the US based on Age Groups ')
plt.xlabel('Age Group')
plt.ylabel('COVID-19 & Total Deaths')
def formatter(**kwargs):
    height = kwargs['height']
    return "{} deaths".format(height)
datacursor(formatter=formatter, hover=True)
plt.show()

#Line Graph
df.plot(kind='line', x='Age Group', y=['COVID-19 Deaths', 'Total Deaths'], color=['red', 'blue'])
plt.ticklabel_format(style='plain', axis='y')
plt.xticks(rotation=45)
plt.title('COVID-19 Deaths and Total Deaths in the US based on Age Groups ')
plt.xlabel('Age Group')
plt.ylabel('COVID-19 & Total Deaths')
def formatter(**kwargs):
    height = kwargs['height']
    return "{} deaths".format(height)
datacursor(formatter=formatter, hover=True)
plt.show()

# Pie Chart
labels = 'Total Covid-19 Deaths', 'Total Deaths'
sizes = [592682, 4847715]
explode = (0, 0.1) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

# Scatterplot

ax1 = df.plot(kind='scatter', x='Age Group', y='COVID-19 Deaths', color='red')
ax2 = df.plot(kind='scatter', x='Age Group',y= 'Total Deaths', color='blue', ax=ax1)
plt.xticks(rotation=45)
plt.ticklabel_format(style='plain', axis='y')
plt.title('COVID-19 Deaths and Total Deaths in the US based on Age Groups ')
plt.xlabel('Age Group')
plt.ylabel('COVID-19 & Total Deaths')
mplcursors.cursor(hover=True)
plt.show()





