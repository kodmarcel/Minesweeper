#adding imports
from GameEngine import GameEngine as GE
from PlayFrame import PlayFrame as PF
import sys
from tkinter import Tk

################
###Main Program#
################


class Play():

    def StartGame(self,minesAmount,height,width):
        blockWidth=50
        blockHeight=50
        '''function called when we press play'''
        self.gameEngine=GE(minesAmount,height,width)
        self.playWindow=Tk()
        self.playWindow.geometry(str(blockWidth*width+blockWidth//2)+'x'+str(blockHeight*height+blockHeight//2))#TODO: change to create a window according to field size
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
            

    def rightClick(self,event):
        if self.alive:
            x=event.x//50
            y=event.y//50
            self.gameEngine.ManageFlags(x,y)
            self.update()
            
    def update(self):
            shownField,activeMines=self.gameEngine.GetStatus()
            self.playFrame.Paint(activeMines,shownField)
            if not self.alive:print("You died")


def main():
    '''Function to run on game start'''
    play=Play()
    play.StartGame(20,10,10)#calls function to start the game









if __name__=='__main__':
    main()
