#Creating structures for tasks
#Priority scheduling
class proc:
    def __init__(self,pid,at,bt,priority=0):
        self.pid=int(pid)
        self.at=int(at)
        self.bt=int(bt)
        self.pr=int(priority)
    pass
class task:
    def __init__(self,proc,st,et):
        self.proc=proc
        self.st=int(st)
        self.et=int(et)
    pass
def finin(processes, process):
    for p in processes:
        if process.pid==p.pid:
            return processes.index(p)
n=int(input("Enter the number of processes: "))
processes=[]
atl=[]
procq=[]
q=2
for i in range(n):
    pid=input(f"Enter the process ID for {i+1}th process:")
    at=input(f"Enter the arrival time for {i+1}th process:")
    bt=input(f"Enter the Burst time for {i+1}th process:")
    pr=input(f"Enter the priority for {i+1}th process:")
    print("*"*50) 
    process=proc(pid,at,bt,pr)
    processes.append(process)
    
processes.sort(key=lambda x : x.at)

done=[False for x in range(n)]
ct=processes[0].at 
while False in done:
    procq=[]
    for process in processes:
        if process.at<=ct and not done[processes.index(process)]:
            procq.append(process)
        if process.at>ct:
            break
    hipr=999999999
    hiproc=None
    for process in procq:
        
        if process.pr<hipr:
            hipr=process.pr
            hiproc=process
    atl.append(task(hiproc,ct,ct+hiproc.bt))
    ct+=hiproc.bt
    done[processes.index(hiproc)]=True
print("Process ID"," "*20,"Start time"," "*20,"End time"," "*20,"Turnaround time"," "*20,"Waiting time")
avgw=0.0
avgt=0.0


for task in atl:
    print(task.proc.pid," "*32,task.st," "*28,task.et," "*30,str(task.et-task.proc.at)," "*30,str(task.et-task.proc.at-task.proc.bt))    
    avgw=avgw+(task.et-task.proc.at-task.proc.bt)*1.0
    avgt=avgt+(task.et-task.proc.at)*1.0   
avgw=avgw/(n*1.0)
avgt=avgt/(n*1.0)

print("Average waiting time: ",avgw)
print("Average Turnaround time: ",avgt)
    
