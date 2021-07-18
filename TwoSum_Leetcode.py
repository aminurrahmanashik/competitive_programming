class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List_len = len(nums)
        List = []
        for i in range(List_len):
            for j in range(List_len):
                if nums[i] + nums[j] == target and i != j:
                    List.append(i)
                    List.append(j)
                    return List   
        
                                
