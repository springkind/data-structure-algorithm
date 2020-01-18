# 1부터 n까지 연속한 정수의 곱을 구하는 알고리즘을 만들어보세요.

def get_factorial(n):
    f = 1

    for i in range(2, n+1):
        f = f * i

    return f


def test_get_factorial():
    assert get_factorial(1) == 1
    assert get_factorial(2) == 2
    assert get_factorial(5) == 120