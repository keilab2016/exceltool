import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math


def output_graph(list_data): #list_dataに入れたいデータ
    fig = plt.figure(figsize=(35,10), dpi=100)
    left = ['１．システム情報科学に関する高い専門能力（コース共通）',
         '１．システム情報科学に関する高い専門能力（コース専門能力）',
         '１．システム情報科学に関する高い専門能力（卒業研究）',
         '２．研究的態度を支える問題探究力・構想力',
         '３．共創のための情報表現能力・チームワーク力',
         '４．自律的に学び続けるためのメタ学習力',
         '５．専門家として持つべき人間性']
    X_label = ['年度1',
            '年度2',
            '年度3',
            '年度4',
            '年度5',
            '年度6',
            '年度7']
        #折れ線グラフ
    plt.ylim(0,9)
    graph_array = [[0 for j in range(7)] for j in range(7)]
    for list_two in range(7):
        for list_one in range(2):
            graph_array[list_two][list_one] = (list_data[list_one][list_two])#配列のxとyを逆転
            print(graph_array)#確認用
    p0=plt.plot(X_label, graph_array[0], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="blue",markerfacecolor="lightblue")
    p1=plt.plot(X_label, graph_array[1], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    p2=plt.plot(X_label, graph_array[2], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    p3=plt.plot(X_label, graph_array[3], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    p4=plt.plot(X_label, graph_array[4], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    p5=plt.plot(X_label, graph_array[5], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    p6=plt.plot(X_label, graph_array[6], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")#各カテゴリごとに，今後グラフ化の関数とか作りたい，ここの書き方がダサい
    plt.title("b1018336")
    plt.xlabel("年度")
    plt.ylabel("スコア")
    plt.rcParams['axes.axisbelow'] = True
    plt.legend((p0[0],p1[0], p2[0], p3[0],p4[0],p5[0],p6[0]), left, loc=4 ,fontsize=40 ,prop={'size':20})
        # 作成したチャートを画像出力
    fig.savefig('b1018336.png')#titleのために学籍番号を渡して欲しい...
        # 出力したgraph.pngをout.xlsxに貼り付ける
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    img = openpyxl.drawing.image.Image('b1018336.png')
    ws.add_image(img, 'B12')
    wb.save('out.xlsx')
