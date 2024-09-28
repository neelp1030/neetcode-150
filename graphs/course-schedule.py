# you are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a
# the pair [0, 1], indicates that you must take course 1 before taking course 0
# there are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1
# return true if it is possible to finish all courses, otherwise return false

# first, we can populate an adjacency list for the graph based on the prerequisites
# if we successfully run a dfs on all courses, then we can return true
# but if any dfs results in a cycle (we will need to track visiting set), then it will be impossible so we return false
# we will also track a visited set to avoid redundant work

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjListMap = {i: [] for i in range(numCourses)}
        
        visited = set()
        visiting = set()

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

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

# time complexity: O(n + p)
# space complexity: O(n)