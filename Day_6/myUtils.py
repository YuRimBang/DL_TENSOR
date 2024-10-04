###---------------------------------------------------
### 모델 구현 및 학습에 사용되는 공통 기능 함수들
###---------------------------------------------------
###모듈 로딩
import tensorflow as tf
###---------------------------------------------------
### 함수 기능 : 회귀 모델의 솔실 계한 후 반환
### 함수 이름 : regLossFunc
### 매개 변수 : target_y, predicted_y, kind
###---------------------------------------------------
# 손실함수/비용함수  :  타겟값과 예측값의 차이 계산 함수 
# 회귀 : MSE
def regLossFunc(target_y, predicted_y, kind="mse"):
    
    if kind=="mse":
        return tf.reduce_mean(tf.square(target_y - predicted_y))
    elif kind=="mae":
        return
    elif kind=="rmse":
        return