import requests
import time
import pandas as pd
CANDLES = "https://www.okx.com/priapi/v5/market/history-candles"
TRADES = "https://www.okx.com/api/v5/market/history-trades"
GOOGLE = 29798540
META = 14917609
APPLE = 908440
AMAZON = 645156
class VCdata:
    def __init__(self,coin,start,end) -> None:
        self.instruId = coin.upper()
        self.start = start
        pass
    def get_price(self,sleep_time=0.4):
        pricedata = self.get_vcprice(self.instruId,'USDT','1H')
        from finta import TA
        pricedata['SMA'] = TA.SMA(pricedata, 7)
        pricedata['CCI'] = TA.CCI(pricedata)
        pricedata['ADX'] = TA.ADX(pricedata)
        pricedata['STOCH'] = TA.STOCH(pricedata)
        pricedata['ATR'] = TA.ATR(pricedata)
        pricedata[['upper_bb', 'middle_band', 'lower_bb']] = TA.BBANDS(pricedata)
        pricedata['RSI'] = TA.RSI(pricedata)
        pricedata['MOM'] = TA.MOM(pricedata)
        pricedata['EMA'] = TA.EMA(pricedata, 7)
        pricedata[['MACD','MACDSingal']] = TA.MACD(pricedata,column='open')
        pricedata = pricedata.dropna()
        pricedata.index = pricedata.index.strftime('%Y-%m-%d')
        return pricedata
        
    def okxApi(self,baseUrl,instrument,bar,limit,after=None):
        if after:
            parms = {'instId':instrument,'bar':bar,'limit':limit,'after':after}
        else:
            parms = {'instId':instrument,'bar':bar,'limit':limit}
        data = requests.get(url=baseUrl,headers={'User-Agent':'Mozilla/5.0','content-type':'application/json'},params=parms).json()['data']
        return data
    def iter_get(self,baseUrl,instrument,bar,sleep_time=0.2):
        datas = []
        data = self.okxApi(baseUrl,instrument,bar,limit=1000)
        time.sleep(sleep_time)
        while data:
            datas.extend(data)
            try:
                data = self.okxApi(baseUrl,instrument,bar,limit=1000,after=pricedata[-1][0])
            except:
                data = []
            time.sleep(sleep_time)
        return datas
    def get_vcprice(self,fromInst:str,toInst:str,bar:str,filename:str=None,start=None,end=None):
        instId = fromInst.upper() + '-' + toInst.upper()
        df = pd.DataFrame(self.iter_get(CANDLES,instId,bar))
        df = df.apply(lambda x:pd.to_numeric(x))
        df = df.iloc[:,:-2]
        df.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'currency_volume']
        df['date']= pd.to_datetime(df['date'],unit='ms')
        df.set_index('date',inplace=True)
        if filename:
            df.to_csv('../datasets/'+filename+'.csv')
            return '../datasets/'+filename+'.csv'
        # pricedata.to_csv('datasets/BTC_USDT_1D_pricedata.csv')
        return df
    def get_trade(self,instId, limit,sleep_time=0.2):
        datas = []
        parms = {'instId':instId,'limit':limit}
        data = requests.get(url=TRADES,headers={'User-Agent':'Mozilla/5.0','content-type':'application/json'},params=parms).json()['data']
        time.sleep(sleep_time)
        while data:
            datas.extend(data)
            try:
                data = requests.get(url=TRADES,headers={'User-Agent':'Mozilla/5.0','content-type':'application/json'},params={'instId':instId,'limit':limit,'after':pricedata[-1]['ts']}).json()['data']
            except:
                data = []
            time.sleep(sleep_time)
        return datas
    def get_tradedf(self,fromInst:str,toInst:str,limit:int,filename:str=None):
        instId = fromInst.upper() + '-' + toInst.upper()
        df = pd.DataFrame(self.get_trade(instId,limit))
        df = df.apply(lambda x:pd.to_numeric(x))
        df['ts']= pd.to_datetime(df['ts'],unit='ms')
        df.set_index('ts',inplace=True)
        if filename:
            df.to_csv('../datasets/'+filename+'.csv')
            return '../datasets/'+filename+'.csv'
        return df
    def getMarketEmotion(self,fromInst:str,toInst:str,limit:int,filename:str=None):
        ##获得市场情绪数据
        import pandas as pd
        url = "https://api.alternative.me/fng/?limit=2000&date_format=us"
        import requests
        response =requests.get(url=url,headers={'User-Agent':'Mozilla/5.0','content-type':'application/json'})
        data = response.json()['data']
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['timestamp'])
        df.set_index('date',inplace=True)
        df = df.iloc[:,:2]
        df['FearGreedIndex'] = df['value'].astype('int')
        df = df.iloc[::-1]
        return df['FearGreedIndex']
    
    def getMarketCap(self,Inst:str,start,end,interval='1d'):
        response = requests.get(url=f'https://api.coinmarketcap.com/data-api/v3/global-metrics/quotes/historical?interval={interval}&timeEnd={end}&timeStart={start}')
        marketcap = pd.DataFrame(response.json()['data']['quotes'])
        marketcap['date'] = pd.to_datetime(marketcap['timestamp'])
        marketcap.set_index('date',inplace=True)
        ## 数据清洗
        marketcap[marketcap==0] = np.nan
        marketcap['date'] = pd.to_datetime(marketcap['timestamp'])
        marketcap.set_index('date',inplace=True)
        marketcap.fillna(method='bfill',inplace=True)
        marketcap = marketcap.iloc[:,2:]
        USD = [response.json()['data']['quotes'][i]['quote'][0] for i in range(len(response.json()['data']['quotes']))]
        USD = pd.DataFrame(USD)
        USD.columns = ['USD'+i for i in USD.columns]
        USD['date'] = pd.to_datetime(USD['USDtimestamp'])
        USD.set_index('date',inplace=True)
        USD = USD.iloc[:,2:]
        marketcapall = pd.merge(marketcap,USD,on='date')
        marketcapall.drop(columns=['quote'],inplace=True)
        marketcapall.index = pd.to_datetime(marketcapall.index.strftime('%Y-%m-%d'))
        return marketcapall.iloc[:,:-2]
    
    def getStockData(self,company,datefrom,dateto):
        url = f'https://markets.businessinsider.com/Ajax/Chart_GetChartData?instrumentType=Share&tkData=1178,{company},1178,333&from={datefrom}&to={dateto}'
        response = requests.get(url=url,headers={'User-Agent':'Mozilla/5.0','content-type':'application/json'})
        data = response.json()[:-1]
        df = pd.DataFrame(data)
        df['date'] = pd.to_datetime(df['Date'])
        df.set_index('date',inplace=True)
        return df.iloc[:,:5]
    def getAllStockData(self,datefrom='20180101',dateto='20230612'):
        names = ['GOOGLE','META','APPLE','AMAZON']
        df = None
        for i,d in enumerate([GOOGLE,META,APPLE,AMAZON]):
            getdata = self.getStockData(d,datefrom,dateto)
            if df is None:
                df = getdata
            df[f'{names[i]}Price'] =getdata['Close']
            df[f'{names[i]}Volume']=getdata['Volume'] 
        return df.iloc[:,-2:]
        # alldata = pd.merge(alldata,df.iloc[:,-2:],on='date')
    def get_dataset(self):
        ## 获得数据集
        pricedata = self.get_pricedata(self.fromInst,self.toInst,self.start,self.end,self.i)
        emotiondata = self.getMarketEmotion(self.fromInst,self.toInst,self.i)
        marketcap = self.getMarketCap(self.fromInst,self.start,self.end)
        stockdata = self.getAllStockData(self.start,self.end)
        alldata = pd.merge(pricedata,emotiondata,on='date')
        alldata = pd.merge(alldata,marketcap,on='date')
        alldata = pd.merge(alldata,stockdata,on='date')
        alldata = alldata.iloc[1:,:]
        alldata.to_csv('../datasets/'+self.fromInst+'-'+self.toInst+'-'+self.start+'-'+self.end+'.csv')
        return alldata
        
if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    vcdata = VCdata('btc','2021-01-01','2021-07-01')
    vcdata.get_dataset()
