class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_sorted = citations.copy()
        citations_sorted.sort()
        ans = 0
        for i in range(0, len(citations)):
            hindex = min(citations_sorted[i], len(citations_sorted) - i )
            ans = max(ans, hindex)
        return ans
        
