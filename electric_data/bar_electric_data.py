import pandas as pd
import matplotlib.pyplot as plt
from mpldatacursor import datacursor
from matplotlib import ticker

df = pd.read_csv(r'/Users/carlykostka/Documents/CodeProjects/electric_data/results.csv', delimiter=',') 

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
df.plot(kind = 'bar', x = 'Year', y = 'Revenue', color = 'c', ax=ax1)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(False) 
ax1.yaxis.set_major_formatter(formatter) 
ax1.xaxis.set_label_text("Year")
ax1.yaxis.set_label_text("Revenue ($)")
ax1.set_title("How Electrical Company Revenue Changes Over the Years (1990-2020)")
def formatter(**kwargs):
    height = kwargs['height']
    return "$ {}".format(height)
datacursor(formatter=formatter)

df.plot(kind = 'bar', x = 'Year', y = 'Price', color = 'r', ax=ax2)
ax2.xaxis.set_label_text("Year")
ax2.yaxis.set_label_text("Price (cents/kw/hr)")
ax2.set_title("How Consumer Prices of electricty Change Over the Years (1990-2020)")
fig.subplots_adjust(hspace=1)
def formatter(**kwargs):
    height = kwargs['height']
    return "{} cents".format(height)
datacursor(formatter=formatter)

df.plot(kind = 'bar', x = 'Year', y = 'Sales', color = 'purple', ax=ax3)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(False) 
ax3.yaxis.set_major_formatter(formatter) 
ax3.xaxis.set_label_text("Year")
ax3.yaxis.set_label_text("Sales")
ax3.set_title("How Sales of electricty Change Over the Years (1990-2020)")
fig.subplots_adjust(hspace=1)
def formatter(**kwargs):
    height = kwargs['height']
    return "$ {}".format(height)
datacursor(formatter=formatter)

fig.suptitle('*2020-2021 data not finalized*')
plt.show()

# df.plot(kind='bar', x='Year', y=['Revenue', 'Sales', 'Customers', 'Price'], color=['red', 'blue', 'cyan', 'purple'])
# plt.ticklabel_format(style='plain', axis='y')
# plt.xticks(rotation=45)
# plt.title('Trends of Electricty from 1990-2020 ')
# plt.xlabel('Year')
# def formatter(**kwargs):
#     height = kwargs['height']
#     return "{} deaths".format(height)
# datacursor(formatter=formatter, hover=True)
# plt.show()