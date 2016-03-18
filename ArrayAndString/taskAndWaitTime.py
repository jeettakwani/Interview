__author__ = 'jtakwani'
'''
Given an array of task and k wait time for which a repeated task needs
to wait k time to execute again. return overall unit time it
will take to complete all the task.
Example:
1. A B C D and k = 3
ans: 4 (execute order A B C D)
2. A B A D and k = 3
ans: 6 (execute order A B . . A D)
3. A A A A and k =3
ans: 13 (A . . . A . . . A . . . A)
4. A B C A C B D A and k = 4
ans: 11 (A B C . . A .C B D A )
'''

def waitTime(tasks,taskWaitTime):
    time = {}
    totalTime = 0
    for t in tasks:
        if t in time and totalTime - time[t] < taskWaitTime:
            totalTime = time[t] + taskWaitTime

        totalTime += 1
        time[t] = totalTime

    print totalTime


waitTime([1,2,3,1,3,2,4,1],4)
waitTime([1,2,3,4],3)
waitTime([1,2,1,3],3)
waitTime([1,1,1,1,],3)