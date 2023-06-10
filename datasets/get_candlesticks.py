apikey = "3caf46a9-be6d-4671-a468-c12a9146d68f"
# secretkey = "9A38782D92569BAEEDDE43186697BC72"
import okx.MarketData as MD
import time
import pandas as pd
flag ='1'
MDAPI = MD.MarketAPI(flag=flag)
def iter_get_data(instId, bar, limit,sleep_time=0.2):
    datas = []
    ## https://www.okx.com/docs-v5/zh/#rest-api-market-data-get-candlesticks-history
    data = MDAPI.get_history_candlesticks(instId= instId,bar=bar,limit=limit)['data']
    time.sleep(sleep_time)
    while data:
        datas.extend(data)
        try:
            data = MDAPI.get_history_candlesticks(instId= instId,bar=bar,limit=limit,after=data[-1][0])['data']
        except:
            data = []
        time.sleep(sleep_time)
    return datas
def get_dataFrame(fromInst:str,toInst:str,bar:str,filename:str=None):
    instId = fromInst.upper() + '-' + toInst.upper()+ '-SWAP' 
    df = pd.DataFrame(iter_get_data(instId,bar, 1440))
    df = df.apply(lambda x:pd.to_numeric(x))
    df = df.iloc[:,:-2]
    df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'currency_volume']
    df['date']= pd.to_datetime(df['date'],unit='ms')
    df.set_index('date',inplace=True)
    if filename:
        df.to_csv('../datasets/'+filename+'.csv')
        return '../datasets/'+filename+'.csv'
    return df
