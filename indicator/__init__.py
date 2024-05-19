import talib as tl
 
 
def getMACD(df_close_data, fastperiod=12, slowperiod=26,signalperiod=9):
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
    dif, dea,_= tl.MACD(df_close_data, fastperiod, slowperiod,signalperiod)
    return dif, dea, _*2