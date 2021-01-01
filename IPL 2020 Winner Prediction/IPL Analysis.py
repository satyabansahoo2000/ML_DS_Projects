#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


# In[84]:


matches = pd.read_csv("data/Training Matches IPL 2008-2019.csv")
test = pd.read_csv("data/Testset Matches IPL 2020.csv")

matches.shape, test.shape


# In[85]:


matches.head()


# In[86]:


matches.describe().T


# In[87]:


matches.isnull().sum()


# In[88]:


matches.drop(["id", "season", "date", 
              "toss_winner", "toss_decision", "result", "dl_applied",
             "win_by_runs", "win_by_wickets", "umpire3"], 
             axis=1, inplace=True)


# In[90]:


matches.city.unique()


# **Bengaluru** and **Bangalore** are both same city, so changing the name.

# In[91]:


matches.replace("Bangalore","Bengaluru", inplace=True)


# In[92]:


matches.loc[matches.city.isnull()]


# In[93]:


# Filling all the missing values of city with Dubai
matches.city.fillna("Dubai", inplace=True)


# In[94]:


# Printing all the team names
for i in matches['team1'].unique():
    print(i)


# In[95]:


# Changing the names of the teams
# Some teams changed their names too, so changing their names
matches.replace("Rising Pune Supergiant","Rising Pune Supergiants", inplace=True)
matches.replace('Pune Warriors', 'Rising Pune Supergiants', inplace=True)
matches.replace('Deccan Chargers', 'Sunrisers Hyderabad', inplace=True)
matches.replace('Delhi Daredevils', 'Delhi Capitals', inplace=True)

matches['team1'].unique()


# In[96]:


# Converting the names to the abbreviations
matches.replace({"Mumbai Indians":"MI", "Delhi Capitals":"DC", 
               "Sunrisers Hyderabad":"SRH", "Rajasthan Royals":"RR", 
               "Kolkata Knight Riders":"KKR", "Kings XI Punjab":"KXIP", 
               "Chennai Super Kings":"CSK", "Royal Challengers Bangalore":"RCB",
              "Kochi Tuskers Kerala":"KTK", "Rising Pune Supergiants":"RPS",
              "Gujarat Lions":"GL"}, inplace=True)
matches['team1'].unique()


# In[97]:


# Dropping the rows containing NaN values in winner column
matches.dropna(subset=["winner"], inplace=True)


# In[98]:


# Dropping the rows containing NaN values in umpire1 and umpire2 column
matches.dropna(subset=["umpire1","umpire2"], inplace=True)


# In[99]:


matches.isnull().sum()


# In[100]:


plt.figure(figsize=(12,8))
g = sns.countplot(x = "winner", data=matches, color='blue',
                 order = matches.winner.value_counts().index)
g.set_title("COUNT OF WINNER'S TEAM FROM 2008-2019", fontsize=25)
g.set_xlabel("WINNER", fontsize=15)
g.axes.get_yaxis().set_visible(False)
for p in g.patches:
    g.annotate(format(p.get_height(), '.0f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
plt.show()


# In[101]:


train = matches.copy()
train.head()


# In[102]:


# Removing the teams that are not playing in 2020
train.drop(train.loc[train.team1.isin(['KTK','RPS','GL'])].index, inplace=True)
train.drop(train.loc[train.team2.isin(['KTK','RPS','GL'])].index, inplace=True)


# In[103]:


# Converting to numerical values
train.replace({"MI":0,"CSK":1,"RCB":2,
              "KKR":3,"DC":4,"KXIP":5,
              "RR":6,"SRH":7}, inplace=True)


# In[104]:


# converting to numerical '1' where team1 is the winner 
# and '0' where team2 is the winner
train["winner"] = np.where(train["winner"] == train["team1"], 1, 0)


# In[105]:


#encoding to numeric values
from sklearn.preprocessing import LabelEncoder
encoder= LabelEncoder()

train["city"]=encoder.fit_transform(train["city"])
train["player_of_match"]=encoder.fit_transform(train["player_of_match"])
train["venue"]=encoder.fit_transform(train["venue"])
train["umpire1"]=encoder.fit_transform(train["umpire1"])
train["umpire2"]=encoder.fit_transform(train["umpire2"])


# In[106]:


# Correlation
corr = train.corr()
corr


# In[107]:


# Heatmap of correlation
mask = np.triu(corr)

plt.figure(figsize=(12,8))
sns.heatmap(corr,
           square=True,
            fmt=".1g",
            mask=mask,
           annot=True,
           cbar=False)
plt.show()


# Venue and team2 have the highest correlation for the **winner** column which shows this 2 features will contribute the most while predicting the winner.

# In[108]:


feature = train.drop('winner', axis=1)
target = train['winner']


# In[109]:


from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report


# In[110]:


#Splitting the data into training and testing data and scaling it
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(feature, target, 
                                                    test_size=0.3, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# In[111]:


#Logistic Regression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of logistic regression classifier on test set: {:.4f}'.format(logreg.score(X_test, y_test)*100))
print(70*"-")

# Gaussian Naive Bayes
NB = GaussianNB()
NB.fit(X_train, y_train)
y_pred = NB.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of logistic regression classifier on test set: {:.4f}'.format(NB.score(X_test, y_test)*100))
print(70*"-")

# Stochastic Gradient Descent
SGD = SGDClassifier(loss='modified_huber', shuffle=True, random_state=42)
SGD.fit(X_train, y_train)
y_pred = SGD.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of logistic regression classifier on test set: {:.4f}'.format(SGD.score(X_test, y_test)*100))
print(70*"-")

# K-Nearest Neighbours
KNN = KNeighborsClassifier(n_neighbors=15)
KNN.fit(X_train, y_train)
y_pred = KNN.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of logistic regression classifier on test set: {:.4f}'.format(KNN.score(X_test, y_test)*100))
print(70*"-")

#SVM
svm=SVC()
svm.fit(X_train,y_train)
svm.score(X_test,y_test)
y_pred = svm.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of SVM classifier on test set: {:.4f}'.format(svm.score(X_test, y_test)*100))
print(70*"-")

#Decision Tree Classifier
dtree=DecisionTreeClassifier()
dtree.fit(X_train,y_train)
dtree.score(X_test,y_test)
y_pred = dtree.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of decision tree classifier on test set: {:.4f}'.format(dtree.score(X_test, y_test)*100))
print(70*"-")

#Random Forest Classifier
randomForest= RandomForestClassifier(n_estimators=100)
randomForest.fit(X_train,y_train)
randomForest.score(X_test,y_test)
y_pred = randomForest.predict(X_test)
print("Confusion matrix\n",confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print('Accuracy of random forest classifier on test set: {:.4f}'.format(randomForest.score(X_test, y_test)*100))


# As **Random Forest Classifier** gives the more accuracy, we will go with **Random Forest Classifier**

# In[112]:


test.head()


# In[113]:


test_copy = test.copy()
test_copy.drop(["id", "season", "date", 
           "umpire3"], axis=1, inplace=True)


# In[114]:


test_copy.replace({"MI":0,"CSK":1,"RCB":2,
              "KKR":3,"DC":4,"KXIP":5,
              "RR":6,"SRH":7}, inplace=True)


# In[115]:


test_copy["city"]=encoder.fit_transform(test_copy["city"])
test_copy["player_of_match"]=encoder.fit_transform(test_copy["player_of_match"])
test_copy["venue"]=encoder.fit_transform(test_copy["venue"])
test_copy["umpire1"]=encoder.fit_transform(test_copy["umpire1"])
test_copy["umpire2"]=encoder.fit_transform(test_copy["umpire2"])


# In[116]:


pred = randomForest.predict(test_copy)
print(pred)

winner = list()
for i in range(len(pred)):
    if pred[i] == 0:
        winner.append(2)
    else:
        winner.append(1)


# In[117]:


submission = {"id":test.id.tolist(), 
              "winner":winner}
submit = pd.DataFrame(submission)

submit.to_csv("data/submit.csv", index=False)


# In[118]:


get_ipython().system('kaggle competitions submit -c winnerpredictionchallenge -f \'data/submit.csv\' -m ""')


# In[ ]:




