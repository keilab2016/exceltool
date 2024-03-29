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
import copy
import xlrd

#ディレクトリが存在していなければ作成
if(os.path.exists('image') == False):
    os.mkdir('image')

if(os.path.exists('output') == False):
    os.mkdir('output')
 
# コマンド引数から学籍番号(複数)を取得
args = sys.argv
targets=[]
year=9999;
for a in range(1,len(args)):
    userid=re.sub(r'^b','',args[a])
    targets.append(userid.rstrip())
    if userid.startswith('10'):
        n = int(userid[0:4])
        year = min(year, n + 1000)

# アンケート回答データの読み込み
exceldata={}
flist=[]
for path in input_from_excel(year):
    fname = path.replace(input_path,'')
    #fname = fname.replace('_回答データ','')
    if fname.endswith('.xlsx'):
        # Moodle
        fname = fname[0:fname.find('_')] # ファイル名から _ 以降を削除
        flist.append(fname.replace('.xlsx',''))
        try:
            df=pd.read_excel('%s' % path)
            print('Moodle',path)
        except xlrd.biffh.XLRDError:
            print('Moodle',path,'Unsupported or Corrupt file')
    else:
        # manaba
        fname = fname[0:fname.find('_')] # ファイル名から _ 以降を削除
        flist.append(fname.replace('.xls',''))
        try:
            df=pd.read_excel('%s' % path, header=5)
            print('manaba',path)
        except xlrd.biffh.XLRDError:
            print('manaba',path,'Unsupported or Corrupt file')
    error=0
    try:
        df1=df[section.sectionList1] #section.pyから列名のリストを取得
    except KeyError:
        error=1
    if error!=0:
        error=0
        try:
            df1=df[section.sectionList2] #section.pyから列名のリストを取得
        except KeyError:
            error=1
    if error!=0:
        error=0
        try:
            df1=df[section.sectionList3] #section.pyから列名のリストを取得
        except KeyError:
            error=1
    if error!=0:
        print('アンケート回答データの読み込みエラー', fname)
    exceldata[fname]=df1

# 学生毎にデータ抽出とグラフ出力
for userid in targets:
    print(userid, flush=True)
    list_data=[]
    for fname in exceldata:
        df1=copy.deepcopy(exceldata[fname])
        if 'ユーザ名' in df1:
            data=df1[df1['ユーザ名'].isin(['b' + userid])]
        else:
            data=df1[df1['# ユーザID'].isin(['b' + userid])]

        #data(dataframe型)をlist化（２次元配列になってしまう）
        if data.empty:
            data3=[]
        else:
            data3=data.values.tolist()[0]

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

        #print(data4)

        list_data.append(data4)
    output_graph(flist,list_data,userid)
