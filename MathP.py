import matplotlib.pyplot as abcd
import pandas as bbc
import numpy as numal
df=bbc.read_csv("check.csv")
v=numal.array(df['Total Population'])
m=numal.array(df['Total Males'])


abcd.plot(v,m)
abcd.show()