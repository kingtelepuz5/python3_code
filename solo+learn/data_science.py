#
import numpy as np
n, p = [int(x) for x in input().split()]

lista = []
for i in range(n):
    lista.append(input().split())
print(np.array(lista).astype(np.float16).mean(axis=1).round(2))
# reshape

import numpy as np
r = int(input())
lst = [float(x) for x in input().split()]

arr_ABD = np.array(lst)
arr_ABD = arr_ABD.reshape(r,int(len(lst)/r))
print(arr_ABD.round(2))

# заменяем нан средним значением ряда
import numpy as np
import pandas as pd

lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]
lst_df = pd.Series(lst)
abd = lst_df.fillna(lst_df.mean()).round(1)
print(abd)
#hz cto
n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]


import numpy as np

X=np.array(X).reshape(n,p)
y=np.array(y)
b=np.linalg.pinv(X) @ y.transpose()
print(np.around(b,decimals=2))
# matrix confusion
y_true = [x for x in input().split()]
y_pred =  [x for x in input().split()]

from sklearn.metrics import confusion_matrix

print((confusion_matrix(y_pred, y_true, labels=['1', '0']))/1)
# hz chto 2
import numpy as np


first = np.array([[0., 0.]])
second = np.array([[2., 2.]])
n = int(input())

data = []

for i in range(n):
   data.append([float(i) for i in input().split()])


data = np.array(data).reshape((-1,2))


for i in range(n):
   dist1 = np.sqrt(((data[i]-first[0])**2).sum())

   dist2 = np.sqrt(((data[i]-second[0])**2).sum())

   if (dist1) <= (dist2):
      first = np.vstack((first,data[i]))

   else:
      second = np.vstack((second,data[i]))



if first.size > 2:
   mean1 = np.mean(first[1:], axis=0)
   print(np.around(mean1, decimals=2))
else:
   print(None)


if second.size > 2:
   mean2 = np.mean(second[1:], axis=0)
   print(np.around(mean2, decimals=2))
else:
   print(None)
