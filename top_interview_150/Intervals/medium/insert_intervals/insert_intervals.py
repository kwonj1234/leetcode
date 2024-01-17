class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for i in range(len(intervals)):
            if newInterval is None\
            or intervals[i][1] < newInterval[0] \
            or intervals[i][0] > newInterval[1]:
                if newInterval and  intervals[i][0] > newInterval[1]:
                    ans.append(newInterval)
                    newInterval = None
                ans.append(intervals[i])
            else:
                if newInterval[0] < intervals[i][0]:
                    if intervals[i][0] <= newInterval[1] < intervals[i][1]:
                        newInterval[1] = intervals[i][1]
                elif intervals[i][0] <= newInterval[0] <= intervals[i][1]:
                    if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
                        ans.append(intervals[i])
                        newInterval = None
                    elif intervals[i][1] < newInterval[1]:
                        newInterval[0] = intervals[i][0]

        if newInterval:
            ans.append(newInterval)        

        return ans