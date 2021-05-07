import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


#Pandas
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
#Zad1
grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
wykres = grupa.plot()
wykres.legend()
plt.title("Liczba urodzonych dzieci dla każdego roku")
plt.show()
#Zad2
grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.bar()
wykres.legend()
plt.xticks(rotation=0)
plt.title("Liczba urodzonych chłopców i dziewczynek")
plt.show()
#Zad3
grupa = df[df['Rok'] > 2012].groupby(['Plec']).agg({'Liczba':['sum']})
wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20)
plt.legend()
plt.show()

#Matplotlib

#Zad1
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()
#Zad2
x = np.arange(1, 21, 1)
plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, 20, 0, 1])
plt.legend()
plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
plt.show()
#Zad3
x = np.arange(0, 30, .1)
plt.plot(x, np.sin(x), 'b', label='sin(x)')
plt.plot(x, np.cos(x), 'r', label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x) cos(x)')
plt.legend(loc='upper right')
plt.show()
#Zad4
df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
print(df)
colors = np.random.randint(0, 50, len(df.index))
scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) for x in range(len(df.index))]
scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) * 5 for x in range(len(df.index))]
plt.scatter(df[0], df[1], c=colors, s=scale)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
#Zad5
plt.subplot(1, 3, 1)
grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()
grouped.plot.bar(color=['r', 'g'])
plt.xlabel('Płeć')

#2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.ylabel('Liczba narodzonych dzieci')

#3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
y = df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()
plt.bar(x, y)
plt.show()

#Zad6
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
explode = [0.0 for n in range(len(policzone.index))]
explode[np.random.randint(0, len(policzone.index) + 1)] = 0.2
policzone.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadow=True)
plt.title("Procentowy udział kwot zamówień sprzedawców")
plt.show()