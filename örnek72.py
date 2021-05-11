import pandas as pd
df=pd.read_csv('matlab 2018\IMDB_Bottom250movies2_OMDB_Detailed.csv')
result=df
#print(result)
#result=df.columns #burda oluşan csv uzantısını dataframe olarak yaptıktan sonra sütün bilgilerini istedim
result=df.info #burda oluşan csv uzantısını dataframe olarak yaptıktan sonra genel  bilgilerini istedim
#oluşan dataframedaki csv uzantısının ilk 5 kaydını ?
result=df.head()
print(result)