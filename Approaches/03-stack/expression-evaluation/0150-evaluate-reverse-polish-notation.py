# 150. Evaluate Reverse Polish Notation  [Medium]
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# runtime 41 ms | memory 20.5 MB

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st=[]
        nums=[]
        for i in range(-200, 201):
            nums.append(str(i))
        for i in tokens:
            if i in nums:
                st.append(int(i))
            else:
                if i=='+':
                    t2=st.pop()
                    t1=st.pop()
                    st.append(t1+t2)
                elif i=='-':
                    t2=st.pop()
                    t1=st.pop()
                    st.append(t1-t2)
                elif i=='*':
                    t2=st.pop()
                    t1=st.pop()
                    st.append(t1*t2)
                elif i=='/':
                    t2=st.pop()
                    t1=st.pop()
                    st.append(int(t1/t2))
        return st.pop()
