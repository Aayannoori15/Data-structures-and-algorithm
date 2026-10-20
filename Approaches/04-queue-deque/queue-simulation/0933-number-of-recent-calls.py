# 933. Number of Recent Calls  [Easy]
# https://leetcode.com/problems/number-of-recent-calls/
# runtime 42 ms | memory 23 MB

class RecentCounter:

    def __init__(self):
        self.queue=[]

    def ping(self, t: int) -> int:
        self.queue.append(t)
        m = t - 3000
        while self.queue and self.queue[0] < m:
            self.queue.pop(0)
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
