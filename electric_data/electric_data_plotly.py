import pandas as pd
import plotly.express as px
import pandas as pd
import plotly.subplots as sp


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

# Plotly graph
df = pd.read_csv(r'/Users/carlykostka/Documents/CodeProjects/electric_data/results.csv', delimiter = ',')
fig1 = px.line(df, x = 'Year', y = 'Revenue')
fig2 = px.line(df, x = 'Year', y = 'Price')
fig2.update_traces(line_color='red')
figure1_traces = []
figure2_traces = []
for trace in range(len(fig1["data"])):
    figure1_traces.append(fig1["data"][trace])
for trace in range(len(fig2["data"])):
    figure2_traces.append(fig2["data"][trace])
this_figure = sp.make_subplots(
              rows=2, cols=1, 
              subplot_titles = ("How Electrical Company Revenue Changes Over the Years (1990-2021)",
                               "How Consumer Prices of electricty Change Over the Years (1990-2021)")) 
                               
for traces in figure1_traces:
    this_figure.append_trace(traces, row = 1, col = 1)
for traces in figure2_traces:
    this_figure.append_trace(traces, row = 2, col = 1)

this_figure.update_traces(mode = "markers+lines")
this_figure.update_xaxes(title = 'Year')
this_figure.update_yaxes(title = 'Price (cents/kw/hr)')
this_figure.update_layout(title = "*2020-2021 data not finalized*", 
                          xaxis_title = "Year", yaxis_title = "Revenue ($)", 
                          title_font_size = 12)
this_figure.show()


# df = pd.read_csv(r'/Users/carlykostka/Documents/CodeProjects/electric_data/results.csv', delimiter = ',') 
# fig = px.line(df, x = 'Year', y = ['Revenue', 'Price'], title = 'Revenue and Price Change')
# fig.update_traces(mode="markers+lines")
# fig.show()