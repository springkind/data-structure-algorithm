# 1부터 n까지의 수를 모두 더해라

# solution 1
# 구해야하는 목표 : 모두 다 더한 '숫자 하나'
# 1부터 하나씩 더해서 n까지 모두 더한다
def sum_n(num):
    result = 0

    for n in range(1, num+1):
        result = result + n

    return result

# solution 2
# 구해야하는 목표 : 모두 다 더한 '숫자 하나'
# 양 끝 숫자를 더하는 공식을 사용한다
def sum_n2(num):
    return num*(num+1)/2


# pytest 검증
def test_sum_n():
    assert sum_n(1) == 1
    assert sum_n(2) == 1+2
    assert sum_n(5) == 1+2+3+4+5
    assert sum_n(10) == 55
    assert sum_n(100) == 5050


def test_sum_n2():
    assert sum_n2(1) == 1
    assert sum_n2(2) == 1+2
    assert sum_n2(5) == 1+2+3+4+5
    assert sum_n2(10) == 55
    assert sum_n2(100) == 5050
