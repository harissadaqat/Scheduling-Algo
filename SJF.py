
bt=[]  
processes=[]   
wt=[] 
tat=[] 

print("Enter the NUMBER of process: ")
n=int(input())

for x in range(0,n):
processes.insert(x,x+1)

print("Enter the BURST TIME of the processes: \n")
bt=list(map(int, raw_input().split()))


for x in range(0,len(bt)):  
	for y in range(0,len(bt)-i):
		if(bt[y]>bt[y+1]):
   temp=bt[y]
   bt[y]=bt[y+1]
   bt[y+1]=temp
   temp=processes[y]
   
   processes[y]=processes[y+1]
   processes[y+1]=temp
  
avgwt=0    
avgtat=0   

wt.insert(0,0)
tat.insert(0,bt[0])


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