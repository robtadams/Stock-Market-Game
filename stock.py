# importing neccesary libraries
#-------------------------------------------------------------------------------

from graphics import *
from random import *
import time

#-------------------------------------------------------------------------------

class Stock():

    def __init__(self, name, lineWidth=5, startHeight=256, color="red"):

        self.posVar = 40
        self.negVar = 40

        self.dis = 10
        self.lineList = []

        self.lineWidth = lineWidth
        self.startHeight = startHeight
        self.color = color
        self.Mode = "flat"
        self.Name = name

        self.reallyBadStock = False
        self.reallyTooGoodStock = False

        self.p1 = Point(0, startHeight)
        self.p2 = Point(self.dis, startHeight + randint(-3, 3))

    def buyStock(self):
        print("Bought {}".format(self.Name))

    def sellStock(self):
        print("Sold {}".format(self.Name))

def main():
    
    iteration = 0
    switchRate = 5
    almostOffScreen = 500
    graphSpeed = 0

    Modes = ["flat", "slow rise", "slow fall", "fast rise", "fast fall", "chaotic"]
    Mode = Modes[randint(0,5)]

    win = GraphWin(width=729, height= 512)

    cheeseStock = Stock("cheeseStock",   color = "red")
    crackerStock = Stock("crackerStock", color = "blue")
    sardineStock = Stock("sardineStock", color = "green")

    #buyCheeseButton = tk.Button(win, text="Buy Cheese", command = cheeseStock.buyStock())
    #buyCheeseButton.place(x=50, y=50)
    #sellCheeseButton = tk.Button(win, text="Sell Cheese", command = cheeseStock.sellStock())
    #sellCheeseButton.place(x=100, y=50)

    stockList = [cheeseStock, crackerStock, sardineStock]
    
    while True:
        
        iteration += 1

        for stock in stockList:
            
            if(iteration % switchRate == 0):

                    if not stock.reallyTooGoodStock and not stock.reallyBadStock:
                        stock.Mode = Modes[randint(0, 5)]
                    elif stock.reallyBadStock:
                        stock.Mode = Modes[3]
                    else :
                        stock.Mode = Modes[4]
                        
                    match stock.Mode:
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

                    #print("{0}: {1} mode".format(stock.Name, stock.Mode))
            
            if len(stock.lineList) > (win.width/stock.dis):
                for line in stock.lineList:
                    line.move(-stock.dis, 0)
                    line.getP1().move(-stock.dis,0)
                    line.getP2().move(-stock.dis,0)
                #for stock in stockList:
                deleteLine = stock.lineList.pop(0)
                deleteLine.undraw()
                
                # Keep an eye out on these lines
                stock.p1.move(-stock.dis, 0)
                stock.p2.move(-stock.dis, 0)

            if stock.p2.getY() > almostOffScreen:
                stock.reallyBadStock = True
            else:
                stock.reallyBadStock = False

            if stock.p2.getY() < 40:
                stock.reallyTooGoodStock = True
            else:
                stock.reallyTooGoodStock = False
            
            line = Line(stock.p1, stock.p2)
            line.setFill(stock.color)
            line.setWidth(stock.lineWidth)

            stock.lineList.append(line)
            
            line.draw(win)
            
            stock.p1 = stock.lineList[-1].getP2()
            p2Y = stock.p1.getY() - randint(-stock.negVar, stock.posVar)
            if p2Y < 0:
                p2Y = 0
            if p2Y > win.height:
                p2Y = win.height
            stock.p2 = Point(stock.p1.getX() + stock.dis, p2Y)
        
main()
