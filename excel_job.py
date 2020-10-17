from input import input_from_excel
from output import output_graph

df1 = input_from_excel("201909_後期.xlsx")
df2 = input_from_excel("202004_前期.xlsx")

userid = df1['# ユーザID'].unique().tolist()
data1=df1[df1['# ユーザID']==userid[0]]
data2=df2[df2['# ユーザID']==userid[0]]

output_graph(data1,data2)
