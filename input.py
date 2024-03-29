import os

input_path='Templete/'

def input_from_excel(year): #入学年を取得し、読み込むデータを決定
    files=[]
    last_files=[]
    for f in sorted(os.listdir(input_path)):
        if os.path.isfile(input_path + f) and not f.startswith('.'):
            n = int(f[0:4])
            if n >= year:
                if '卒業' in f:
                    last_files.append(input_path + f)
                else:
                    files.append(input_path + f)
    if len(last_files) > 0:
        files.append(last_files[len(last_files)-1])
    return(files)
