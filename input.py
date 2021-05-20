import os

input_path='Templete/'

def input_from_excel(): #入学年を取得し、読み込むデータを決定
    files=[]
    last_files=[]
    for f in os.listdir(input_path):
        if '卒業' in f:
            last_files.append(input_path + f)
        else:
            files.append(input_path + f)
    if len(last_files) > 0:
        files.append(last_files[len(last_files)-1])
    return(files)
