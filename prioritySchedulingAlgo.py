
bt=[]  
processes=[]   
wt=[] 
tat=[] 
priority[]

print("Enter the NUMBER of process: ")
n=int(input())

for i in range(0,n):
processes.insert(i,i+1)
 
print("Enter the BURST TIME of the processes: \n")
bt=list(map(int, raw_input().split()))

print("\nEnter the PRIORITY of the processes: \n")
priority=list(map(int, raw_input().split()))


for x in range(0,len(priority)):  
	for y in range(0,len(priority)-i):
		if(priority[y]>priority[y+1]):
   temp=priority[y]
   priority[y]=priority[y+1]
   priority[y+1]=temp
   
   temp=bt[y]
   bt[y]=bt[y+1]
   bt[y+1]=temp
   
   temp=processes[j]
   processes[y]=processes[y+1]
   processes[y+1]=temp
  
avgwt=0    
avgtat=0   

wt.insert(0,0)
tat.insert(0,bt[0])


for x in range(1,len(processes)):
 wt.insert(x,wt[x-1]+bt[x-1])
 tat.insert(x,wt[x]+bt[x])
 
 
 
for x in range(1,len(bt)):  
 wt.insert(x,wt[x-1]+bt[x-1])
 tat.insert(x,wt[x]+bt[x])
 avgwt+=wt[x]
 avgtat+=tat[x]

 
avgwt=float(avgwt)/n
avgtat=float(avgtat)/n

print("PROCESS\t  BURST TIME\t  WAITING TIME\t  TURN AROUND TIME")

for x in range(0,n):
 print(str(processes[x])+"\t\t"+str(bt[x])+"\t\t"+str(wt[x])+"\t\t"+str(tat[x]))
 print("\n")

print("Average Waiting time is: "+str(avgwt))
print("Average Turn Arount Time is: "+str(avgtat))
