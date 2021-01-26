import openpyxl
import section
import matplotlib.pyplot as plt
from openpyxl.styles.fonts import Font
import pprint
import label_year
import os
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math

def make_plt(number,title,list_two,userid):
    #グラフの出力場所（セル番号）
    cell_num=[9,24,39,5,20,35,50]

    fig = plt.figure(figsize=(15,5), dpi=100)
    X_label = label_year.year_list
    plt.ylim(1,7)
    p = plt.plot(X_label,number,marker="o", markersize=3)
    #plt.title(title)
    #plt.xlabel("年度")
    #plt.ylabel("スコア")
    plt.rcParams['axes.axisbelow']
    # 作成したチャートを画像出力
    fig.savefig('image/%s_%d.png'%(userid,list_two))#カレントディレクトリに「学籍番号_num.png」を保存
    user_check = userid
    if(os.path.isfile('output/%s.xlsx'%userid)):
        print("true")
        wb = openpyxl.load_workbook('output/%s.xlsx'%userid)
    else:
        print("false") 
        wb = openpyxl.load_workbook('output_Templete.xlsx')
    sheet = wb.worksheets[0]
    ws = wb.active
    # ws = wb.worksheets[0]
    img = openpyxl.drawing.image.Image('image/%s_%d.png'%(userid,list_two))
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
    sheet['B4'].font = Font(size=14)
    sheet['B4'] = '%sさん の学習達成度推移です。'%userid
    wb.save('output/%s.xlsx'%userid)# output.pyで出力した.pngをout.xlsxに貼り付ける
    plt.close()
