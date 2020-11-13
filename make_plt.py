import openpyxl
import section
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math

def make_plt(number,title,cell_width):
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
    plt.title(title)
    plt.xlabel("年度")
    plt.ylabel("スコア")
    plt.rcParams['axes.axisbelow']
    file_path = 'b1018336' + title + '.png'
    fig.savefig(file_path)
    
    wb = openpyxl.Workbook()
    ws = wb.worksheets[0]
    img = openpyxl.drawing.image.Image(file_path)
    cell_image = 'B' + str(cell_width)
    ws.add_image(img,cell_image)
    wb.save('out_test.xlsx')
