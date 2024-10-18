# importing neccesary libraries
#-------------------------------------------------------------------------------

from graphics import *
from random import *
import time

#-------------------------------------------------------------------------------

class Stock():

    def __init__(self, lineWidth=5, startHeight=256, color="red"):

        self.posVar = 40
        self.negVar = 40

        self.dis = 10

        self.lineWidth = lineWidth
        self.startHeight = startHeight
        self.color = color
        self.Mode = "flat"

        self.reallyBadStock = False
        self.reallyTooGoodStock = False

        self.p1 = Point(0, startHeight)
        self.p2 = Point(dis, startHeight + randint(-3, 3))

def main():
    
    iteration = 0
    switchRate = 5

    marketTooGood = False
    almostOffScreen = 50

    marketCrisisMode = False

    Modes = ["flat", "slow rise", "slow fall", "fast rise", "fast fall", "chaotic"]
    Mode = Modes[randint(0,5)]

    win = GraphWin(width=729, height= 512)
    p1 = Point(0, startHeight)
    p2 = Point(dis, startHeight + randint(-3, 3))

    cheeseStock = Stock(color = "red")
    crackerStock = Stock(color = "blue")
    sardineStock = Stock(color = "green")

    lineList = []
    stockList = [cheeseStock, crackerStock, sardineStock]
    
    while True:
        
        iteration += 1
        
        if(iteration % switchRate == 0):

            for stock in stockList:
                if not stock.reallyTooGoodStock and not stock.reallyBadStock:
                    stock.Mode = Modes[randint(0, 5)]
                elif stock.reallyBadStock:
                    stock.Mode = Modes[3]
                else :
                    stock.Mode = Modes[4]
                    
                match Mode:
                    case "flat":
                        stock.posVar=3
                        stock.negVar=3
                    case "slow rise":
                        stock.posVar=15
                        stock.negVar=5
                    case "slow fall":
                        stock.posVar=5
                        stock.negVar=15
                    case "fast rise":
                        stock.posVar=30
                        stock.negVar=5
                    case "fast fall":
                        stock.posVar=5
                        stock.negVar=25
                    case "chaotic":
                        stock.posVar = 20
                        stock.negVar = 20
        
        if len(lineList) > win.width/dis:
            for line in lineList:
                line.move(-dis, 0)
                line.getP1().move(-dis,0)
                line.getP2().move(-dis,0)
            for stock in stockList:
                deleteLine = lineList.pop(0)
                deleteLine.undraw()
                stock.p1.move(-dis, 0)
                stock.p2.move(-dis, 0)


        for stock in stockList:
            if p2.getY() < almostOffScreen:
                marketTooGood = True
            else:
                marketTooGood = False

            if p2.getY() > win.height - 40:
                marketCrisisMode = True
            else:
                marketCrisisMode = False

            print(p2.getY())
            
            line = Line(stock.p1, stock.p2)
            line.setFill(color)
            line.setWidth(lineWidth)

            lineList.append(line)
            
            line.draw(win)
            
            stock.p1 = lineList[-1].getP2()
            stock.p2 = Point(p1.getX() + dis, p1.getY() - randint(-negVar, posVar))

        time.sleep(graphSpeed)
        
