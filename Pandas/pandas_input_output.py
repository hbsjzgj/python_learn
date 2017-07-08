import pandas as pd
'''
Format 
Type	Data Description	Reader	        Writer
text	CSV	                read_csv	    to_csv
text	JSON	            read_json	    to_json
text	HTML	            read_html	    to_html
text	Local clipboard	    read_clipboard	to_clipboard
binary	MS Excel	        read_excel	    to_excel
binary	HDF5 Format	        read_hdf	    to_hdf
binary	Feather Format	    read_feather	to_feather
binary	Msgpack	            read_msgpack	to_msgpack
binary	Stata	            read_stata	    to_stata
binary	SAS	                read_sas	 
binary	Python              Pickle Format	read_pickle	to_pickle
SQL	    SQL	                read_sql	    to_sql
SQL	    Google Big Query	read_gbq	    to_gbq
'''

data = pd.read_csv('student.csv',)
''' data
   student ID\tname\tage\tgender
0        1100\tKelly\t22\tFemale
1          1101\tClo\t21\tFemale
2        1102\tTilly\t22\tFemale
3           1103\tTony\t24\tMale
4          1104\tdavid\t20\tMale
5        1105\tCatty\t22\tFemale
6             1106\tM\t3\tFemale
7              1107\tN\t43\tMale
8              1108\tA\t13\tMale
9              1109\tS\t12\tMale
10         1110\tDavid\t33\tMale
11           1111\tDw\t3\tFemale
12             1112\tQ\t23\tMale
13           1113\tW\t21\tFemale
'''
data.to_pickle('student.pickle')
