#python3で実行すること
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools

#対象となるxlsxファイルの名前を入れる
name= "201909_後期"
df = pd.read_excel('%s.xlsx'%name,header=5)
#本当は、動的にしたい（指定したpass内にあるxlsxファイルの分だけのdfを作成したい）↓エラー
#import os
#directory = os.listdir('/Users/ryuumamatsuo/excel_job/*.xlsx')
#data=[]
#for file_name in directory:
#data.append(pd.read_excel('%s.xlsx'%file_name))
df=df[['# ユーザID','１．システム情報科学に関する高い専門能力（コース共通）',
 '１．システム情報科学に関する高い専門能力（コース専門能力）',
 '１．システム情報科学に関する高い専門能力（卒業研究）',
 '２．研究的態度を支える問題探究力・構想力',
 '３．共創のための情報表現能力・チームワーク力',
 '４．自律的に学び続けるためのメタ学習力',
 '５．専門家として持つべき人間性',]]
userid = df['# ユーザID'].unique().tolist()
 #df形式でidと一致した学生を抽出
data=df[df['# ユーザID']==userid[0]]
#list化するがこの時、2次元配列になっている
data2=data.values.tolist()
#1次元配列に戻す
data3=list(itertools.chain.from_iterable(data2))
#配列の0番（userid）を削除
del data3[0]

#「202004_前期」から同じ学生のデータを読み込んで、同じ学生を一つのファイルに出力するための読み込み
#↑とファイル名の書き方変えてる
ndf = pd.read_excel('202004_前期.xlsx',header=5)
ndf=ndf[['# ユーザID','１．システム情報科学に関する高い専門能力（コース共通）',
 '１．システム情報科学に関する高い専門能力（コース専門能力）',
 '１．システム情報科学に関する高い専門能力（卒業研究）',
 '２．研究的態度を支える問題探究力・構想力',
 '３．共創のための情報表現能力・チームワーク力',
 '４．自律的に学び続けるためのメタ学習力',
 '５．専門家として持つべき人間性',]]
ndata=ndf[ndf['# ユーザID']==userid[0]]
ndata2=ndata.values.tolist()
ndata3=list(itertools.chain.from_iterable(ndata2))
del ndata3[0]

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
