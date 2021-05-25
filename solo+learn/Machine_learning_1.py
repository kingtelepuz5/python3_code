n = int(input())
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])
y = [int(x) for x in input().split()]
datapoint = [float(x) for x in input().split()]

import pandas as pd
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
model.fit(X, y)

prevision = model.predict([datapoint])
print(int(prevision))
#======================================================
import numpy as np
import pandas as pd
filename = input()
column_name = input()

df = pd.read_csv(filename)
arr = np.array(df[column_name])
print(arr)
#===========================================================
tp, fp, fn, tn = [int(x) for x in input().split()]

ac = (tp + tn) / (tp+fp+fn+tn) #accuracy
pr = tp / (tp + fp) # precision
re = tp / (tp + fn) # recall
f1 = (2 * pr * re) / (pr + re) # f1 score

output = [ac, pr, re, f1]

for i in output:
	print(round(i, 4))
# gini чето там
S = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

SL = len(S)
BL=len(B)
AL = len(A)


one = S.count(1)
zero = S.count(0)
giniP = one/(one+zero)
giniInit = 2*giniP*(1-giniP)


one = A.count(1)
zero = A.count(0)
giniP = one/(one+zero)
giniLeft = 2*giniP*(1-giniP)


one = B.count(1)
zero = B.count(0)
giniP = one/(one+zero)
giniRight= 2*giniP*(1-giniP)

IG= giniInit -(giniLeft*(AL/SL))-(giniRight*(BL/SL))
print (round(IG,5))
#==============================================================
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

randomState = int(input())
n = int(input())
rows = []
for i in range(n):
	rows.append([float(a) for a in input().split()])

X = np.array(rows)
y = np.array([int(a) for a in input().split()])


X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=randomState)

rf = RandomForestClassifier(n_estimators=5,random_state=randomState)
rf.fit(X_train,y_train)

print(rf.predict(X_test))
# sigmoid func
w1, w2, b, x1, x2 = [float(x) for x in input().split()]
import math
output = w1*x1 + w2*x2 + b
output = round(1/(1 + math.exp(output*-1)), 4)
print(output)
