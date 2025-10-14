import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("dane\\otodom.csv", sep=",")
print(df.head(3).to_string())

print()
print()

print(df.describe(percentiles=[0.1,0.3,0.5,0.95]).round(2).T.to_string())

print()
print()
# wykres korelacji kolumn
print(df.iloc[3:10,4:6])

print()
print(f'Wykres korelacji kolumn')
# Tworzenie heatmapy
plt.figure(figsize=(6, 4))
sns.heatmap(df.iloc[:, 1:].corr(), annot=True)

# Dostosowanie przestrzeni
plt.tight_layout()
plt.subplots_adjust(top=0.9)

# Wyświetlenie wykresu
plt.show()


plt.scatter(df.powierzchnia, df.cena)
plt.show()

x = df.iloc[:,2:]
y = df.iloc[:,1]
# y = df.cena

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = LinearRegression()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))