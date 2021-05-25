#--------------------LinearRegression algoritm------------------------
from sklearn.linear_model import LinearRegression
import  numpy as np
## Data (Apple stock prices)
apple = np.array([155, 156, 157])
n = len(apple)

model = LinearRegression().fit(np.arange(n).reshape((n,1)),apple)
print("Model predict to data Apple: \n",model.predict([[3],[4]]))
import matplotlib.pyplot as plt
plt.xkcd()
plt.plot(model.predict([[3],[4]]), data=apple)
plt.title('Apple Stock price')
plt.xlabel('X')
plt.ylabel('Y')
plt.savefig("plot.jpg")
#plt.show()
#-----------------------LogisticRegression model---------------------
from sklearn.linear_model import LogisticRegression
## Data (#cigarettes, cancer)
X = np.array([
            [0, "No"],
            [30, "Yes"],
            [90, "Yes"]])

model = LogisticRegression().fit(X[:,0].reshape(n,1), X[:,1])
print("predict on LogisticRegression one_line: \n",model.predict([[2],[12],[13],[40],[90]]))

for i in range(20):
    print("x=" + str(i) + "-->" + str(model.predict_proba([[i]]))) # алгоритм говори, что если человек курит 12 и более сигарет шанс заболеть раком быстро возрастает
plt.xkcd()
plt.title('Sigarets to die ^^ <3')
plt.xlabel('coll')
plt.ylabel('True/nope')
plt.hist(model.predict([[2],[12],[13],[40],[90]]))
plt.savefig("plot_log.jpg")
#plt.show()
#-------------
plt.xkcd()
plt.title('Sigarets to die ^^ <3')
plt.xlabel('coll')
plt.ylabel('True/nope')
plt.savefig("plot_log.jpg")
#plt.show()
#--------
plt.xkcd()
plt.title('Sigarets to die ^^ <3')
plt.xlabel('coll')
plt.ylabel('True/nope')
plt.hist(model.predict_proba([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]]))
plt.savefig("plot_log1_h.jpg")
#plt.show()
#-------
plt.plot(model.predict([[2],[12],[13],[40],[90]]))
plt.xkcd()
plt.xlabel('coll')
plt.ylabel('True/nope')
plt.plot(model.predict_proba([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20]]))
plt.savefig("plot_log1_p.jpg")
#plt.show()
#-----------------K means algoritm---------------------------
from sklearn.cluster import KMeans
## Data (Work (h) / Salary ($))
X = np.array([[35, 7000], [45, 6900], [70,7100], [20, 2000], [25, 2200], [15, 1800]])
kmeans = KMeans(n_clusters=2).fit(X)
cc = kmeans.cluster_centers_
print(cc)
#-----------------Hist ---------------------
plt.xkcd()
plt.title('True work week ^^ <3')
plt.xlabel('coll')
plt.ylabel('Many')
plt.hist(cc)
plt.savefig("plot_K_m_h.jpg")
#plt.show()
#-------------------plot-----------------
plt.xkcd()
plt.title('True work week ^^ <3')
plt.xlabel('coll')
plt.ylabel('Many')
plt.plot(cc, data=X)
plt.savefig("plot_K_m_h.jpg")
#plt.show()

#---------------KNN(forest)-------------------------

from sklearn.neighbors import KNeighborsRegressor
##Data House Size(square meters)/ House Price($)
X = np.array([[35, 30000], [45, 45000], [40, 50000], [35, 35000], [25, 32500], [40, 40000]])
KNN = KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1, 1), X[:,1])
res = KNN.predict([[30]])
print("out put KNN: \n",res)
print(X[:,0].reshape(-1,1))
#---------------- Plot --------------------
plt.xkcd()
plt.title('Это цена домов в зависимости от размера дома')
plt.xlabel('Размер дома')
plt.ylabel('Цена')
plt.plot(res)
plt.savefig("plot_KNN_m_p.jpg")
#plt.show()

#------NEURAL-NETWORK----------------
## Dependencies
from sklearn.neural_network import MLPRegressor
import numpy as np
## Questionaire data (WEEK, YEARS, BOOKS, PROJECTS, EARN, RATING)
X = np.array(
[[20, 11, 20, 30, 4000, 3000],
[12, 4, 0, 0, 1000, 1500],
[2, 0, 1, 10, 0, 1400],[35, 5, 10, 70, 6000, 3800],
[30, 1, 4, 65, 0, 3900],
[35, 1, 0, 0, 0, 100],
[15, 1, 2, 25, 0, 3700],
[40, 3, -1, 60, 1000, 2000],
[40, 1, 2, 95, 0, 1000],
[10, 0, 0, 0, 0, 1400],
[30, 1, 0, 50, 0, 1700],
[1, 0, 0, 45, 0, 1762],
[10, 32, 10, 5, 0, 2400],
[5, 35, 4, 0, 13000, 3900],
[8, 9, 40, 30, 1000, 2625],
[1, 0, 1, 0, 0, 1900],
[1, 30, 10, 0, 1000, 1900],
[7, 16, 5, 0, 0, 3000]])
## One-liner
neural_net = MLPRegressor(max_iter=1000, solver='lbfgs').fit(X[:,:-1], X[:,-1])# переобучение, в книге ошибка на 9900 итераций +  оптимизатор
## Result
res = neural_net.predict([[0, 0, 0, 0, 0]])
print(res)
print("Out put neural_net: \n",res)#ожидаемый выход при 00000 это 94.94
res = neural_net.predict([[20,0,0,0,0]])
print("Ожидаемый выход 440, больше не сильно страшно: \n",res)
#сеть работает через жопу
res = neural_net.predict([[20,0,10,0,0]])
print(res)
res = neural_net.predict([[20, 1, 10, 0, 0]])
print(res)
res = neural_net.predict([[20, 1, 10, 50, 1000]])
print("мой коэф профи: \n",res)
#---------forest -------------
from sklearn import tree

## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
[1, 8, 1, "linguistics"],
[5, 7, 9, "art"]])
Tree = tree.DecisionTreeClassifier().fit(X[:,:-1], X[:,-1])
student_0 = Tree.predict([[8,6, 5]])
print("Студент с знаниями, мат 8, языки 6, креативность 5: \n",student_0)
student_1 = Tree.predict([[3, 7, 9]])
print("Студент с знаниями, мат 3, языки 7, креативность 9: \n",student_1)
#------------RISK-------------
## Data (rows: stocks / cols: stock prices)
X = np.array([[25,27,29,30],
[1,5,3,2],
[12,11,8,3],
[1,1,2,2],
[2,6,2,2]])
# Find the stock with smallest variance
#min_row = min([(i,np.var(X[i,:])) for i in range(len(X))], key=lambda x: x[1])
#print("Row with minimum variance: \n", + str(min_row(0)))
#print("Variance:\n ", + str(min_row[1]))
#don't work, why? i am don't give a fuck
var = np.var(X, axis=1)#аксис1 это по строкам, аксис0 по столбцам
min_row = (np.where(var==min(var)), min(var))
print(var)
print(min_row)
#---------- ----------------------------
X = np.array([[1,3,5], [1, 1, 1], [0, 2, 4]])
print("average: \n",np.average(X))
print("var: \n",np.var(X))
print("std: \n",np.std(X))
#------------------0000-----------------
## Stock Price Data: 5 companies
# (row=[price_day_1, price_day_2, ...])
x = np.array([[8, 9, 11, 12],
[1, 2, 2, 1],
[2, 8, 9, 9],
[9, 6, 6, 3],
[3, 3, 3, 3]])
avg, var, std = np.average(x, axis=1),np.var(x, axis=1), np.std(x, axis=1)
print("averages: \n" + str(avg))
print("Variance: \n" + str(var))
print("Standart Devitiations: \n" + str(std))
#================----=================
x = np.array([[[1,2], [1,1]],
[[1,1], [2,1]],
[[1,0], [0,0]]])
print("averages(Axis=2): \n" +str(np.average(x, axis=2)))
print("Variance(Axis=2): \n" +str(np.var(x, axis=2)))
print("Sta(Axis=2): \n" +str(np.std(x, axis=2)))
#===================SVMS===================
from sklearn import svm
## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
[10, 1, 2, "computer science"],
[1, 8, 1, "literature"],
[4, 9, 3, "literature"],
[0, 1, 10, "art"],
[5, 7, 9, "art"]])
svm = svm.SVC().fit(X[:,:-1], X[:,-1])
student_0  = svm.predict([[3,3,6]])
student_1 = svm.predict([[8, 1, 1]])
print("Student_0(3,3,6) :\n ",student_0)
print("Student_1(8,1,1) :\n ",student_1)
#--------------RANDOM FOREST--------------------
from sklearn.ensemble import RandomForestClassifier
## Data: student scores in (math, language, creativity) --> study field
X = np.array([[9, 5, 6, "computer science"],
[5, 1, 5, "computer science"],
[8, 8, 8, "computer science"],
[1, 10, 7, "literature"],
[1, 8, 1, "literature"],
[5, 7, 9, "art"],
[1, 1, 6, "art"]])
forest = RandomForestClassifier(n_estimators=10).fit(X[:,:-1], X[:,-1])
students = forest.predict([[8,6,5], [3,7,9], [2, 2, 1]])
print("RANDOM forest predict: \n",students)
