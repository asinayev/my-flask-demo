import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show

def makeplot(ticker):
	stockdat = pd.read_csv("https://www.quandl.com/api/v3/datasets/WIKI/%s.csv?start_date=2016-07-01&end_date=2016-08-01" % ticker)
	output_file("templates/lines.html")
	p = figure(title='Stocks',x_axis_label='Date', y_axis_label='Closing Price', 
				x_axis_type="datetime")
	dates = stockdat['Date'].astype('datetime64')
	p.line(dates, stockdat['Close'], legend="Price", line_width=2)
	show(p)