#Setup
import sys
if "-v" in sys.argv:
    verbose = True
    sys.argv.remove("-v")
else:
    verbose = False
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <test case> <proposed solution> <thread count> [-v]")
    print("Verifies a proposed solution, given a test case and the number of threads")
    print("Both the test case and the proposed solution should be saved in a file, and the filename sent in as input")
    print("Threads will complete the tasks in their list in order, waiting idly until all prerequisites have completed")
    print("By default, determines if a deadlock occurs, and if not, calculates the full runtime and usage ratio.")
    print("An optional -v argument adds additional information, for debugging purposes")
    exit()

#Parse input files
def parsetestfile(testfile):
    data = testfile.readlines()[1:]
    result = []
    for i in data:
        element = [int(j) for j in i.strip().split(" ")]
        result.append([element[0], element[1], element[3:]])
    return result
def parseanswerfile(answerfile):
    return [[int(j.strip()) for j in i.split(",")] for i in answerfile.readline().split(";")]
testfile = open(sys.argv[1])
test = parsetestfile(testfile)
testfile.close()
answerfile = open(sys.argv[2])
answer = parseanswerfile(answerfile)
answerfile.close()

#Validate answer
expectedprocesscount = int(sys.argv[3])
if(len(answer) > expectedprocesscount):
    print(f"Error: Too many processes detected: expected at most {expectedprocesscount}, but got {len(answer)}")
    exit()
if(len(answer) < expectedprocesscount):
    print(f"Warning: Number of processes is less than expected: expected {expectedprocesscount}, but got {len(answer)}.")
    print("Verifier will still run, but this may not be efficient.")
allnumbers = sum(answer, start=[])
allnumbers.sort()
if(len(allnumbers)!=len(test)):
    print(f"Error: Incorrect number of tasks completed")
    exit()
for i in range(len(test)):
    if(allnumbers[i] != i):
        print(f"Error: Not all tasks completed exactly once.")
        exit()

#Run test
taskscompleted = [-1]*len(test)
processes = [0]*len(answer)
while(sum(processes) < len(test)):
    progressmade = False
    for i in range(len(processes)):
        if(processes[i] < len(answer[i])):
            nexttask = answer[i][processes[i]]
            canstart = all([taskscompleted[j]>=0 for j in test[nexttask][2]])
            if(canstart):
                starttime = 0 if processes[i] == 0 else taskscompleted[answer[i][processes[i]-1]]
                starttime = max([starttime]+[taskscompleted[j] for j in test[nexttask][2]])
                endtime = starttime+test[nexttask][1]
                taskscompleted[nexttask] = endtime
                progressmade = True
                processes[i]+=1
                if(verbose):
                    print(f"Process {i} starting task {nexttask} at time {starttime}, ending at {endtime}")
    if(not progressmade):
        print("Error: Deadlock reached")
        exit()
singlethreadedruntime = sum([i[1] for i in test])
ourruntime = max(taskscompleted)
print(f"All tasks completed in {ourruntime} minutes.\nSingle-threaded runtime is {singlethreadedruntime} minutes, for a {100*singlethreadedruntime/(ourruntime*expectedprocesscount)}% usage ratio")
