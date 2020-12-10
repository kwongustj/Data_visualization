import pandas as pd  
import matplotlib as mpl       
import matplotlib.pyplot as plt

df8=pd.read_csv('roadkill.csv',sep=',')
plt.rc('font', family='NanumGothic') # For Windows
animals=df8.groupby('노선')['노선'].count()
print(animals)
animals.plot(kind = 'bar')