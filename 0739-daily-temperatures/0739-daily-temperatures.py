class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[]
        answer=[0 for _ in temperatures]
        for i,t in enumerate(temperatures):  
            while st and temperatures[st[-1]]<t:
                pop=st.pop()
                answer[pop]=i-pop            
            st.append(i)   
            
        return answer

