from graphics import *
from random import *
import time

def buyRed():
    print("Buy Red")
    
def sellRed():
    print("Sell Red")

#buyRedButton = tk.Button(win, text="Buy Red", command = buyRed)
#buyRedButton.place(x=50, y=50)
#sellRedButton = tk.Button(win, text="Sell Red", command = sellRed)
#sellRedButton.place(x=100, y=50)

def stock(lineWidth=5, graphSpeed=1, startHeight=256):

    #lineWidth = 5

    posVar = 40
    negVar = 40

    dis = 10
    iteration = 0
    switchRate = 5

    #graphSpeed = 10

    marketTooGood = False
    almostOffScreen = 50

    marketCrisisMode = False

    Modes = ["flat", "slow rise", "slow fall", "fast rise", "fast fall", "chaotic"]
    Mode = Modes[randint(0,5)]

    win = GraphWin(width=729, height= 512)
    p1 = Point(0, startHeight)
    p2 = Point(dis, startHeight + randint(-3, 3))

    lineList = []

    print(Mode)
    while True:
        
        
        iteration += 1
        
        if(iteration % switchRate == 0):

            if not marketTooGood and not marketCrisisMode:
                Mode = Modes[randint(0, 5)]
                print(Mode)
            elif marketCrisisMode:
                Mode = Modes[3]
            else :
                Mode = Modes[4]
                
            match Mode:
                case "flat":
                    posVar=3
                    negVar=3
                case "slow rise":
                    posVar=15
                    negVar=5
                case "slow fall":
                    posVar=5
                    negVar=15
                case "fast rise":
                    posVar=30
                    negVar=5
                case "fast fall":
                    posVar=5
                    negVar=25
                case "chaotic":
                    posVar = 20
                    negVar = 20
        
        if len(lineList) > 72:
            for line in lineList:
                line.move(-dis, 0)
                line.getP1().move(-dis,0)
                line.getP2().move(-dis,0)
            deleteLine = lineList.pop(0)
            deleteLine.undraw()
            p1.move(-dis, 0)
            p2.move(-dis, 0)


        if p2.getY() < almostOffScreen:
            marketTooGood = True
        else:
            marketTooGood = False

        if p2.getY() > win.height - 40:
            marketCrisisMode = True
        else:
            marketCrisisMode = False

        print(p2.getY())
        
        line = Line(p1, p2)
        line.setFill("red")
        line.setWidth(lineWidth)

        lineList.append(line)
        
        line.draw(win)
        time.sleep(graphSpeed)
        p1 = lineList[-1].getP2()
        p2 = Point(p1.getX() + dis, p1.getY() - randint(-negVar, posVar))
        
stock()
