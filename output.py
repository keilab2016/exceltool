import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools

def output_graph(data1,data2):
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
    data1 = list(itertools.chain.from_iterable(data1.values.tolist()));
    del data1[0]
    p1=plt.plot(left, data1,
                marker="D", markersize=12, markeredgewidth=3, markeredgecolor="blue",
                markerfacecolor="lightblue")
    data2 = list(itertools.chain.from_iterable(data2.values.tolist()));
    del data2[0]
    p2=plt.plot(left, data2,
                marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",
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
