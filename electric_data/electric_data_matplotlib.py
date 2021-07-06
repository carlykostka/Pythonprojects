import pandas as pd
import matplotlib.pyplot as plt
from mpldatacursor import datacursor
from matplotlib import ticker

# Opening and rewriting cvs file to extract parsed data that is needed
f = open('//Users/carlykostka/OneDrive/Documents/Coding/1990_2021_revenue_prices_US.csv', 'r')
w = open('results.csv', 'w')
header = 'Year,Revenue,Sales,Customers,Price\n'
w.writelines(header)
count = 0 
for line in f.readlines():
    if count < 3:
        count = count + 1
        continue
    parsed_data = line.split(',')
    if parsed_data[1] == '.':
        new_line = parsed_data[0] + ',' + parsed_data[3] + ',' + parsed_data[4] + ',' + parsed_data[5] + ',' + parsed_data[6]
        w.writelines(new_line)   
w.close()

# Reading in new csv file and visualizing the data in a linear graph with matplotlib
df = pd.read_csv(r'/Users/carlykostka/Documents/CodeProjects/electric_data/results.csv', delimiter=',') 

# Subplot 1
fig, (ax1, ax2) = plt.subplots(2, 1)
df.plot(kind = 'line', x = 'Year', y = 'Revenue', color = 'c', marker = 'o', ax=ax1)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(False) 
ax1.yaxis.set_major_formatter(formatter) 
ax1.set_ylim((0, 450000000))
ax1.xaxis.set_label_text("Year\n *2020-2021 data not finalized*")
ax1.yaxis.set_label_text("Revenue ($)")
ax1.set_title("How Electrical Company Revenue Changes Over the Years (1990-2020)")
def formatter(**kwarg):
    label = 'Year: {x:.0f}\n Revenue: ${y:.0f}'.format(**kwarg)
    return label
datacursor(ax1, formatter=formatter, hover = True)

# Subplot 2
df.plot(kind = 'line', x = 'Year', y = 'Price', color = 'r', alpha = 0.3, marker = 'o', ax=ax2)
ax2.xaxis.set_label_text("Year")
ax2.yaxis.set_label_text("Price (cents/kw/hr)")
ax2.set_title("How Consumer Prices of electricty Change Over the Years (1990-2020)")
fig.subplots_adjust(hspace=0.5)
def formatter(**kwarg):
    label = 'Year: {x:.0f}\n Consumer Price: {y:.0f}'.format(**kwarg)
    return label
datacursor(ax2, formatter=formatter, hover = True)
plt.show()


    