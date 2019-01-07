
import pandas as pd

def change_unq_key(key_col,var,i):
    return (str(key_col)+"_"+var+"_"+i)

def modify_rec(var,array):
    global df_orig    
    df_temp=df_orig.copy()
    df_new=df_orig.copy()
    for i in array:
        df_app=df_temp.copy()
        df_app[var]=i
        df_app['Var1'] = df_app.apply(lambda x: change_unq_key(x['Var1'],var,i), axis=1)
        pieces = (df_new,df_app)
        df_new=pd.concat(pieces, ignore_index = True)
    df_orig=df_new.copy()    
    #End Function modify_rec
    
    
    

    
df_orig=pd.read_csv('C:\\Users\\avinash\\Documents\\input_file.csv', dtype=object)

modify_rec('var1',['0','1'])
modify_rec('var2',['Y','N'])

df_orig.to_csv('C:\\Users\\avinash\\Documents\\out_file.csv')
