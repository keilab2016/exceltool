from input import input_from_excel
from output import output_graph
import numpy as np
import pandas as pd
import itertools
import section
userid = 'b1018336'

list_data=[]
#df1 = input_from_excel("201909_後期.xlsx")
#df2 = input_from_excel("202004_前期.xlsx")
files = input_from_excel()
for i, j in enumerate(files):
    #print(files[i])
    df=pd.read_excel('%s'%files[i],header=5)
    if(section.sectionList[0] != '# ユーザID'):  #複数グラフを作る場合、sectionリストの要素が減り続けるのを防ぐ
        section.sectionList.insert(0,'# ユーザID')
    df1=df[section.sectionList] #section.pyから列名のリストを取得
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
