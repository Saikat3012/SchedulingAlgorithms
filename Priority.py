class Priority:
    def findWaitingTime(self,processes, n, wt):
        wt[0] = 0
        for i in range(1, n):
            wt[i] = processes[i - 1][1] + wt[i - 1]
    def findTurnAroundTime(self,processes, n, wt, tat):
        for i in range(n):
            tat[i] = processes[i][1] + wt[i]
    def findavgTime(self,processes, n):
        wt = [0] * n
        tat = [0] * n
        self.findWaitingTime(processes, n, wt)
        self.findTurnAroundTime(processes, n, wt, tat)
        total_wt = 0
        total_tat = 0
        for i in range(n):
            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]

        print("Average waiting time = %.5f "%(total_wt /n))
        print("Average turn around time = ", total_tat / n)

    def priorityScheduling(self,proc, n):
        proc = sorted(proc, key = lambda proc:proc[2],
                      reverse = True);
        self.findavgTime(proc, n)

# if __name__ =="__main__":
#
#     # Process id's
#     proc = [[1, 10, 1],
#             [2, 5, 0],
#             [3, 8, 1]]
#     n = 3
#     priorityScheduling(proc, n)
