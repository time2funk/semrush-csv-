# 
# pointer file unique parser
# 
import pandas as pd
# file work
import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath

# 
# 
path = "filter"
cols = ['Keyword','Search Volume','Keyword Difficulty Index']
# 
# 
mydir = listdir(path)
filesNames = filter(lambda x: x.endswith('.csv'), mydir)
print filesNames


if len(filesNames) > 1:
	
	for name in filesNames:
		f = str(joinpath( path, name ))
		
		if filesNames.index(name) == 0:
			df = pd.read_csv( f )
		else:
			tmp = pd.read_csv( f )
			tmp = tmp.merge(df,on=cols,how='left')
			df = df.append(tmp)
		print "up"

	df.drop_duplicates(cols,keep='first',inplace=True)
	df.to_csv('result/keywords.csv', index=False, sep=',', columns=cols, index_label=False, encoding='utf-8')
	# df_new = pd.read_csv('file_name.csv').drop(['unnamed 0'],axis=1)
print "finish"
# 
# END
# 
