from datetime import date
import akshare as ak
import arrow
import arrow
import pandas as pd
import os.path
import sys
cpath_current = os.path.dirname(os.path.dirname(__file__))
cpath = os.path.abspath(os.path.join(cpath_current))
sys.path.append(cpath)
def trade_date():
    path = f'{cpath}/stock_date/trade_date.csv'
    try:
        csvframe = pd.read_csv(path,dtype={'trade_date': str,})
        csvframe["trade_date"]=date(*map(int, csvframe["trade_date"].split('-')))
        return csvframe
    except Exception as e:
        temp_df =  ak.tool_trade_date_hist_sina()
        temp_df.to_csv(path, mode='w', index=False, header=True, sep=',')
        return temp_df 

def get_pre_trade_date(now_date=arrow.now().format("YYYY-MM-DD"),pre=None):
    now_date=date(*map(int, now_date.split('-')))
    tool_trade_date_hist_sina_df = trade_date()
    df = tool_trade_date_hist_sina_df.loc[tool_trade_date_hist_sina_df['trade_date'] <=  now_date]
    df = df.iloc[::-1].reset_index(drop = True)
    list = df['trade_date'].values.tolist() 
    if pre is None:
        return list
    else :
        return list[pre]
if __name__ == '__main__':
    # trade_date()
    df = get_pre_trade_date('2024-06-19',pre=1)
    print(df)