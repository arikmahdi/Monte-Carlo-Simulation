# -*- coding: utf-8 -*-
"""Assignment_02_ii.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekxTMdKLIE4wjfrMMiDdqQttFcrah--S
"""

import random
import math
import matplotlib.pyplot as plt
random.seed(0)

n=[100,1000,5000,10000]
h1=[]
h2=[]
m1=[]
m2=[]
area_list=[]
length=len(n)
area_square=12  #square area: length*width
j=0
for i in range(length):
  trials=n[j]
  j=j+1
  hits=0
  h1.clear()
  h2.clear()
  m1.clear()
  m2.clear()

  for k in range(trials):
    x=random.uniform(0,2)
    y=random.uniform(0,6)
    y1=2*x+2
    if y<=y1:
      hits=hits+1
      h1.append(x)
      h2.append(y)
    else:
      m1.append(x)
      m2.append(y)
      
  
  area=(hits/trials)*area_square  #calculate area
  print("value of trials",trials)
  print("Area :",area)
  #area_list.append(area)    # collect area value in area list 

  #Scatter
  print("Scatter :")
  plt.scatter(m1, m2, label = "Miss",color="Green")
  plt.scatter(h1, h2, label = "Hit",color="Red")
  plt.legend()
  plt.show()