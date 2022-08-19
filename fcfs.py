#first come first serve 
class proc:
    #Class wrapping the input 
    def __init__(self,pid,at,bt):
        self.pid=int(pid)
        self.at=int(at)
        self.bt=int(bt)
    pass
class task:
    #Class wrapping the output (containing start times and end times per process)
    def __init__(self,proc,st,et):
        self.proc=proc
        self.st=int(st)
        self.et=int(et)
    pass
def smol(a,b):
    if(a>b):
        return a
    else:
        return b
n=int(input("Welcome to the FCFS simulator. To begin enter the number of processes you wish to simulate."))
processes=[]
atl=[]
for i in range(n):
    print("*"*50)    
    pid=input(f"Enter the process ID (integer) for {i+1}th process:")
    at=input(f"Enter the arrival time for {i+1}th process:")
    bt=input(f"Enter the Burst time for {i+1}th process:")
    print("*"*50) 
    process=proc(pid,at,bt)
    processes.append(process)
     
processes.sort(key= lambda x:x.at)
t=0
for i in range(n-1):
    if processes[i].at == processes[i+1].at:
        if processes[i].pid>processes[i+1].pid:
            tas=task(processes[i+1],smol(t,processes[i+1].at),processes[i+1].bt+smol(t,processes[i+1].at))
            t=processes[i+1].bt+smol(t,processes[i+1].at)
            atl.append(tas)
            tas=task(processes[i],smol(t,processes[i].at),processes[i].bt+smol(t,processes[i].at))
            t=processes[i].bt+smol(t,processes[i].at)
            atl.append(tas)
            i+=1
        else:
            tas=task(processes[i],smol(t,processes[i].at),processes[i].bt+smol(t,processes[i].at))
            t=processes[i].bt+smol(t,processes[i].at)
            atl.append(tas)
            tas=task(processes[i+1],smol(t,processes[i+1].at),processes[i+1].bt+smol(t,processes[i+1].at))
            t=processes[i+1].bt+smol(t,processes[i+1].at)
            atl.append(tas)
            i+=1
           
    else:
        tas=task(processes[i],smol(t,processes[i].at),processes[i].bt+smol(t,processes[i].at))
        t=processes[i].bt+smol(t,processes[i].at)
        atl.append(tas)
        
        
if i<n-1:
    tas=task(processes[n-1],smol(t,processes[n-1].at),processes[n-1].bt+smol(t,processes[n-1].at))
    t=processes[n-1].bt+smol(t,processes[n-1].at)
    atl.append(tas)
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
