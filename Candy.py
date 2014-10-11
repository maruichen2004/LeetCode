class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for i in range(len(ratings))]
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i+1] and candies[i] >= candies[i+1]:
                candies[i+1] = candies[i] + 1
        for i in reversed(range(1, len(ratings))):
            if ratings[i] < ratings[i-1] and candies[i] >= candies[i-1]:
                candies[i-1] = candies[i] + 1
        return sum(candies)
