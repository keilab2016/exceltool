from input import input_from_excel
from output import output_graph
import numpy as np
import pandas as pd
import itertools
import sys

list_data=[]

#指定ディレクトリのexcelファイル名をlist型で取得
files = input_from_excel()

#コマンド引数を取得
args = sys.argv

#argsをstr型に変換
args_list=list(map(str,args))

#args_list[0]削除　0番には、ファイル名が入っているため
del args_list[0]

for a ,b in enumerate(args_list):
    #コマンド引数で指定された学籍番号を1つずつ挿入
    userid=args_list[a]

    for i, j in enumerate(files):
        df=pd.read_excel('%s'%files[i],header=5)
        df1=df[['# ユーザID','１．システム情報科学に関する高い専門能力（コース共通）',
           '１．システム情報科学に関する高い専門能力（コース専門能力）',
           '１．システム情報科学に関する高い専門能力（卒業研究）',
           '２．研究的態度を支える問題探究力・構想力',
           '３．共創のための情報表現能力・チームワーク力',
           '４．自律的に学び続けるためのメタ学習力',
           '５．専門家として持つべき人間性']]
        #excelをdataframe化したdf1とuseridが一致するものをdataframe型で抽出
        data=df1[df1['# ユーザID'].isin([userid])]

        #data(dataframe型)をlist化（２次元配列になってしまう）
        data2=data.values.tolist()

        #1次元配列に戻す
        data3=list(itertools.chain.from_iterable(data2))

        #print(data3)
        #配列の0番（userid）を削除
        del data3[0]
        list_data.append(data3)
print(list_data)
        #output_graph(list_data)
