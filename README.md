# stock_digging_2-
An Empirical Examination of Stochastic Properties of A-Share Stock Returns

In recent studies, I have learned about stochastic processes and an interesting stylized fact that stock price changes tend to follow normal distributions in equity markets. Adhering to the principle of "practice makes perfect," I conducted an empirical analysis by randomly selecting several A-share stocks and examining their daily return patterns. The research method and key findings are summarized below:

1. Get the data from internet, using the data from package: baostock, which helps me to find every stock price in history.
2. When I learned the stochastic processes, Stock returns typically follow a log-normal distribution. So I try to collect stock return rate as in $\frac{open[time_t] - close[time_(t - 1)]}{open(time_t)}$ to get the rate of return by using excel.
3. Then I put them into python to do test about the normal distribution (Kolmogorov-Smirnov test). The result is amazing(china_airplane.py):

I also try other company as well(china_tele.py):

I didn't believe at the first time, then I try to do with a random number, here is the result(random_number.py):

As the I find that the sh.601111 doesn't follow the normal distribution, I begin to try other stock in America, given Tesla as an example(Tesla.py):
![image](https://github.com/shenshenland/stock_digging_2-/blob/main/tesla_stock.png)
Then I still try the UK stock like HSBA(HSBA.py):

