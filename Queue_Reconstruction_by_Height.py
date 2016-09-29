class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(people) == 0:
            return []
        n = len(people)
        sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
        height, index = [], []
        for i in range(n):
            height.insert(sorted_people[i][1], sorted_people[i][0])
            index.insert(sorted_people[i][1], sorted_people[i][1])
        res = []
        for i in range(n):
            res.append([height[i], index[i]])
        return res