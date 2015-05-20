class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        queue, indegree, outdegree = [], {}, {}
        for i, j in prerequisites:
            if i not in indegree: indegree[i] = {}
            if j not in outdegree: outdegree[j] = {}
            indegree[i][j] = True
            outdegree[j][i] = True
        for i in range(numCourses):
            if i not in indegree: queue.append(i)
        while queue:
            prerequisite = queue.pop()
            if prerequisite in outdegree:
                for course in outdegree[prerequisite]:
                    del indegree[course][prerequisite]
                    if not indegree[course]: queue.append(course)
                del outdegree[prerequisite]
        return len(outdegree) == 0
