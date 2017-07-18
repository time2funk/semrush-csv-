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
path = "uploads"
cols = ['Keyword','Search Volume','Keyword Difficulty Index']
# 
# 
def filtr(name, array):
	f = str(joinpath( path, name ))
	df = pd.read_csv( f, usecols = array )
	print df
	print type(df)
	return df
#
# 
# 
# 
mydir = listdir(path)
filesNames = filter(lambda x: x.endswith('.csv'), mydir)
print filesNames


if len(filesNames) > 0:

	for file in filesNames:

		df = filtr( file, cols )

		new_file = joinpath( 'filter', file )
		df.to_csv(new_file, sep=',', encoding='utf-8')


print "finish"
# 
# END
# 