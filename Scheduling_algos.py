from fcfs import fcfs
from Priority import Priority
from RR import RR
from sjf import sjf
n=int(input("Enter the number of processes: "))
proc=[]
for i in range(n):
    print("Process: ",i+1,":--")
    b=int(input("\tEnter Burst time: "))
    a=int(input("\tEnter arrival time: "))
    p=int(input("\tEnter priority: "))
    proc.append([i+1,b,a,p])
quantum =int(input("Enter the Quantum: "))
f=fcfs()
p=Priority()
r=RR()
s=sjf()
print("\t\t:: Scheduling Algorithm ::")
print("<===============================================>")
print("FCFS:")
f.findavgTime(proc,n)
print("<===============================================>")
print("\nSJF:")
s.findavgTime(proc, n)
print("<===============================================>")
print("\nRR:")
r.findavgTime(proc, n,quantum)
print("<===============================================>")
print("\nPriority:")
p.priorityScheduling(proc, n)
