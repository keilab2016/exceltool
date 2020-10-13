#python3で実行すること
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image

#対象となるxlsxファイルの名前を入れる
name= "201909_後期"
df2 = pd.read_excel('%s.xlsx'%name,header=5)
df2.to_csv('%s.csv'%name)
df2_2 = pd.read_csv('%s.csv'%name)

#本当は、動的にしたい（指定したpass内にあるxlsxファイルの分だけのdfを作成したい）↓エラー
#import os
#directory = os.listdir('/Users/ryuumamatsuo/excel_job/*.xlsx')
#data=[]
#for file_name in directory:
#data.append(pd.read_excel('%s.xlsx'%file_name))

headertitle=list(df2_2.columns)

#削除したいカラム名を抽出
headertitle_in = [s for s in headertitle if 'Unnamed' in s]

#条件にマッチしたcolumnsを削除
data_frame = df2_2.drop(columns=headertitle_in)

#excel化してカレントディレクトリに保存
data_frame.to_excel('%s_ver2.xlsx'%name)

df_new = pd.read_excel('%s_ver2.xlsx'%name)
df3=df_new[['１．システム情報科学に関する高い専門能力（コース共通）',
 '１．システム情報科学に関する高い専門能力（コース専門能力）',
 '１．システム情報科学に関する高い専門能力（卒業研究）',
 '２．研究的態度を支える問題探究力・構想力',
 '３．共創のための情報表現能力・チームワーク力',
 '４．自律的に学び続けるためのメタ学習力',
 '５．専門家として持つべき人間性',]]

 #↑の０行目を取得
data=df3.iloc[0,[0,1,2,3,4,5,6]].tolist()

# グラフの描画先の準備
fig = plt.figure(figsize=(40,10), dpi=100)
left = np.array(['１．システム情報科学に関する高い専門能力（コース共通）',
 '１．システム情報科学に関する高い専門能力（コース専門能力）',
 '１．システム情報科学に関する高い専門能力（卒業研究）',
 '２．研究的態度を支える問題探究力・構想力',
 '３．共創のための情報表現能力・チームワーク力',
 '４．自律的に学び続けるためのメタ学習力',
 '５．専門家として持つべき人間性'])
height=np.array(data)
#棒グラフのxlabel 中央に表示
plt.bar(left, height, align="center")
# 作成したチャートを画像出力
fig.savefig('graph.png')
# 出力したgraph.pngをout.xlsxに貼り付ける
wb = openpyxl.Workbook()
ws = wb.worksheets[0]
img = openpyxl.drawing.image.Image('graph.png')
ws.add_image(img, 'B12')
wb.save('out.xlsx')
plt.close()
