import glob
def input_from_excel():
    files=[]
    path = '*期.xlsx'
    list1 = glob.glob(path)
    for l in list1:
        files.append(l)
    print(files)
    return(files)
#input_from_excel()
