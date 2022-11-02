from typing import List
import collections


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    아래 Solution 의 알고리즘은 이해하겠는데...
    이게 왜 BFS 지 ?
    => 방문여부를 확인하는 배열이 존재 ! => 이게 Key Point 인듯...
    directed acyclic graph 문제임. 아무리 봐도...
    BFS 는 인접한 노드를 먼저 탐색.  아래 풀이는 순차적으로 하기 때문에 이런 조건에선 좀 벗어나지만, 방문여부를 확인하는 리스트(스택)
    을 쓰기 때문에 BFS 라고 분류되는듯 ?
    """
    courses = collections.defaultdict(set)
    pres = collections.defaultdict(set)
    for course, pre in prerequisites:
        courses[course].add(pre)  # set 이 기본 단위이기 때문에 add 라는 set 의 method 를 이용한다. value 는 set format 이다.
        pres[pre].add(course)
    # for 문이 우선이고, for 문에서 n이 나오면 그 n에 대해 courses 에 n 을 넣어 없으면 n을 추가.
    no_pre_courses = [n for n in range(numCourses) if not courses[n]]  # prerequisite course 가 없는 course 들
    count = 0
    while no_pre_courses:
        no_pre = no_pre_courses.pop()
        count += 1
        for course in pres[no_pre]:
            courses[course].remove(no_pre)
            if not courses[course]:
                # Prerequisites 을 모두 소화했으면 no_pre_courses 에 추가하여 while 문을 더 돌게 함
                no_pre_courses.append(course)
    return count == numCourses
    # 아래는 조금 더 나은 Solution
    # class Solution:
    #     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #         preMap = {i: [] for i in range(numCourses)}
    #
    #         for course, pre in prerequisites:
    #             preMap[course].append(pre)
    #
    #         visitSet = set()
    #
    #         def dfs(course):
    #             if course in visitSet:
    #                 return False
    #             if preMap[course] == []:
    #                 return True
    #
    #             visitSet.add(course)
    #
    #             for pre in preMap[course]:
    #                 if not dfs(pre): return False
    #             visitSet.remove(course)
    #             preMap[course] = []
    #
    #             return True
    #
    #         for course in range(numCourses):
    #             if not dfs(course): return False
    #         return True


print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
print(canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))
print(canFinish(20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]))
print(canFinish(3, [[1, 0], [1, 2], [0, 1]]))
print(canFinish(3, [[0, 2], [1, 2], [2, 0]]))
