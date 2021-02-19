import os

input_path='Templete/'

def input_from_excel(): #入学年を取得し、読み込むデータを決定
    files=[]
    for f in os.listdir(input_path):
        files.append(input_path + f)
    print(files)
    return(files)
