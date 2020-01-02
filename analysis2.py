import pandas as pd
import seaborn as sns
import random
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\SAMARTH G VASIST\Desktop\pes\gender-classifier-DFE-791531.csv", encoding='latin-1')
print(data)
newdata=data.drop(['_golden','_unit_state','_trusted_judgments','_last_judgment_at','gender_gold','profile_yn_gold'],axis=1,)
sampled=newdata.sample(n=500)
print(sampled)

#sns.countplot(x="gender",data=sampled)
#sns.countplot(x="profile_yn",data=sampled)
#plt.boxplot(sampled["tweet_count"])
#sns.heatmap(sampled.isnull(),yticklabels=False,cmap="viridis")
#sns.boxplot(x="gender",y="tweet_count",data=data)
a=[]
for i in range(1,501):
     a.append(i)
sampled.index=a     
print(sampled.index)
print(sampled)
c=[]
print(sampled["tweet_count"])
for i in range(1,51):
    x=random.randint(1,500)
    while(x in c):
   
      x=random.randint(1,500)
    
    print(x)
    sampled.loc[x,"tweet_count"]=None 
    c.append(x)
print(sampled['tweet_count'].isnull())  

c=[]
for i in range(1,15):
    x=random.randint(1,500)
    while(x in c):
   
      x=random.randint(1,500)
    
    print(x)
    sampled.loc[x,"gender"]=None 
    c.append(x)

c=[]
#print(sampled["tweet_count"])
for i in range(1,51):
    x=random.randint(1,500)
    while(x in c):
   
      x=random.randint(1,500)
    
    print(x)
    sampled.loc[x,"fav_number"]=None 
    c.append(x)
#print(sampled['tweet_count'].isnull()) 
print(sampled.isnull().sum())
#sns.heatmap(sampled.isnull(),yticklabels=False,cmap="viridis")  

print(sampled.isnull().sum())  
sampled.to_csv("deletedsample.csv")
  

fav_mean=sampled["fav_number"].mean(axis=0, skipna=True)
print(fav_mean)

tweet_mean=sampled["tweet_count"].mean(axis=0, skipna=True)
print(tweet_mean)
"""def setmean(cols):
      tc=cols[0]
      if pd.isnull(tc):
         return tweet_mean

sampled['tweet_count']=sampled[['tweet_count']].apply(setmean,axis=1)"""
for i in range(1,501):
    print(i)
    if pd.isnull(sampled.loc[i,'tweet_count']):
        
        sampled.loc[i,'tweet_count']=tweet_mean

for i in range(1,501):
    print(i)
    if pd.isnull(sampled.loc[i,'fav_number']):
        
        sampled.loc[i,'fav_number']=fav_mean

#sns.heatmap(sampled.isnull(),yticklabels=False,cmap="viridis")
print(sampled["tweet_count"])
print(sampled.isnull().sum())  
print(sampled['gender'].value_counts())

t_min=(sampled['tweet_count'].min())    
t_max=(sampled['tweet_count'].max())    
t_range=t_max-t_min
c=[]
for i in range(1,15):
    x=random.randint(1,500)
    while(x in c):
   
      x=random.randint(1,500)
    
    print(x)
    sampled.loc[x,"gender"]=None 
    c.append(x)
print(sampled.isnull().sum())  

print(sampled['gender'].value_counts())
for i in range(1,501):
    if sampled.loc[i,"gender"]!="male" and sampled.loc[i,"gender"]!="female" and sampled.loc[i,"gender"]!="brand" and sampled.loc[i,"gender"]!="unknown":
        sampled.loc[i,"gender"]=sampled['gender'].value_counts().index[0]
        
print(sampled.isnull().sum())

print(sampled['gender'])
for i in range(1,501):
   if sampled.loc[i,"gender"]=="male":
       sampled.loc[i,"gender"]=1
   elif sampled.loc[i,"gender"]=="female":
       sampled.loc[i,"gender"]=0
   elif sampled.loc[i,"gender"]=="brand":
       sampled.loc[i,"gender"]=2
   elif sampled.loc[i,"gender"]=="unknown":
       sampled.loc[i,"gender"]=3

print(sampled['gender'])


#sns.countplot(x="gender",data=sampled)

#plt.scatter(sampled["_unit_id"],sampled["tweet_count"])
print(sampled.isnull().sum())
#sns.heatmap(sampled.isnull(),yticklabels=False,cmap="viridis")

counts=[]
favs=[]
for i in range(1,501):
    counts.append(sampled.loc[i,'tweet_count'])
    favs.append(sampled.loc[i,'fav_number'])
print(counts)
counts.sort()
favs.sort()
print(favs)

m=[]
for i in range(1,501):
    m.append(i)
print(m)
m=[(i-0.5)/500 for i in m]

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(counts, m)
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
import matplotlib.pyplot as plt
plt.scatter(counts,m,color="r")
yfit = [a + b * xi for xi in counts]
plt.plot(counts, yfit)

    

"""k=[]
for i in range(1,len(counts)+1):
    k.append(i)
print(k)"""    
fav_min=(sampled['fav_number'].min())    
fav_max=(sampled['fav_number'].max())    
fav_range=fav_max-fav_min
k=[(i-fav_mean)/500 for i in favs]
l=[(i-fav_min)/fav_range for i in favs]
print(l)

#plt.scatter(counts,k)
#plt.show()

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(favs, l)
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
import matplotlib.pyplot as plt
plt.scatter(favs,l,color="r")
yfit = [a + b * xi for xi in favs]
plt.plot(favs, yfit)

a, b = best_fit(favs, k)
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
import matplotlib.pyplot as plt
plt.scatter(favs,k,color="r")
yfit = [a + b * xi for xi in favs]
plt.plot(favs, yfit)





k=[(i-tweet_mean)/500 for i in counts]
l=[(i-t_min)/t_range for i in counts]
print(l)

#plt.scatter(counts,k)
#plt.show()

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# solution
a, b = best_fit(counts, l)
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
import matplotlib.pyplot as plt
plt.scatter(counts,l,color="r")
yfit = [a + b * xi for xi in counts]
plt.plot(counts, yfit)

a, b = best_fit(counts, k)
#best fit line:
#y = 0.80 + 0.92x

# plot points and fit line
import matplotlib.pyplot as plt
plt.scatter(counts,k,color="r")
yfit = [a + b * xi for xi in counts]
plt.plot(counts, yfit)











sampled.to_csv("cleanedsample.csv")
