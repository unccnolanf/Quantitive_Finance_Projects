import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf

# import data
def get_data(stocks, start, end):
    stockData = yf.download(stocks,start=start,end=end,auto_adjust=True)
    returns = stockData.pct_change(fill_method=None)
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns,covMatrix

stocklist = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'JPM']
stocks = stocklist
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days = 300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)
print(meanReturns)

#assigns random weights (percentange) to each of 6 stocks
weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

print(weights)

# Monte Carlo Method
# number of simulations

mc_sims = 100
T = 100 #timeframe in days
initial_portfolio = 10000

meanM = np.repeat(meanReturns.values.reshape(-1,1), T, axis=1)

portfolio_sims = np.full((mc_sims, T), 0.0)

for m in range(0,mc_sims):
    #MC loops
    Z = np.random.normal(size =(len(weights), T))
    L = np.linalg.cholesky(covMatrix)
    daily_returns = meanM + L @ Z
    portfolio_returns = np.dot(weights, daily_returns)
    portfolio_sims[m, :] = np.cumprod(1 + portfolio_returns) * initial_portfolio

#Plot all data
plt.plot(portfolio_sims.T)
plt.ylabel('Portfolio value')
plt.xlabel('Days')
plt.title('MC Stock Portfolio Simulation')
plt.show()




