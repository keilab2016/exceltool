import openpyxl
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']
from PIL import Image

def make_plt(flist,number,list_two,userid):

    # グラフの初期設定
    fig = plt.figure(figsize=(6.5,2.6), dpi=200)
    X_label = flist
    #print(X_label)
    plt.rcParams["font.size"] = 15
    plt.ylim(0,7.5)
    plt.yticks([1,3,5,7])

    # データの整形?!(Noneの場合は描画しないようにする)
    arrenged_number = []
    for n in number: 
        if(n == None):
            arrenged_number.append(np.nan)
        else:
            arrenged_number.append(n)

    # グラフの描画
    plt.grid(True)
    p = plt.plot(X_label,arrenged_number,linewidth = 2,marker="o", markersize=9,markerfacecolor="orange")
    plt.xticks(X_label, rotation="30")
    plt.tight_layout()
    plt.rcParams['axes.axisbelow']
    # 作成したチャートを画像出力
    fig.savefig('image/%s_%d.png'%(userid,list_two))#カレントディレクトリに「学籍番号_num.png」を保存

    img = openpyxl.drawing.image.Image('image/%s_%d.png'%(userid,list_two))
    img.width = 625
    img.height = 250

    plt.close()
    return img
