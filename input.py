import glob
import label_year 
year_list = []
term_list = ["04_前期", "09_後期"]
x_list_data = []
def make_year_list(admission_year):
    year_list.clear()
    x_list_data.clear()
    year = int(admission_year)
    for i in range(8):
        year_list.append(year)
        if((i+1) % 2 == 0):
            year = year + 1
            x_list_data.append(str(year_list[i]) + "年後期")
        else:
            x_list_data.append(str(year_list[i]) + "年前期")
    x_list_data.append(str(year) + "年卒業")
    label_year.x_list = x_list_data



def input_from_excel(): #入学年を取得し、読み込むデータを決定
    print(year_list)
    print(label_year.x_list)
    files=[]
    for i in range(8):
        if((i+1) % 2 == 0):
            path = 'Templete/' + str(year_list[i]) + term_list[1] + '.xlsx'
        else:
            path = 'Templete/' + str(year_list[i]) + term_list[0] + '.xlsx'

        print("path= " + path)
        data = glob.glob(path)
        if(data != []):
            files.append(data[0])
        else:
            files.append("")
    
    path = 'Templete/' + str(year_list[7] + 1) + '03_卒業.xlsx'
    data = glob.glob(path)
    print("path= " + path)
    if(data != []):
        files.append(data[0])
    else:
        files.append("")

    #files=sorted(files)
    print(files)
    return(files)
#input_from_excel()
