# you are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z
# you are also given an integer n
# each CPU cycle allows the completion of a single task, and tasks may be completed in any order
# the only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU
# return the minimum number of CPU cycles required to complete all tasks

# the idea is basically to always prioritize the task type that has the most of its kind left, to optimize cooldown time
# to do this, we will count up the frequency of each task type and store this info in a maxHeap
# for every cpu cycle, we determine the highest remaining frequency task type and run that one
# whenever we run a task, it will go on cooldown and be able to run again only after the cooldown time has elapsed
# so while the task is on cooldown, we will store it in a queue (deque)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
            time += 1
        
        return time

# time complexity: O(n)
# space complexity: O(1)