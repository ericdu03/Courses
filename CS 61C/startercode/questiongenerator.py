import random, sys
if(len(sys.argv) != 3):
    print(f"Usage: {sys.argv[0]} <number of tasks> <number of threads>")
    print("Creates a new test case with the given number of tasks and expected number of threads")
    print("Additionally has several optional arguments to change runtime of each task and increase connectivity")
    print("Connectivity is a measure of how many prerequisites tasks will have.")
    print("A connectivity of 2 indicates that each task has on average two prerequisites")
    print("Outputs the new test case to stdout; you can pipe this to a file by adding the command \"> <file output>\"")
    print(f"As in: {sys.argv[0]} 10000 100 > a.out")
    exit()
#For random question generation
def generaterandomquestion(numtasks, numprocesses, mintime=1, maxtime=100, connectivityratio=2):
    tasks = [[] for i in range(numtasks)]
    print(numtasks)
    for i in range(int(connectivityratio*numtasks)):
        a = random.randrange(0, numtasks)
        b = random.randrange(0, numtasks)
        if(a!=b):
            if(b<a):
                a,b = b,a
            if(a not in tasks[b]):
                tasks[b].append(a)
    for i in range(numtasks):
        a = f"{i} {random.randrange(mintime, maxtime+1)} {len(tasks[i])}"
        for j in tasks[i]:
            a+= " "+str(j)
        print(a)
generaterandomquestion(int(sys.argv[1]),int(sys.argv[2]))
