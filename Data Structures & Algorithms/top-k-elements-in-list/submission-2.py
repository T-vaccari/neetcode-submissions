class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        my_dict = defaultdict(int)
        for num in nums:
            my_dict[num] += 1

        buckets = [None] * (len(nums) + 1)  # Worst case scenario, all different

        for key, v in my_dict.items():
            if buckets[v] is None:
                buckets[v] = [key]
            else:
                buckets[v].append(key)

       

        index = len(nums) - 1
        res = []
        
        for count in range(len(nums), 0, -1):
            if buckets[count]:
                for num in buckets[count]:
                    res.append(num)
                    if len(res) == k:
                        return res



