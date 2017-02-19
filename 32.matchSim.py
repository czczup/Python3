#matchSim.py
from random import *
#顶层设计(第一阶段)
def main():
    printIntro()
    #打印程序的介绍性信息
    probA,probB,n = getInputs()
    #获得程序运行所需的参数
    winsA,winsB = simNGames(n,probA,probB)
    #模拟n次比赛
    printSummary(winsA,winsB)
    #输出球员A和B获胜比赛的次数和概率
#第二阶段
def printIntro():
    print("This program simulates a game between two")
    print("There are two players,A and B")
    print("Probility(a number between 0 and 1) is used")
def getInputs():
    a = eval(input("What is the prob.play A wins?\n"))
    b = eval(input("What is the prob.play B wins?\n"))
    n = eval(input("How many games to simulate?\n"))
    return a,b,n
def simNGames(n,probA,probB):
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB
#第三阶段
def simOneGame(probA,probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB
def gameOver(a,b):
    return a==15 or b==15
def printSummary(winsA,winsB):
    n = winsA + winsB
    print("\nGames simulated:%d"%n)
    print("Wins for A:{0}({1:0.1%})".format(winsA,winsA/n))
    print("Wins for B:{0}({1:0.1%})".format(winsB,winsB/n))
    
main()
