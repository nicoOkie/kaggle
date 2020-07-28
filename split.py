import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/train.csv')

y = df['prix']
x = df.drop('prix', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=69)

x_test.to_csv('./data/test2.csv')
y_test.to_csv('./data/y_test.csv')
