from input import input_from_excel
from input import make_year_list
from output import output_graph
import numpy as np
import pandas as pd
import section
import itertools
import sys
import openpyxl
import os

#ディレクトリが存在していなければ作成
if(os.path.exists('image') == False):
    os.mkdir('image')

if(os.path.exists('output') == False):
    os.mkdir('output')
 
#コマンド引数を取得
args = sys.argv

#argsをstr型に変換
args_list=list(map(str,args))

#args_list[0]削除　0番には、ファイル名が入っているため
del args_list[0]


for a ,b in enumerate(args_list):
    #コマンド引数で指定された学籍番号を1つずつ挿入
    userid=args_list[a]
    admission_year="20"+userid[3:5]
    print(admission_year)
    list_data=[]
    make_year_list(admission_year)
    #指定ディレクトリのexcelファイル名をlist型で取得
    files = input_from_excel()

    for i, j in enumerate(files):
        if(files[i]!=''): #20〇〇年○期のデータが存在する場合
            df=pd.read_excel('%s'%files[i],header=5)
            if(section.sectionList[0] != '# ユーザID'):  #複数グラフを作る場合、sectionリストの要素が減り続けるのを防ぐ
                section.sectionList.insert(0,'# ユーザID')
            try:
                df1=df[section.sectionList] #section.pyから列名のリストを取得
            except KeyError:
                df1=df[section.sectionList1] #section.pyから列名のリストを取得
            #excelをdataframe化したdf1とuseridが一致するものをdataframe型で抽出
            data=df1[df1['# ユーザID'].isin([userid])]

            #data(dataframe型)をlist化（２次元配列になってしまう）
            data2=data.values.tolist()

            #1次元配列に戻す
            data3=list(itertools.chain.from_iterable(data2))

            #配列の0番（userid）を削除
            del data3[0]

            #0をNoneに置き換える
            data4 = []
            for d in data3:
                if(d == 0):
                    data4.append(None)
                else:
                    data4.append(d)

            print(data4)

            list_data.append(data4)
        else: #データが存在しない場合
            list_data.append([None,None,None,None,None,None,None])
    print(list_data)
    output_graph(list_data,userid)
