from input import input_from_excel
from input import input_path
from output import output_graph
import numpy as np
import pandas as pd
import section
import itertools
import sys
import openpyxl
import os
import re

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
    userid=re.sub(r'^b','',args_list[a])
    admission_year="20"+userid[2:4]
    print(admission_year)
    list_data=[]
    #指定ディレクトリのexcelファイル名をlist型で取得
    files = input_from_excel()

    flist = []
    for i, j in enumerate(files):
        if(files[i]!=''): #20〇〇年○期のデータが存在する場合
            fname = files[i].replace(input_path,'')
            fname = fname.replace('_回答データ','')
            print(fname)
            if fname.endswith('.xlsx'):
                flist.append(fname.replace('.xlsx',''))
                df=pd.read_excel('%s'%files[i])
            else:
                flist.append(fname.replace('.xls',''))
                df=pd.read_excel('%s'%files[i],header=5)
            try:
                secList=section.sectionList.copy()
                df1=df[secList] #section.pyから列名のリストを取得
                #excelをdataframe化したdf1とuseridが一致するものをdataframe型で抽出
                data=df1[df1['ユーザ名'].isin(['b' + userid])]
            except KeyError:
                secList=section.sectionList1.copy()
                df1=df[secList] #section.pyから列名のリストを取得
                #excelをdataframe化したdf1とuseridが一致するものをdataframe型で抽出
                data=df1[df1['# ユーザID'].isin(['b' + userid])]

            #data(dataframe型)をlist化（２次元配列になってしまう）
            data2=data.values.tolist()

            #1次元配列に戻す
            data3=list(itertools.chain.from_iterable(data2))

            data4 = []
            if len(data3)==0:
                data4 = [np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
            else:
                #配列の0番（userid）を削除
                del data3[0]
                #0をNoneに置き換える
                for d in data3:
                    if(d == 0):
                        data4.append(None)
                    else:
                        data4.append(d % 8)

            print(data4)

            list_data.append(data4)
        #else: #データが存在しない場合
        #    list_data.append([None,None,None,None,None,None,None])
    print(flist,list_data)
    output_graph(flist,list_data,userid,secList)
