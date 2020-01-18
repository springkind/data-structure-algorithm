# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만들어보세요.

# solution 1 for문을 이용한 풀이
def get_factorial(n):
    f = 1

    for i in range(2, n+1):
        f = f * i

    return f

# solution 2 재귀함수를 이용한 풀이
def get_factorial_by_recursive(n):
    if n == 1:
        return 1
    return n * get_factorial_by_recursive(n-1)


def test_get_factorial():
    assert get_factorial(1) == 1
    assert get_factorial(2) == 2
    assert get_factorial(5) == 120

def test_get_factorial_by_recursive():
    assert get_factorial_by_recursive(1) == 1
    assert get_factorial_by_recursive(2) == 2
    assert get_factorial_by_recursive(5) == 120