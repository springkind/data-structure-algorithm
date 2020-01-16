# 리스트에 숫자가 n개 있을 때 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘 만들기

# 결과값 : 0 이상, 정수, 1개
# 입력값 : 숫자 n개로 이루어진 리스트, 숫자 연속 아님, 중복 가능, 빈 배열 가능.
# 과정 : 하나의 비교 기준이 되는 숫자를 설정
#       리스트 안의 숫자와 기준 숫자를 비교함
#       비교했을 때 큰 숫자를 인덱스와 함께 저장
#       마지막까지 비교를 한 후 남아있는 숫자의 인덱스를 반환
#       만약 같은 값이 나올 경우에는 맨 처음의 인덱스 값을 반환

def get_index_of_max_num(l):
    # list가 빈 배열일 경우 None값을 반환
    if len(l) == 0:
        return None
    else:
        # 맨 처음 값으로 result 초기화
        result = [0, l[0]]
        
        # list를 하나씩 돌며 인덱스와 값을 모두 가져옴
        for idx, val in enumerate(l) :
            # list 안의 값 중에서 초기 값보다 큰 값이 발견될 경우 해당 값의 index와 value로 result갑 변경
            if val > result[1]:
                result = [idx, val]
                
    # result에서 index값만 가져와서 결과로 반환
    return result[0]



def test_get_index_of_max_num():
    assert get_index_of_max_num([]) == None
    assert get_index_of_max_num([1]) == 0
    assert get_index_of_max_num([1, 1, 1, 1, 1, 1]) == 0
    assert get_index_of_max_num([1, 2, 1, 1, 1]) == 1
    assert get_index_of_max_num([1, 5, 3, 7, 8, 6, 14, 1]) == 6
    assert get_index_of_max_num([1, 5, 3, 7, 78, 6, 14, 1]) == 4