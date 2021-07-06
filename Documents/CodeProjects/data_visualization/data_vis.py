#Imports  
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataframe = pd.read_csv(r'/Users/carlykostka/Downloads/exercise_dataset.csv') 
print(dataframe.head())

dataframe.head().plot(kind='bar', x='Activity, Exercise or Sport (1 hour)', y='130 lb', color='blue')
plt.title('Calories burned by different weight groups ')
plt.xlabel('Activity')
plt.ylabel('Calories burned for every 1 hour')
plt.show()

  
