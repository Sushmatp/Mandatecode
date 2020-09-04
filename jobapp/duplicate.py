import pandas as pd 
xlsx = pd.ExcelFile("F://rlog//mandate attributes.xlsx")
df = pd.read_excel(xlsx, 'Sheet1')
df['is_duplicated'] = df.duplicated(['Job_ID','Company_ID'])
print(df['is_duplicated'])
print(df['is_duplicated'].sum())

df_nodup = df.loc[df['is_duplicated'] == True]
print(df_nodup)

df.drop_duplicates(subset=['Job_ID','Company_ID'],keep='first',inplace=True)
df['is_duplicated'] = df.duplicated(['Job_ID','Company_ID'])
print(df['is_duplicated'])
print(df['is_duplicated'].sum())

 