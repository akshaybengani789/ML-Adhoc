# -*- coding: utf-8 -*-
"""Data_Visualization1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uq4O6wl2MosxxDLwWgOYsAxF9fhiW2IC
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('student.csv')

plt.pie(df['marks'],labels=df['student_name'])

