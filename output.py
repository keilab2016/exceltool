import openpyxl
import section
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math


def output_graph(list_data,userid):
    #title = section.sectionList.pop(0)
    #left = section.sectionList
    #print(title)
    print(userid)

    #グラフの出力場所（セル番号）
    cell_num=[8,23,38,4,19,34,49]

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
    for num ,num2 in enumerate(X_label):
        fig = plt.figure(figsize=(35,10), dpi=100)
        p0=plt.plot(X_label, graph_array[num], marker="D", markersize=12, markeredgewidth=3, markeredgecolor="blue",markerfacecolor="lightblue")
        #plt.title("%s"%userid)
        plt.xlabel("年度")
        plt.ylabel("スコア")
        plt.rcParams['axes.axisbelow'] = True
        #plt.legend((p0[num]), left, loc=4 ,fontsize=40 ,prop={'size':20})

        # 作成したチャートを画像出力
        fig.savefig('%s_%d.png'%(userid,num))#カレントディレクトリに「学籍番号_num.png」を保存
        wb = openpyxl.Workbook()
        ws = wb.active
        # ws = wb.worksheets[0]
        img = openpyxl.drawing.image.Image('%s_%d.png'%(userid,num))
        img.width = 72 * 7
        img.height = 25 * 10
        if num < 3:
            row_number = cell_num[num]
            cell = ws.cell(row=row_number, column=3).coordinate#セルの位置を指定（column=3はC列のこと
            img.anchor = cell
            ws.add_image(img)
            #ws.add_image(img,'C%d'%cell_num[num])
        else:
            row_number = cell_num[num]
            cell = ws.cell(row=row_number, column=15).coordinate
            img.anchor = cell
            ws.add_image(img)
            #ws.add_image(img,'O%d'%cell_num[num])
        wb.save('%s.xlsx'%userid)# output.pyで出力した.pngをout.xlsxに貼り付ける
        plt.close()
