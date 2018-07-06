# Ques1
import pandas as pd
data={'name':['akshita'],'age':[20],'mail_id':['akshitasharma01111@gmail.com'],'ph_no':[9813489211]}
df=pd.DataFrame(data)
print(df)
print(df.append({'name':'gourav sareen','age':20,'mail_id':'gouravsareen0112@gmail.com','ph_no':8708151150},ignore_index=True))



# Ques2
import pandas as pd
df1=pd.read_csv('Test.csv')
print(df1.head(5))
print(df1.head(10))
print(df1.sum(axis=0))
print(df1.sum(axis=1))
print(df1.mean(axis=0))
print(df1.mean(axis=1))
print(df1.describe())
print(df1.count())
print(df1.tail(5))
print(df1['Location'].sum())
print(df1['Location'].describe())
print("location occurs"+str(df1['Location'].count())+"times")
