
"""
택배 배달과 수거하기 문제

https://school.programmers.co.kr/learn/courses/30/lessons/150369
"""


def solution(cap, n, deliveries, pickups):
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries.pop()
        have_to_pick += pickups.pop()

        while have_to_deli > 0 or have_to_pick > 0:  # break point : 가장 먼 point 모두 task 완료 시.
            # 각 변수의 음수가 의미하는 것 : 잔여 task 배송 및 수집 회수이며 이 루프에서 탈출한 뒤 만약 새로이 pop 해서 가져오는 값들이 다시 음수 혹은 0이 되면 바로 탈출.
            # 이는 가는 길 혹은 돌아오는 길에 task 를 수행했다는 것과 동치의 의미
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2  # 왕복. 가장 먼거리부터 하므로 n - i 가 기본거리.

    return answer