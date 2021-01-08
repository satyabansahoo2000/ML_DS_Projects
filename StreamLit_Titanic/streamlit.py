import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

@st.cache
def load_data():
    train = pd.read_csv("data/train.csv")
    return train

st.markdown('# SURVIVE OR NOT????')
st.markdown("![](https://media.giphy.com/media/OJw4CDbtu0jde/giphy.gif)")

def data_cleaning(train):
    train_copy = train.copy()

    # Droping the columns
    train_copy.drop(['PassengerId', 'Cabin', 'Ticket', 'Name'], axis=1, inplace=True)

    # Fillinf the nan values with mode and mean values
    train_copy['Embarked'].fillna(train_copy['Embarked'].mode()[0], inplace=True)
    train_copy['Age'].fillna(round(train_copy.Age.mean()), inplace=True)

    # Converting the categorical values to numerical
    train_copy = train_copy.join(pd.get_dummies(train_copy['Sex']))
    train_copy = train_copy.join(pd.get_dummies(train_copy['Embarked']))

    # Dropping the categorical columns
    train_copy.drop(['Sex', 'Embarked'], axis=1, inplace=True)

    return train_copy

train = load_data()
st.markdown("## Raw Data")
st.dataframe(train)
st.markdown('## Cleaned Data')
data = data_cleaning(train)
st.dataframe(data)

gender = st.sidebar.selectbox(
    'Gender?',
    ('Male', 'Female')
)

ticket = st.sidebar.selectbox(
    'Ticket Classs?',
    ('1 : Upper Class',
    '2 : Middle Class',
    '3 : Lower Class')
)

age = st.sidebar.slider(
    'Age of the person',
    0,80
)

siblings = st.sidebar.slider(
    "Number of siblings",
    0,8
)

parch = st.sidebar.slider(
    "Number of parents/Children",
    0,6
)

fare = st.sidebar.text_input("Enter the fare")

embarked = st.sidebar.selectbox(
    "Port of Embarkation",
    ['Cherbourg', 'Queenstown', 'Southampton'])

st.title("Distribution Data for Age")
fig1 = plt.figure()
sns.distplot(data['Age'])
st.pyplot(fig1)

st.title("Count of Ticket Class")
fig2 = plt.figure()
sns.countplot(data['Pclass'], color='blue')
st.pyplot(fig2)

st.title("Count of Siblings")
fig3 = plt.figure()
sns.countplot(data['SibSp'], color='blue')
st.pyplot(fig3)

st.title("Count of Parents/Children")
fig4 = plt.figure()
sns.countplot(data['Parch'], color='blue')
st.pyplot(fig4)

st.title("Distribution Data for Fare")
fig5 = plt.figure()
sns.distplot(data['Fare'])
st.pyplot(fig5)

features = data.drop(['Survived'], axis=1)
labels = data['Survived']

X_train, X_test, y_train, y_test = train_test_split(features, labels,
                                                    test_size=0.2, random_state=42,
                                                   shuffle=True)

st.markdown("### Gaussian Naive Bayes Model")
NB = GaussianNB()
NB.fit(X_train, y_train)
pred = NB.predict(X_test)
accuracy = accuracy_score(pred, y_test)
cross_valid = cross_val_score(NB, features, labels,
                            scoring='roc_auc', cv=10)
st.write(f"Accuracy Score: {round(accuracy,2)*100}%")
