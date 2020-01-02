import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# we'll want this for plotting
import matplotlib.pyplot as plt

# we'll want this for text manipulation
import re

# for quick and dirty counting
from collections import defaultdict

# the Naive Bayes model
from sklearn.naive_bayes import MultinomialNB
# function to split the data for cross-validation
from sklearn.model_selection import train_test_split
# function for transforming documents into counts
from sklearn.feature_extraction.text import CountVectorizer
# function for encoding categories
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

twigen=pd.read_csv(r"C:\Users\SAMARTH G VASIST\Desktop\pes\gender-classifier-DFE-791531.csv", encoding='latin-1')
print(twigen.head())

def normalize_text(s):
    # just in case
    s = str(s)
    s = s.lower()
    
    # remove punctuation that is not word-internal (e.g., hyphens, apostrophes)
    s = re.sub('\s\W',' ',s)
    s = re.sub('\W\s',' ',s)
    
    # make sure we didn't introduce any double spaces
    s = re.sub('\s+',' ',s)
    
    return s


print(twigen['text'])
twigen['text_norm'] = [normalize_text(s) for s in twigen['text']]
print(twigen['text'])
twigen['description_norm'] = [normalize_text(s) for s in twigen['description']]

gold_values = defaultdict(int)
for val in twigen._golden:
    gold_values[val] += 1
print(gold_values)

# what does the confidence look like?
print(len(twigen['gender:confidence']))
print(np.any(np.isnan(twigen['gender:confidence'])))
# we've got at least one NaN, so let's remove
gender_confidence = twigen['gender:confidence'][np.where(np.invert(np.isnan(twigen['gender:confidence'])))[0]]
print(len(gender_confidence))
gender_nonones = gender_confidence[np.where(gender_confidence < 1)[0]]
print(len(gender_nonones))


twigen_confident = twigen[twigen['gender:confidence']==1]
print(twigen_confident.shape)

print(twigen.columns)
# pull the data into vectors
print(twigen['text_norm'])
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(twigen_confident['text_norm'])
print(x)
print(x.shape)
print(type(x))


encoder = LabelEncoder()
y = encoder.fit_transform(twigen_confident['gender'])
print(y)
# split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# take a look at the shape of each of these
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)


nb = MultinomialNB()
nb.fit(x_train, y_train)

y_pred = nb.predict(x_test)
print(y_pred)
print(accuracy_score(y_test, y_pred))


print(nb.score(x_test, y_test))

cm = confusion_matrix(y_test, y_pred)

print(cm)

print(classification_report(y_test, y_pred))


twigen['all_features'] = twigen['text_norm'].str.cat(twigen['description_norm'], sep=' ')

twigen_confident = twigen[twigen['gender:confidence']==1]
#print(twigen['text_norm'])
# pull the data into vectors
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(twigen_confident['text_norm'])

encoder = LabelEncoder()
y = encoder.fit_transform(twigen_confident['gender'])

# split into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

nb = MultinomialNB()
nb.fit(x_train, y_train)

print(nb.score(x_test, y_test))




