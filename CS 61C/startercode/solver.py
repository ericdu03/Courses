#Setup
import sys
if "-v" in sys.argv:
    verbose = True
    sys.argv.remove("-v")
else:
    verbose = False
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <test case> <thread count> [-v]")
    print("Finds a solution for a given test case.")
    print("test case should be a file containing the data value")
    print("The starter code automatically parses the input file for you, and writes an answer in the appropriate format")
    print("You can save your answer by piping your output to a file (assuming you have no additional print statements)")
    print(f"ex: {sys.argv[0]} Test1.txt 2 > answer.out")
    print("An optional -v argument is included, but currently does nothing. You may want to use it as a verbose flag,")
    print("so that debugging data gets printed only when verbose is set to True.")
    exit()

#Parse input
def parsetestfile(testfile):
    data = testfile.readlines()[1:]
    result = []
    for i in data:
        element = [int(j) for j in i.strip().split(" ")]
        result.append({"TaskID":element[0], "runtime":element[1], "prerequisites":element[3:]})
    return result
testfile = open(sys.argv[1])
test = parsetestfile(testfile)
testfile.close()
threadcount = int(sys.argv[2])

#Return a list of length threadcount, where each list details what each thread does
def findsolution(test, threadcount):
    #YOUR SOLUTION HERE
    time = 0
    workers = [(-1, 0) for _ in range(threadcount)] #(task ID, time of completion)
    completed = []
    result = [[] for _ in range(threadcount)]
    # print(test)
    while test:
        available_tasks = [task for task in test if all(x in completed for x in task["prerequisites"])]
        delete = []
        # print(time, available_tasks, workers, completed)
        for i in range(len(workers)):
            # print(workers[i][1])
            if workers[i][1] <= time:
                completed.append(workers[i][0])
                if available_tasks:
                    task = available_tasks.pop(0)
                    delete.append(task)
                    workers[i] = (task["TaskID"], task["runtime"] + time)
                    result[i].append(task["TaskID"])
                else:
                    workers[i] = (0, float('inf'))
        for val in delete:
            test.pop(test.index(val))
        time = min(a[1] for a in workers)
    return result



    # return [list(range(len(test)))]+[[]]*(threadcount-1)



result = findsolution(test, threadcount)
val = ""
for i in result:
    for j in i:
        val+=str(j)+","
    val=val[:-1]+";"
print(val[:-1])
