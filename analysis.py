import pandas as pd
import seaborn as sns
data=pd.read_csv(r"C:\Users\SAMARTH G VASIST\Desktop\pes\gender-classifier-DFE-791531.csv", encoding='latin-1')
print(data)
data.loc[1,"name"]=None
print(data.loc[1,"name"])
print(data.columns)
newdata=data.drop(['_golden','_unit_state','_trusted_judgments','_last_judgment_at','gender_gold','profile_yn_gold'],axis=1,)
print(len(newdata.columns))
print(newdata.isnull().sum())
print(newdata["fav_number"].mean(axis=0, skipna=True))
#sns.heatmap(newdata.isnull(),yticklabels=False, cmap="viridis")
def setnan(cols):
     tweet_count=cols[0];
     return None
#data['Age'] = data[['Age','Pclass']].apply(impute_age,axis=1) 
d=newdata[['tweet_count']].apply(setnan,axis=1)

d=newdata[[]]
#print(d)
print(d.isna())
newdata.drop(['tweet_count'], axis=1, inplace=True)
newdata=pd.concat([newdata,d],axis=1)
newdata.rename(columns={0:'tweetcounts'}, inplace=True)
print(newdata.isnull().sum())
y=newdata.iloc[[1,3],:]
print(y)
print(y['tweet_count'])
    
newdata.to_csv("file1.csv")