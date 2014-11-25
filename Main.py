#adding imports
from GameEngine import GameEngine as GE
from PlayFrame import PlayFrame as PF
import sys
from tkinter import Tk,Label,Frame

################
###Main Program#
################


class Play():

    def StartGame(self,minesAmount,height,width):
        blockWidth=50
        blockHeight=50
        self.minesAmount=minesAmount
        '''function called when we press play'''
        self.gameEngine=GE(minesAmount,height,width)
        self.playWindow=Tk()
        self.playWindow.geometry(str(blockWidth*width+blockWidth//2)+'x'+str(blockHeight*height+blockHeight//2)+'+200+200')#TODO: change to create a window according to field size
        self.playWindow.title("Minesweeper")
        self.playFrame=PF(self.playWindow,height,width,blockHeight,blockWidth)
        self.playFrame.canvas.bind("<Button-1>", self.leftClick)
        self.playFrame.canvas.bind("<Button-3>", self.rightClick)
        self.playFrame.pack()
        
        self.alive=True
        self.update()

    def leftClick(self,event):
        if self.alive:
            x=event.x//50
            y=event.y//50
            self.alive=self.gameEngine.ExposeBlock(x,y)
            self.update()
        else:
            self.DeadFrame()
            

    def rightClick(self,event):
        if self.alive:
            x=event.x//50
            y=event.y//50
            self.gameEngine.ManageFlags(x,y)
            self.update()
            
    def update(self):
            shownField,activeMines=self.gameEngine.GetStatus()
            self.playFrame.Paint(activeMines,shownField)
            self.checkWin(shownField)

    def checkWin(self,shownField):
        currentBlocks=sum([1 for x in shownField if x=='X' or x=='F'])
        if currentBlocks==self.minesAmount:
            self.WinFrame()

    def DeadFrame(self):
        self.playFrame.destroy()
        self.deadScreen=Frame(self.playWindow,bg="red")
        self.deadScreen.pack(fill="both", expand=1)
        self.deadText=Label(self.deadScreen,text="You stepped on a mine!\nClick here to try again.",fg="black",bg="red")
        self.deadText.bind("<Button-1>",self.onClickRestart)
        self.deadText.pack()

    def WinFrame(self):
        self.playFrame.destroy()
        self.winScreen=Frame(self.playWindow,bg="blue")
        self.winScreen.pack(fill="both", expand=1)
        self.winText=Label(self.winScreen,text="You won!\nClick here to try again.",fg="yellow",bg="blue")
        self.winText.bind("<Button-1>",self.onClickRestart)
        self.winText.pack()


        
    def onClickRestart(self,event):
        self.playWindow.destroy()
        self.StartGame(10,10,10)

def main():
    '''Function to run on game start'''
    play=Play()
    play.StartGame(10,10,10)#calls function to start the game









if __name__=='__main__':
    main()
