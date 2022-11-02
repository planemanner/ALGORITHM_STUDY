from typing import List

"""
An image is represented by an m x n integer grid image where image[i][j] represents 

the pixel value of the image.

You are also given three integers sr, sc, and color. 

You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, 

plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 

plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 

Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

constraints

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # 이 문제는 시작점에서 자기 그룹에 속하는 친구들만 찾으면 되는 문제.
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        row_len = len(image)
        col_len = len(image[0])
        center_color = image[sr][sc]
        visit = set()

        def change_color(y, x):

            if image[y][x] == center_color:
                image[y][x] = color

        def search(row, col):
            change_color(row, col)
            visit.add((row, col))
            for direction in directions:
                dy, dx = direction
                ny, nx = row + dy, col + dx
                if 0 <= ny < row_len and 0 <= nx < col_len and (ny, nx) not in visit:
                    if image[ny][nx] == center_color:
                        # 인덱싱 하는 시간도 꽤 크니까 이거 항상 고려하자.
                        search(ny, nx)

        search(sr, sc)
        return image


class Solution_2:
    # 더 나은 코드 구조
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.R = len(image)
        self.C = len(image[0])
        starting_pixel = image[sr][sc]

        self.dfs(image, sr, sc, color, starting_pixel)
        return image

    def dfs(self, image, sr, sc, color, starting_pixel):
        if sr < 0 or sr > self.R - 1 or sc < 0 or sc > self.C - 1 or image[sr][sc] != starting_pixel or \
                image[sr][sc] == color:
            # Valid point 가 아닌 경우 재귀 함수 종료를 위한 조건문
            return

        image[sr][sc] = color
        self.dfs(image, sr + 1, sc, color, starting_pixel)
        self.dfs(image, sr - 1, sc, color, starting_pixel)
        self.dfs(image, sr, sc + 1, color, starting_pixel)
        self.dfs(image, sr, sc - 1, color, starting_pixel)


solver = Solution()
image = [[1,1,1],[1,1,0],[1,0,1]]
image_2 = [[0,0,0],[0,0,0]]
new_image = solver.floodFill(image, 1, 1, 2)
new_image_2 = solver.floodFill(image_2, 0, 0, 0)
print(new_image)
print(new_image_2)
print(sum([123,74,74,171,95])/5)