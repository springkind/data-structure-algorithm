# 최댓값을 찾는 알고리즘

# 결과값 : 한개의 숫자
# 입력값 : 숫자들이 들어있는 배열. 중복값이 들어있을 수도 있고, 빈 배열일 가능성도 있음.
# 과정 : 리스트 안에 있는 숫자들의 크기 비교
def get_max(l):
    # 빈 배열이 들어올 경우
    if len(l) == 0:
        return None

    # 1개 이상의 숫자가 들어있는 배열인 경우
    else :
        # list의 첫번째 숫자를 가져와서 초기화
        max = l[0]
        # list에 있는 모든 숫자들을 한번씩 훑어보면서
        for n in l:
            # max 숫자보다 더 큰 숫자가 있는지 확인
            if n > max:
                # 만약 이전에 업데이트 된 max값 보다 더 큰 값이 발견될 경우, max값을 발견된 n으로 치환
                max = n

        # 마지막까지 확인 한 후 max 값으로 남아있는 숫자 반환
        return max

def test_get_max():
    assert get_max([]) == None
    assert get_max([1]) == 1
    assert get_max([1,1,1,1,1,1]) == 1
    assert get_max([1,2,1,1,1]) == 2
    assert get_max([1,5,3,7,8,6,14,1]) == 14
    assert get_max([1, 5, 3, 7, 78, 6, 14, 1]) == 78