import datetime as dt
import numpy as np
import math

def preprocessing(df):
    #[例2]
    #走破タイムを「分.秒.コンマ秒」→「秒」などに変換する
    def convert_time(x):
        if str(x) == 'nan':
            return x
        
        sp = x.split('.')
        
        #1分以内(ex: 58.9)
        if len(sp) == 2:
            return float(sp[0])+ float(sp[1])*0.1
        #1分以上(ex: 1.30.9)
        if len(sp) == 3:
            return float(sp[0])*60 + float(sp[1]) + float(sp[2])*0.1
    
    df['走破タイム_1走前'].apply(convert_time)
    df['走破タイム_2走前'].apply(convert_time)
    df['走破タイム_3走前'].apply(convert_time)
    
    #開催月,開催日を分割
    df['開催月'] = df['開催日付'] //100
    df['開催日'] = df['開催日付'] %100

    df['開催月_1走前'] = df['開催日付_1走前'] //100
    df['開催日_1走前'] = df['開催日付_1走前'] %100
    df['開催月_2走前'] = df['開催日付_2走前'] //100
    df['開催日_2走前'] = df['開催日付_2走前'] %100
    df['開催月_3走前'] = df['開催日付_3走前'] //100
    df['開催日_3走前'] = df['開催日付_3走前'] %100

    #レース間隔(前走から何日)
    def interval(x):
        x = x.replace('.0','')
        
        if x.find('nan') > 0:
            return np.nan
        
        date = x.split(':')
        
        now = dt.date(int(date[0]),int(date[1])//100,int(date[1])%100)
        pre = dt.date(int(date[2]),int(date[3])//100,int(date[3])%100)
        return (now - pre).days
        
    df['レース間隔'] = df['開催年'].astype('str') + ':' + df['開催日付'].astype('str') + ':' + df['開催年_1走前'].astype('str') + ':' + df['開催日付_1走前'].astype('str')
    df['レース間隔'] = df['レース間隔'].apply(interval)


    #開催月日を三角関数で変換
    df['開催月_sin'] = df['開催月'].apply(lambda x:np.sin(math.radians(x/12)))
    df['開催月_cos'] = df['開催月'].apply(lambda x:np.cos(math.radians(x/12)))
    df['開催日_sin'] = df['開催日'].apply(lambda x:np.sin(math.radians(x/31)))
    df['開催日_cos'] = df['開催日'].apply(lambda x:np.cos(math.radians(x/31)))


    return df