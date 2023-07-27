import yfinance as yf
import pandas as pd

def export_stock_data(ticker, start_date, end_date, output_file):
    # ��ȡ��˹���Ĺ�Ʊ����/ get the data from tesla
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # �����ݱ��浽CSV�ļ�/ restore the file to csv file
    stock_data.to_csv(output_file)

if __name__ == "__main__":

    ticker = "TSLA"  # ��˹���Ĺ�Ʊ����/stock code
    start_date = "2023-01-01"  # ��ʼ����/start date
    end_date = "2023-07-31"  # ��������/ending date
    output_file = "tesla_stock_data.csv"  # �����ļ�������/name of the output file

    # ������Ʊ���ݵ�CSV�ļ�/ put the data into file
    export_stock_data(ticker, start_date, end_date, output_file)