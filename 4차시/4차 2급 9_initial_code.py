#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(height):
    #여기에 코드를 작성해주세요.
    count = 0
    for i, arr in enumerate(height):
        for j, idx in enumerate(arr):
            if ((j != 0 and arr[j-1] > idx) or (j == 0)) and ((j != 3 and arr[j+1] > idx) or (j == 3)) and  ((i != 0 and height[i-1][j] > idx) or (i == 0)) and  ((i != 3 and height[i+1][j] > idx) or (i == 3)):
                count+=1
                print(idx)
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")

