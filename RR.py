class RR:
    def findWaitingTime(self,processes, n, bt,wt, quantum):
        rem_bt = [0] * n
        for i in range(n):
            rem_bt[i] = bt[i]
        t = 0
        while(1):
            done = True
            for i in range(n):
                if (rem_bt[i] > 0) :
                    done = False

                    if (rem_bt[i] > quantum) :
                        t += quantum
                        rem_bt[i] -= quantum
                    else:
                        t = t + rem_bt[i]
                        wt[i] = t - bt[i]
                        rem_bt[i] = 0
            if (done == True):
                break
    def findTurnAroundTime(self,processes, n, bt, wt, tat):
        for i in range(n):
            tat[i] = bt[i] + wt[i]
    def findavgTime(self,proc, n, quantum):
        wt = [0] * n
        tat = [0] * n
        processes,bt,a,pr=zip(*proc)
        processes=list(processes)
        bt=list(bt)
        self.findWaitingTime(processes, n, bt,wt, quantum)
        self.findTurnAroundTime(processes, n, bt,wt, tat)
        total_wt = 0
        total_tat = 0
        for i in range(n):

            total_wt = total_wt + wt[i]
            total_tat = total_tat + tat[i]

        print("Average waiting time = %.5f "%(total_wt /n) )
        print("Average turn around time = %.5f "% (total_tat / n))
# if __name__ =="__main__":
#
#     # Process id's
#     proc = [1, 2, 3]
#     n = 3
#
#     # Burst time of all processes
#     burst_time = [10, 5, 8]
#
#     # Time quantum
#     quantum = 2;
#     findavgTime(proc, n, burst_time, quantum)

