bt=[]
wt=[]
tat=[]
avgwt=0
avgtat=0

print("Enter the NUMBER of processes: ")
n=int(input())


print("Enter the BURST TIME of the processes: \n")
bt=list(map(int, raw_input().split()))

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
 print(str(x)+"\t\t"+str(bt[x])+"\t\t"+str(wt[x])+"\t\t"+str(tat[x]))
 print("\n")
 
print("Average Turn Arount Time is: "+str(avgtat))

print("Average Waiting time is: "+str(avgwt))

