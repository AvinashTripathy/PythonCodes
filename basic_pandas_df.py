import pandas as pd
import os
import xlsxwriter

in_dir="/avinash/indir"

file_in="Base_DS.csv"
file_out="Out_Base_DS.csv"

infile=pd.read_csv(os.path.join(in_dir,file_in),sep=',',dtype=object)
outfile = infile[infile["size"] != "1"]
outfile.to_csv(os.path.join(in_dir,file_out), sep=",",  header=True, index=False)
