import openpyxl
import section
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image
import itertools
import math
from make_plt import make_plt 

def output_graph(flist,list_data,userid):
    num = len(list_data)

    graph_array = [[0 for j in range(num)] for j in range(7)]
    for list_two in range(7):
        for list_one in range(num):
            graph_array[list_two][list_one] = (list_data[list_one][list_two])#配列のxとyを逆転
        
        make_plt(flist,graph_array[list_two],list_two,userid)
