from input import input_from_excel
from output import output_graph
import numpy as np
import pandas as pd
import itertools
userid = 'b1018336'
list_data=[]
#df1 = input_from_excel("201909_後期.xlsx")
#df2 = input_from_excel("202004_前期.xlsx")
files = input_from_excel()
for i, j in enumerate(files):
    #print(files[i])
    df=pd.read_excel('%s'%files[i],header=5)
    df1=df[['# ユーザID','１．システム情報科学に関する高い専門能力（コース共通）',
           '１．システム情報科学に関する高い専門能力（コース専門能力）',
           '１．システム情報科学に関する高い専門能力（卒業研究）',
           '２．研究的態度を支える問題探究力・構想力',
           '３．共創のための情報表現能力・チームワーク力',
           '４．自律的に学び続けるためのメタ学習力',
           '５．専門家として持つべき人間性']]
    data=df1[df1['# ユーザID']==userid]
    data2=data.values.tolist()
        #1次元配列に戻す
    data3=list(itertools.chain.from_iterable(data2))
        #配列の0番（userid）を削除
    del data3[0]
    list_data.append(data3)
#df2 = input_from_excel(files[1])
#data2=df2[df2['# ユーザID']==userid]
output_graph(list_data)
print(list_data)
