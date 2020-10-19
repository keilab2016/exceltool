import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import os
import itertools

import glob
files=[]
path = '*.xlsx'
list1 = glob.glob(path);
kensaku = '期.xlsx'
for l in list1:
    if kensaku in l:
        files.append(l)

        #xlsx内のすべての学籍番号(重複削除済)が格納してあるlistを作成
list_usr=[]
for i, j in enumerate(files):
    list_usr_1=pd.read_excel('%s'%files[i],header=5)
    list_usr_2=list_usr_1['# ユーザID'].values.tolist()
    list_usr += list_usr_2
list_usr_unique = list(set(list_usr))

data_height=[]
for i, j in enumerate(files):
    df=pd.read_excel('%s'%files[i],header=5)
    df=df[['# ユーザID','１．システム情報科学に関する高い専門能力（コース共通）',
 '１．システム情報科学に関する高い専門能力（コース専門能力）',
 '１．システム情報科学に関する高い専門能力（卒業研究）',
 '２．研究的態度を支える問題探究力・構想力',
 '３．共創のための情報表現能力・チームワーク力',
 '４．自律的に学び続けるためのメタ学習力',
 '５．専門家として持つべき人間性']]
        #df形式でidと一致した学生を抽出
    data=df[df['# ユーザID']==df_usr_unique[1]]
        #list化するがこの時、2次元配列になっている
    data2=data.values.tolist()
        #1次元配列に戻す
    data3=list(itertools.chain.from_iterable(data2))
        #配列の0番（userid）を削除
    del data3[0]
    data_height.append(data3)

    # グラフの描画先の準備
    fig = plt.figure(figsize=(35,10), dpi=100)
    left = ['１．システム情報科学に関する高い専門能力（コース共通）',
     '１．システム情報科学に関する高い専門能力（コース専門能力）',
     '１．システム情報科学に関する高い専門能力（卒業研究）',
     '２．研究的態度を支える問題探究力・構想力',
     '３．共創のための情報表現能力・チームワーク力',
     '４．自律的に学び続けるためのメタ学習力',
     '５．専門家として持つべき人間性']
    #折れ線グラフ
    plt.ylim(0,7)
    p1=plt.plot(left, data3, marker="D", markersize=12, markeredgewidth=3, markeredgecolor="blue",
      markerfacecolor="lightblue")
    p2=plt.plot(left, ndata3, marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",
      markerfacecolor="peru")
    plt.title("This is a title")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.rcParams['axes.axisbelow'] = True
    plt.legend((p1[0], p2[0]), ("201909_後期", "202004_前期"), loc=4 ,fontsize=40 ,prop={'size':20})
    # 作成したチャートを画像出力
    fig.savefig('graph.png')
    # 出力したgraph.pngをout.xlsxに貼り付ける
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    img = openpyxl.drawing.image.Image('graph.png')
    ws.add_image(img, 'B12')
    wb.save('out.xlsx')
    plt.close()
