import numpy as np
import statistics as st
def calcute(lis):
   a= np.mean(lis)
   b=np.median(lis)
   c=st.mode(lis)
   print(f"mean: {a}")
   print(f"mediann: {b}")
   print(f"mode: {c}")
lis=[1,2,2,3,4,5]
print(calcute(lis))

