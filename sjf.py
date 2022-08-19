#shortest job first- non pre-emptive
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
n=int(input("Enter the number of processes."))
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
processes.sort(key=lambda x : x.at)
done=[False for x in range(n)]
t=processes[0].at #represents time
et=-1
while False in done:
    if et<=t:
        #If current time is greater than current end time then Start looking for minimums
        temp=[]
        for i in range(n):
            if not done[i] and processes[i].at<=t:
                temp.append([i,processes[i].bt])
        temp.sort(key=lambda x : x[1])        
        et=temp[0][-1]+t
        atl.append(task(processes[temp[0][0]],t,et))
        done[temp[0][0]]=True

    t+=1
         #if the task has not been done and has arrived at time



#Since sjf is a not preemptive/ linear scheduling algorithm we can find the total time of execution of the given
# Processes

    
            
            
                    
    
avgw=0.0
avgt=0.0
print("Process ID"," "*20,"Start time"," "*20,"End time"," "*20,"Turnaround time"," "*20,"Waiting time")
for task in atl:
    print(task.proc.pid," "*32,task.st," "*28,task.et," "*30,str(task.et-task.proc.at)," "*30,str(task.et-task.proc.at-task.proc.bt))    
    avgw=avgw+(task.et-task.proc.at-task.proc.bt)*1.0
    avgt=avgt+(task.et-task.proc.at)*1.0   
avgw=avgw/(n*1.0)
avgt=avgt/(n*1.0)

print("Average waiting time: ",avgw)
print("Average Turnaround time: ",avgt)
 
                    