import glob
def input_from_excel():
    files=[]
    path = 'Templete/*期.xlsx'
    list1 = glob.glob(path)
    for l in list1:
        files.append(l)
    files=sorted(files)
    print(files)
    return(files)
#input_from_excel()
