import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print ('Enter Trough')
Price_Max=input()
print ('Enter Peak')
Price_Min= input()
Diff= int(Price_Max) - int(Price_Min)
level1 = int(Price_Max) - 0.236 * Diff
level2 = int(Price_Max) - 0.382 * Diff
level3 = int(Price_Max) - 0.618 * Diff

print ("Level", " ", "PRICE")

print ("0 ", "      " , Price_Max)
print ("0.236", "   " ,level1)
print ("0.382",  "   ",level2)
print ("0.618","   ",  level3)
print ("1 ",   "      ", Price_Min)



