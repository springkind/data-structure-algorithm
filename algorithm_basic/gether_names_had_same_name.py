# n명의 사람 아름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘을 만들기

# 결과값 : 리스트 안에 두 번이상 존재하는 리스트의 집합, {"Kelly"}
# 입력값 : ["Kelly", "Susan", "Anny", "Kelly"],
#         문자열들이 들어있는 리스트,
#         빈 배열일 가능성 있음, 모든 이름들에 중복이 없을 수도 있음, 하나의 이름만 여러번 들어있는 집합일 수 있음.


# solution 1
# 과정 : 이름이 '몇 번' 들어있는지 파악해야함.
#       리스트 내의 이름들이 몇 번씩 들어있었는지 카운팅 할 수 있는 딕셔너리를 만듬
#       원본 리스트를 돌면서 각각의 이름이 카운팅 딕셔너리에 들어있지 않을 1경우 목록에 추가하고 초기화, 들어있을 경우 카운트를 올림
#       원본 리스트를 모두 확인 한 이후 카운팅 딕셔너리에서 2개 이상 카운팅 된 이름들을 뽑아 집합을 만듬
def gether_names_had_smae_name(names) :
    # 빈 배열일 경우, 이름이 하나만 들어있는 경우
    if len(names) <= 1 :
        return set()
    else:
        # 이름이 몇번 들어있는지 갯수를 셀 딕셔너리 생성
        # (딕셔너리와 셋 모두 중괄호로 싸여있지만 빈 괄호를 썼을 때에는 {} dictionary 형이 됨. 조심.)
        counts = {}
        
        # names 리스트를 돌면서 count 딕셔너리에 이름, 갯수 저장
        for name in names :
            # 만약 count 딕셔너리에 name이 없을 경우
            if name not in counts :
                # count[name]의 value는 1로 초기화
                counts[name] = 1
            # 있을 경우
            else :
                # count[name]의 기존 값에 +1
                counts[name] = counts[name] + 1

    # 최종적으로 만들어진 counts 딕셔너리에서 value가 1 이상인 이름들만 가져와 집합으로 반환
    return {name for name, count in counts.items() if count > 1}


# solution 2 - 책 풀이
# 과정 : 앞에서부터 탐색하면서 이 이름이 뒤에 또 나오는지 확인.
#        뒤에서 이름이 또 발견된다면 바로 결과 집합에 추가
def gether_names_had_smae_name2(names) :
    # 빈 배열일 경우, 이름이 하나만 들어있는 경우
    if len(names) <= 1 :
        return set()
    else:
        # 1개 이상인 이름들을 저장할 집합 생성
        name_set = set()

        # 리스트의 모든 항목들을 인덱스로 한 번씩 접근
        for i in range(0, len(names)) :
            # 각각의 원소가 중복이 있는 원소인지 표시할 플래그
            is_duplicated = 0

            # i+1 이후의 인덱스 값으로 i번째 이후의 나머지 이름들과 i번째의 이름이 같은지 비교
            for j in range(i+1, len(names)) :
                # 만약 같은 이름이 있을 경우
                if names[i] == names[j] :
                    # i번째 이름의 flag는 1로 바뀜
                    is_duplicated = 1
            # i번째 인덱스 이후에 있는 이름들을 모두 탐색한 이후 최종 flag를 확인
            if is_duplicated == 1 :
                # 중복이 있는 경우 결과를 반환할 집합에 해당 이름 추가
                name_set.add(names[i])

    # 결과 집합 반환
    return name_set



def test_gether_names_had_smae_name() :
    assert gether_names_had_smae_name([]) == set()
    assert gether_names_had_smae_name(["Kelly"]) == set()
    assert gether_names_had_smae_name(["Kelly", "Susan", "Anny"]) == set()
    assert gether_names_had_smae_name(["Kelly", "Kelly", "Kelly"]) == {"Kelly"}
    assert gether_names_had_smae_name(["Kelly", "Susan", "Anny", "Kelly"]) == {"Kelly"}


def test_gether_names_had_smae_name2() :
    assert gether_names_had_smae_name2([]) == set()
    assert gether_names_had_smae_name2(["Kelly"]) == set()
    assert gether_names_had_smae_name2(["Kelly", "Susan", "Anny"]) == set()
    assert gether_names_had_smae_name2(["Kelly", "Kelly", "Kelly"]) == {"Kelly"}
    assert gether_names_had_smae_name2(["Kelly", "Susan", "Anny", "Kelly"]) == {"Kelly"}