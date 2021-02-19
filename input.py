import os
#import glob
#import label_year 
year_list = []
term_list = ["年度前期_回答データ", "年度後期_回答データ"]
#x_list_data = []
def make_year_list(admission_year):
    year_list.clear()
    #x_list_data.clear()
    year = int(admission_year)
    for i in range(8):
        year_list.append(year)
        if((i+1) % 2 == 0):
            year = year + 1
            #x_list_data.append(str(year_list[i]) + "年後期")
        #else:
        #    x_list_data.append(str(year_list[i]) + "年前期")
    #x_list_data.append(str(year) + "年卒業時")
    #label_year.x_list = x_list_data

input_path='Templete/'

def input_from_excel(): #入学年を取得し、読み込むデータを決定
    files=[]
    for f in os.listdir(input_path):
        files.append(input_path + f)
    print(files)
    return(files)
