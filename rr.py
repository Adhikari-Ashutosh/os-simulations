#Creating structures for tasks
#Round robin
class proc:
    def __init__(self,pid,at,bt):
        self.pid=int(pid)
        self.at=int(at)
        self.bt=int(bt)
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
processes1=[]
atl=[]
procq=[]
q=2
for i in range(n):
    pid=input(f"Enter the process ID for {i+1}th process:")
    at=input(f"Enter the arrival time for {i+1}th process:")
    bt=input(f"Enter the Burst time for {i+1}th process:")
    print("*"*50) 
    process=proc(pid,at,bt)
    process1=proc(pid,at,bt)
    processes.append(process)
    processes1.append(process1)
processes.sort(key=lambda x : x.at)
processes1.sort(key=lambda x : x.at)
done=[False for x in range(n)]
ct=processes[0].at 
ready=[False for x in range(n)]
procq.append(processes[0])
while False in done:
    ci=procq.pop(0)
    if ci.bt>q:
        atl.append(task(processes1[finin(processes1,ci)],ct,ct+q))
        ci.bt-=q
        ct+=q
        ready[finin(processes,ci)]=True
    elif ci.bt>0:
        atl.append(task(processes1[finin(processes1,ci)],ct,ct+ci.bt))
        ct+=ci.bt
        ci.bt=0
        done[finin(processes,ci)]=True
        ready[finin(processes,ci)]=True
    else:
        done[finin(processes,ci)]=True
        ready[finin(processes,ci)]=True
    for process in processes:
        if ct>=process.at and not ready[processes.index(process)]:
            procq.append(process)
            ready[processes.index(process)]=True
        elif ct<process.at:
            break
    

    if ci.bt!=0:
        procq.append(ci)


ftl={} #final task lists for calculating wt and tat
for tas in atl:
    if tas.proc.pid in ftl:
        ftl[tas.proc.pid].et=tas.et
    else:
        ftl[tas.proc.pid]=task(tas.proc,tas.proc.at,tas.et)
avgw=0.0
avgt=0.0
print("Process ID"," "*20,"Start time"," "*20,"End time"," "*20,"Turnaround time"," "*20,"Waiting time")
for i in ftl:
    avgw=avgw+(ftl[i].et-ftl[i].st-ftl[i].proc.bt)*1.0
    avgt=avgt+(ftl[i].et-ftl[i].st)*1.0
    print(ftl[i].proc.pid," "*32,ftl[i].st," "*28,ftl[i].et," "*30,ftl[i].et-ftl[i].st," "*30,ftl[i].et-ftl[i].st-ftl[i].proc.bt)   



            


    
      
avgw=avgw/(n*1.0)
avgt=avgt/(n*1.0)

print("Average waiting time: ",avgw)
print("Average Turnaround time: ",avgt)
 
                      
            
