# 735. Asteroid Collision  [Medium]
# https://leetcode.com/problems/asteroid-collision/
# runtime 3 ms | memory 18.7 MB

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(0,len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            elif asteroids[i]<0:
                if len(stack)==0:
                    stack.append(asteroids[i])
                else:
                    if stack[-1]>(-1)*(asteroids[i]):
                        continue
                    elif stack[-1]==(-1)*(asteroids[i]):
                        stack.pop()
                        continue
                    elif stack[-1]<0 :
                        stack.append(asteroids[i])
                    else:
                        while len(stack)!=0 and stack[-1]>0 and stack[-1]<(-1)*(asteroids[i]):
                            stack.pop()
                        if len(stack)==0 or stack[-1]<0:
                            stack.append(asteroids[i])
                        elif stack[-1]>(-1)*(asteroids[i]):
                            continue
                        elif stack[-1]==(-1)*(asteroids[i]):
                            stack.pop()
        return stack
