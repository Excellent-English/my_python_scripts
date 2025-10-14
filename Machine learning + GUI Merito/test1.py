import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dane\\weight-height.csv", sep=",")
# print(type(df))
# print(df.head(3))
# print(df.columns)
#
# print(df.shape)
# print(df.shape[1])

print(f'Ile Pań i ile Panów: {df.Gender.value_counts()}')

df.Height *= 2.54
df.Weight /= 2.2
print(f'Dane po zmianie jednostek\n {df.head()}')

# plt.title('Wykres łączony')
# plt.hist(df.Weight, bins=50)
# plt.show()
#
# plt.title('Wykres pokazujący Panie i Panów')
# plt.hist(df.query("Gender=='Female'").Weight, bins=50)
# # plt.show()
#
# plt.hist(df.query("Gender=='Male'").Weight, bins=50)
# plt.show()




sns.histplot(df.Weight, bins=50).set_title('Wykres łączony')


plt.title('Wykres pokazujący Panie i Panów')
sns.histplot(df.query("Gender=='Female'").Weight).set_title('Wykres pokazujący Panie i Panów')

sns.histplot(df.query("Gender=='Male'").Weight)
# plt.subplot(2,2, 3)
# plt.show()


df = pd.get_dummies(df)
print(df.head())

#Gender 0 - mężczyzna, 1 - kobieta
del df['Gender_Male']
print(df.head())

df.rename(columns={'Gender_Female': 'Gender'}, inplace=True)
print(df.head())

model = LinearRegression()
model.fit(df[['Height', 'Gender']],df['Weight'])

print(f'Współczynnik kierunkowy: {model.coef_}')
print(f'Wyraz wolny: {model.intercept_}')

# własna formuła
gender = 0
height = 192
weight = model.coef_[0] * height + model.coef_[1] * gender + model.intercept_
print(weight)

print(model.predict([[192,0],[167,1]]))