# Wiley Sheehy
# Robin Adams
# Headlands Prep
# Intro to CS S1
# 10/14/21

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
        self.price = 600 - self.p2.getY()

        self.stockOwned = 0

    def buyStock(self, wallet, amount):
        self.price = 600 - self.p2.getY()
        if wallet > self.price * amount:
            wallet -= self.price * amount
            self.stockOwned += amount
            print("Bought {0}\nYou have ${1} and {2} {3} remaining".format(self.Name, wallet, self.stockOwned, self.Name))
        else:
            wallet -= self.price * (wallet // self.price)
            self.stockOwned += (wallet // self.price)
            print("You don't have enough money to buy {}".format(self.Name))
        return wallet
            
    def sellStock(self, wallet, amount):
        self.price = 600 - self.p2.getY()
        if self.stockOwned > amount - 1:
            self.stockOwned -= amount
            wallet += self.price * amount
            print("Sold {0}\nYou have ${1} and {2} {3} remaining".format(self.Name, wallet, self.stockOwned, self.Name))
        else:
            self.stockOwned -= self.stockOwned
            wallet += self.price * self.stockOwned
            print("You don't have any {} left".format(self.Name))
        return wallet

def main():

    amount = 1
    
    iteration = 0
    switchRate = 5
    almostOffScreen = 500
    graphSpeed = 0.25
    pauseCheck = True

    Modes = ["flat", "slow rise", "slow fall", "fast rise", "fast fall", "chaotic"]
    Mode = Modes[randint(0,5)]

    win = GraphWin(width=800, height= 600)

    cheeseStock = Stock("cheeseStock",   color = "red")
    sardineStock = Stock("sardineStock", color = "green")
    crackerStock = Stock("crackerStock", color = "blue")

    wallet = 1000

    """ Buttons """

    # Buy Red Button
    br1 = Point(10, 410)
    br2 = Point(220, 495)
    buyRedButton = Rectangle(br1, br2)
    buyRedButton.setFill("red")
    buyRedButton.draw(win)
    textP = Point((br1.getX() + br2.getX())/2, (br1.getY() + br2.getY())/2)
    buyText = Text(textP, "Buy Cheese Stock")
    buyText.draw(win)

    # Sell Red Button
    sr1 = Point(10, 505)
    sr2 = Point(220, 590)
    sellRedButton = Rectangle(sr1, sr2)
    sellRedButton.setFill("red")
    sellRedButton.draw(win)
    textP = Point((sr1.getX() + sr2.getX())/2, (sr1.getY() + sr2.getY())/2)
    buyText = Text(textP, "Sell Cheese Stock")
    buyText.draw(win)

    # Buy Green Button
    bg1 = Point(240, 410)
    bg2 = Point(450, 495)
    buyGreenButton = Rectangle(bg1, bg2)
    buyGreenButton.setFill("green")
    buyGreenButton.draw(win)
    textP = Point((bg1.getX() + bg2.getX())/2, (bg1.getY() + bg2.getY())/2)
    buyText = Text(textP, "Buy Sardine Stock")
    buyText.draw(win)

    # Sell Green Button
    sg1 = Point(240, 505)
    sg2 = Point(450, 590)
    sellGreenButton = Rectangle(sg1, sg2)
    sellGreenButton.setFill("green")
    sellGreenButton.draw(win)
    textP = Point((sg1.getX() + sg2.getX())/2, (sg1.getY() + sg2.getY())/2)
    buyText = Text(textP, "Sell Sardine Stock")
    buyText.draw(win)

    # Buy Blue Button
    bb1 = Point(470, 410)
    bb2 = Point(690, 495)
    buyBlueButton = Rectangle(bb1, bb2)
    buyBlueButton.setFill("blue")
    buyBlueButton.draw(win)
    textP = Point((bb1.getX() + bb2.getX())/2, (bb1.getY() + bb2.getY())/2)
    buyText = Text(textP, "Buy Cracker Stock")
    buyText.draw(win)

    # Sell Blue Button
    sb1 = Point(470, 505)
    sb2 = Point(690, 590)
    sellBlueButton = Rectangle(sb1, sb2)
    sellBlueButton.setFill("blue")
    sellBlueButton.draw(win)
    textP = Point((sb1.getX() + sb2.getX())/2, (sb1.getY() + sb2.getY())/2)
    buyText = Text(textP, "Sell Cracker Stock")
    buyText.draw(win)

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
                pauseCheck = False
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
            if p2Y > win.height - 200:
                p2Y = win.height - 200
            stock.p2 = Point(stock.p1.getX() + stock.dis, p2Y)

        if iteration % switchRate*randint(1,3) == 0:

            """ Buy and Sell Stocks """

            # Get mouse click
            mousePoint = win.getMouse()

            mouseX = mousePoint.getX()
            mouseY = mousePoint.getY()

            # Buy Red Stock
            if mouseX > br1.getX() and mouseX < br2.getX():
                if mouseY > br1.getY() and mouseY < br2.getY():
                    wallet = cheeseStock.buyStock(wallet, amount)

            # Sell Red Stock
            if mouseX > sr1.getX() and mouseX < sr2.getX():
                if mouseY > sr1.getY() and mouseY < sr2.getY():
                    wallet = cheeseStock.sellStock(wallet, amount)

            # Buy Green Stock
            if mouseX > bg1.getX() and mouseX < bg2.getX():
                if mouseY > bg1.getY() and mouseY < bg2.getY():
                    wallet = sardineStock.buyStock(wallet, amount)

            # Sell Green Stock
            if mouseX > sg1.getX() and mouseX < sg2.getX():
                if mouseY > sg1.getY() and mouseY < sg2.getY():
                    wallet = sardineStock.sellStock(wallet, amount)

            # Buy Blue Stock
            if mouseX > bb1.getX() and mouseX < bb2.getX():
                if mouseY > bb1.getY() and mouseY < bb2.getY():
                    wallet = crackerStock.buyStock(wallet, amount)

            # Sell Blue Stock
            if mouseX > sb1.getX() and mouseX < sb2.getX():
                if mouseY > sb1.getY() and mouseY < sb2.getY():
                    wallet = crackerStock.sellStock(wallet, amount)

        if pauseCheck:
            time.sleep(graphSpeed)
            
main()
