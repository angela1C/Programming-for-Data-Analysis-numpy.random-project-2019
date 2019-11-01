print("hello")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

s = np.random.standard_normal(1500)  # 1500 standard normal values
print(np.mean(s)) # show that the mean is 0
np.std(s) # show that the standard deviation is 1

sns.distplot(s)

m1 = np.arange(3,20,2)
s1 = np.arange()