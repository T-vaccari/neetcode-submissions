class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #Maximum number of client that can be satifies i have at maximum
        # a certain number of jolly that i can use, called minutes
        if not grumpy or not customers:
            return 0

        if sum(grumpy) == 0:
            return sum(customers)
        if not grumpy or not customers:
            return 0

        # O(n) time solution to be found
        # I can compute the baseline for satisfied clients
        # then i can say, ok now immagine if all the clients in this window were satified
        # I can calculate the incremental difference, and maximize that incremental difference.
        
        window_sum = sum([customers[i] * grumpy[i] for i in range(minutes)])
        max_sum = window_sum
        for j in range(1, len(customers)-minutes + 1):
            window_sum = window_sum - customers[j-1] * grumpy[j-1]  + customers[j+minutes-1] * grumpy[j+minutes-1]
            max_sum = max(window_sum, max_sum)

        partial_sum = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                partial_sum += customers[i] 

        return partial_sum + max_sum


            

#customers = [1,0,1,2,1,1,7,5]
#   grumpy = [0,1,0,1,0,1,0,1]

# total = 0 + 0 + 0 + 2 + 0 + 1 + 7 + 5 = 



            




        