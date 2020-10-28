import random
import time

def getNums():
    nums = []
    for i in range(1,21):
        nums.append(i)
    random.shuffle(nums)
    return nums

def startTest():
    test = getNums()[-3:]
    new = [None]*3
    for i in test:
        if i == max(test):
            new[0] = i
        elif i == min(test):
            new[1] = i
        else:
            new[2] = i
    maxDif = abs(new[0] - new[2])
    minDif = abs(new[1] - new[2])

    if minDif == maxDif:
        print("Equal value: {0} {1} {2}".format(new[0],new[1],new[2]))
        answer = None
        startTest()
    elif minDif > maxDif:
        answer = new[1]
    else:
        answer = new[0]

    print("{0} | {1} | {2}".format(test[0],test[1],test[2]))
    start_time = time.time()
    try:
        ans = int(input(""))
    except ValueError:
        print("That's not an integer!")
        start()

    val = 0
    if int(ans) == answer:
        val = 1
    else:
        pass
    t = round(time.time() - start_time, 2)
    return val,t

def start():
    temp = input("Enter to start\n")
    n = 10
    score = 0
    time = []
    for i in range(n):
        val,t = startTest()
        if val == 1:
            score += 1
        else:
            pass
        time.append(t)
    avg_time = round(sum(time) / len(time), 2)
    print("You got {0}/{1} right with an average time of {2} seconds.".format(score,n,avg_time))
    print("Best time: {0}".format(min(time)))
    print("Worst time: {0}".format(max(time)))
        
start()
