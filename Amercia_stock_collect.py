import yfinance as yf
import pandas as pd

def export_stock_data(ticker, start_date, end_date, output_file):
    # 获取特斯拉的股票数据/ get the data from tesla
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # 将数据保存到CSV文件/ restore the file to csv file
    stock_data.to_csv(output_file)

if __name__ == "__main__":

    ticker = "TSLA"  # 特斯拉的股票代码/stock code
    start_date = "2023-01-01"  # 开始日期/start date
    end_date = "2023-07-31"  # 结束日期/ending date
    output_file = "tesla_stock_data.csv"  # 导出文件的名称/name of the output file

    # 导出股票数据到CSV文件/ put the data into file
    export_stock_data(ticker, start_date, end_date, output_file)