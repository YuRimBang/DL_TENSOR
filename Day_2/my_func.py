#------------------------------------------
# 다양한 객체에 활용되는 함수들 포함 모듈
#------------------------------------------
# 함수이름 : printInfo
# 함수기능 : ndarray 객체 속성 출력
# 매개변수 : ndarray 객체, ndarray 객체 이름
# 함수결과 : 없음
#------------------------------------------


def printInfo(ndarrayObj, ndarrayName):
    #ndarray 객체/인스턴스 속성 확인/읽기 ==> 변수명.속성
    print(f'===========[{ndarrayName}]==========')
    print(f'shape : {ndarrayObj.shape}')
    print(f'ndim : {ndarrayObj.ndim}D')
    print(f'size : {ndarrayObj.size}개')
    print(f'itemsize : {ndarrayObj.itemsize}바이트')
    print(f'dtype : {ndarrayObj.dtype}')
    print(f'data : {ndarrayObj.data}')
    print(ndarrayObj)