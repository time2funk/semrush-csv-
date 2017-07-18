
import csv
reader = csv.reader(f)
for row in reader:
	length = len(row)
	for i in row
		# ...

import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
path = "filter"
mydir = listdir(path)
filesNames = filter(lambda x: x.endswith('.csv'), mydir)
print filesNames
file = open( joinpath( mypath,str(i) ), "r")


file = open( joinpath( mypath,str(i) ), "r")
unique_list = list(set(file)-set(unique_list))


import pandas as pd
df = pd.read_csv(csv_file)
df = pd.read_csv(filename, usecols=['col1', 'col3', 'col7'])
# you can also use df['column_name']
tmp = tmp.merge(df,on=['Keyword'],how='left')
df = df.append(tmp)
df.drop_duplicates('Keyword',keep='first',inplace=True)
df.to_csv('result/uniqlist.csv', sep=',', encoding='utf-8')


import xlrd
workbook = xlrd.open_workbook('my_file_name.xls')
# кодировка
workbook = xlrd.open_workbook('my_file_name.xls', encoding='cp1252')
# который загружает только текущие листы в память
workbook = xlrd.open_workbook('my_file_name.xls', on_demand = True)
# открытие листа
worksheet = workbook.sheet_by_name('My_Sheet_Name')
worksheet = workbook.sheet_by_index(0)
# возвращает количество листов
workbook.sheet_names()
# Получение данных из ячеек
worksheet.cell(0, 0).value
if worksheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something


for path,dirs,files in os.walk('data/'):
	for f in files:
	    fname = os.path.join(path,f)
	    assert(os.path.exists(fname))


output = open('result/uniqlist.csv', "w");
for i in unique_list: 
	output.write(str(i))
output.close()


for i in filesNames:
    if isfile(joinpath(mypath,i)):
        print i