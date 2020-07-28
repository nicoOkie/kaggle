import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/train.csv')
df.dropna()

y = df['prix']
x = df.drop('prix', axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=69)

y_test.to_csv('./data/test2.csv')
y_test.to_csv('./test2-predictions.csv')
