"""Course Schedule"""
"""Link to the problem: https://leetcode.com/problems/course-schedule/"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # map each course to prerequisites List
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        # visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False

            if preMap[crs] == []:
                return True

            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


if __name__ == '__main__':
    solution = Solution()
    Input = {"numCourses": 2, "prerequisites": [[1, 0]]}
    print(f"Input:{Input}")
    Output = solution.canFinish(Input["numCourses"], Input["prerequisites"])
    print(f"Output:{Output}")
