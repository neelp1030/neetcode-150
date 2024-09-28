# you are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
# for example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# there are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

# same as original course schedule problem except you also append courses to a result list as you successfully visit them
# return either the result list or [] based on whether you detected a cycle during the process or not (if any of the dfs returns False, then there was a cycle)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjListMap = {i: [] for i in range(numCourses)}
        
        visited = set()
        visiting = set()

        res = []

        for course, prereq in prerequisites:
            adjListMap[course].append(prereq)
        
        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
            
            visiting.add(course)

            for prereq in adjListMap[course]:
                if not dfs(prereq):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res

# time complexity: O(n + p)
# space complexity: O(n)