import pandas as pd
import talib
 
def talib_MACDEXT(df_vol_data):
   macdDIFF, macdDEA, macd = talib.MACDEXT(df_vol_data, fastperiod=12, fastmatype=1, slowperiod=26,    slowmatype=1, signalperiod=9, signalmatype=1)
 
   return (macdDIFF, macdDEA, macd)

def talib_MACD(df_close_data, fastperiod=10, slowperiod=22):
    """
        talib官方默认参数 fastperiod=12, slowperiod=26,signalperiod=9
        参数:
            fastperiod:快线【短周期均线】
            slowperiod:慢线【长周期均线】
            signalperiod:计算signalperiod天的macd的EMA均线【默认是9,无需更改】
        返回参数：
            macd【DIF】 = 12【fastperiod】天EMA - 26【slowperiod】天EMA
            macdsignal【DEA或DEM】 = 计算macd的signalperiod天的EMA
            macdhist【MACD柱状线】 = macd - macdsignal
    """
    # macd, macdsignal, macdhist = getattr(talib, "MACD")(
    #     df_close_data, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=9)
    
    macd, macdsignal, macdhist =talib.MACD(df_close_data, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=7)
    macd_df = pd.DataFrame({
        "macd": macd,
        "macdsignal": macdsignal,
        "macdhist": macdhist
    })
    return macd_df