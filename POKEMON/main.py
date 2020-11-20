import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

def title(name):
    """Title of the Project

    Args:
        name (string): Name of the Title of the Project
    """
    st.text("")
    st.title(name)
    st.text("")

def clean_and_split(df):
    """Clean and Split the data into Train and Test Data

    Args:
        data (dataframes): DataFrame of the Pokemon Data
    """
    legendary_data = df[df['is_legendary'] == 1]
    normal_data = df[df['is_legendary'] == 0].sample(75)
    legendary_data.fillna(legendary_data.mean(), inplace=True)
    normal_data.fillna(normal_data.mean(), inplace=True)
    feature_list = ['weight_kg', 'height_m', 'sp_attack', 'attack',
                    'sp_defense','defense','speed','hp','is_legendary']
    sub_data = pd.concat([legendary_data, normal_data])[feature_list]
    X = sub_data.loc[:, sub_data.columns != 'is_legendary']
    Y = sub_data['is_legendary']
    X_train, X_test, y_train, y_test = train_test_split(X,Y, random_state=1, test_size=0.2, 
                                                        shuffle=True, stratify=Y)
    return X_train, X_test,y_train, y_test

st.title("IS THAT A LEGENDARY POKEMON???")
st.image('pic.jpg', width=600)
st.markdown('''
Photo By [Jie](https://unsplash.com/@imjma) on 
[Unsplash](https://unsplash.com/s/photos/pokemon)
''')

# Load the data
data = pd.read_csv('pokemon.csv')

# Summary
shape = data.shape
total = len(data)
legendary = len(data[data['is_legendary']==1])
non_legendary = total - legendary

# Sub-Headers
st.subheader('''
Number of Pokemons: {}'''.format(total))
st.subheader('''
Number of Legendary Pokemons: {}'''.format(legendary))
st.subheader('''
Number of Non-Legendary Pokemon: {}'''.format(non_legendary))

# Distribution of pokemon on the basis of TYPE
title('Legendary Pokemon Distribution based on Type')
legendary_data = data[data['is_legendary'] == 1]
fig1 = plt.figure()
ax = sns.countplot(data = legendary_data, x='type1',order=legendary_data['type1'].value_counts().index)
plt.xticks(rotation=45)
st.pyplot(fig1)

# Height and Weight Measurement of the Legendary and Non-Legendary Pokemon
title('Height VS Weight for Legendary and Non-Legendary Pokemons')
fig2 = plt.figure()
sns.scatterplot(data=data, x='weight_kg', y='height_m', hue='is_legendary')
st.pyplot(fig2)

# Correlation Between Features
title('Correlation between Feature')
fig3 = plt.figure()
sns.heatmap(legendary_data[['attack','sp_attack','defense','sp_defense','height_m','weight_kg','speed']].corr())
st.pyplot(fig3)

# Model Building using Randon Forest Classifier
title("Random Forest Classifier")
X_train , X_test , y_train , y_test = clean_and_split(data)
st.subheader("Sample Data")
st.dataframe(X_train.head(10))
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

title('Metrics')
st.subheader("Model Score: {}".format(model.score(X_test,y_test)))
st.subheader("Precision Score: {}".format(precision_score(model.predict(X_test),y_test)))
st.subheader("Accuracy Score: {}".format(recall_score(model.predict(X_test),y_test)))

# Confusion Matrix
st.subheader("Confusion Matrix")
fig5 = plt.figure()
conf_matrix = confusion_matrix(model.predict(X_test),y_test)
sns.heatmap(conf_matrix, annot=True, xticklabels=['Normal','Legendary'], yticklabels=['Normal','Legendary'])
plt.ylabel("Actual Values")
plt.xlabel("Predicted Values")
st.pyplot(fig5)
st.subheader("True Positive: {}".format(conf_matrix[1][1]))
st.subheader("True Negative: {}".format(conf_matrix[1][0]))
st.subheader("False Negative: {}".format(conf_matrix[0][1]))
st.subheader("False Positive: {}".format(conf_matrix[0][0]))