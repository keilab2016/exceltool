import openpyxl
import section
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math

def make_plt(number,title,list_two,userid):
    #グラフの出力場所（セル番号）
    cell_num=[8,23,38,4,19,34,49]

    fig = plt.figure(figsize=(15,5), dpi=100)
    X_label = ['年度1',
            '年度2',
            '年度3',
            '年度4',
            '年度5',
            '年度6',
            '年度7']
    plt.ylim(0,9)
    p = plt.plot(X_label,number,marker="D", markersize=12, markeredgewidth=3, markeredgecolor="peru",markerfacecolor="peru")
    #plt.title(title)
    plt.xlabel("年度")
    plt.ylabel("スコア")
    plt.rcParams['axes.axisbelow']
    # 作成したチャートを画像出力
    fig.savefig('%s_%d.png'%(userid,list_two))#カレントディレクトリに「学籍番号_num.png」を保存
    wb = openpyxl.Workbook()
    ws = wb.active
    # ws = wb.worksheets[0]
    img = openpyxl.drawing.image.Image('%s_%d.png'%(userid,list_two))
    img.width = 72 * 7
    img.height = 25 * 10
    if list_two < 3:

        row_number = cell_num[list_two]
        cell = ws.cell(row=row_number, column=3).coordinate#セルの位置を指定（column=3はC列のこと
        img.anchor = cell
        ws.add_image(img)
        #ws.add_image(img,'C%d'%cell_num[num])
    else:
        
        row_number = cell_num[list_two]
        cell = ws.cell(row=row_number, column=15).coordinate
        img.anchor = cell
        ws.add_image(img)
        #ws.add_image(img,'O%d'%cell_num[num])
    wb.save('%s.xlsx'%userid)# output.pyで出力した.pngをout.xlsxに貼り付ける
    plt.close()
