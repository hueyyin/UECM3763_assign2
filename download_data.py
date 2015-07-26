from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p


# Download daily data from Yahoo!Finance starting from 1 Jan 2011 until 20 July 2015
start = dt(2011, 1, 1)
end = dt(2015, 7, 20)


# Genting Malaysia Bhd (code: 4715) is chosen
GENM_close = DR("4715.KL", 'yahoo', start, end)['Close'] #Obtaining closing stock prices


# 5-day moving average of Genting Malaysia Bhd stock prices
ave = 5
mov_ave = pd.rolling_mean(GENM_close,ave) # Use the builit in function in pandas to calculate the moving average


# 5-day moving average plot for the downloaded data
p.plot(mov_ave)
p.xlabel('Day')
p.ylabel('5-day Moving Average')
p.title('5-day Moving Average Plot of Genting Malaysia Bhd \n [1 Jan 2011 - 20 July 2015] ' )
p.show()


# Download and combine FTSEKLCI daily data for the same duration
combine=['4715.KL','^KLSE']
closing = DR(combine, 'yahoo', start, end)['Adj Close']


# Compute the correlation of your Genting Malaysia Bhd with FTSEKLC
correlation = closing.corr()
print('Correlation between Genting Malaysia Bhd and FTSEKLCI:  \n' + str(correlation))