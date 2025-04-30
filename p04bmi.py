import numpy as np
from sklearn.metrics import mean_squared_error
np.random.seed(42)

height = np.random.normal(170, 10,1000)
weight = np.random.normal(65, 15, 1000)

bmi = weight / (height/100)**2
print(bmi)
X = np.vstack((height, weight)).T
y = bmi
print(X)

#데이터를 train용과 test용으로 나눔
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42)

# 함수를 이용한 머신러닝
'''
from p05functions import fit_decision_tree, predict_decision_tree
# 학습 훈련 train
tree_model = fit_decision_tree(X_train, y_train)

# 테스트 데이터로 예측
y_pred = predict_decision_tree(tree_model, X_test)
'''
# 자체 제작 클래스 이용
'''
from p04bmiclass import MyDecisionTree
tree = MyDecisionTree()
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
'''
# 다른 사람이 만든 클래스 이용
from sklearn.tree import DecisionTreeRegressor
tree = DecisionTreeRegressor()
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)

# 평가 : 예측된 결과와, 정답 결과 비교
mse = mean_squared_error(y_pred, y_test)
print(f'평균제곱오차(mse): {mse:.3f}')

for i in range(5):
    print(f"실제 BMI: {y_test[i]:.2f} | 예측 BMI: {y_pred[i]:.2f}")
