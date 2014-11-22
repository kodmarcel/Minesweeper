#adding imports
from GameEngine import GameEngine as GE
from PlayFrame import PlayFrame as PF
import sys
from tkinter import Tk

def StartGame(minesAmount,height,width):
    blockWidth=50
    blockHeight=50
    '''function called when we press play'''
    gameEngine=GE(minesAmount,height,width)
    playWindow=Tk()
    playWindow.geometry(str(blockWidth*width)+'x'+str(blockHeight*height))#TODO: change to create a window according to field size
    playWindow.title("Minesweeper")
    shownField,activeMines=gameEngine.GetStatus()
    playFrame=PF(playWindow,height,width,blockHeight,blockWidth)
    playFrame.pack()

    alive=True
    playFrame.paint(activeMines,shownField)
    
    '''
    while (alive):
        input=getInput()
        #TODO:handle input and game calling
        shownField=gameEngine.GetShownField()
        activeMines=gameEngine.GetMinesActive()    
    '''


    
def main():
    '''Function to run on game start'''
    StartGame(20,10,10)#calls function to start the game









if __name__=='__main__':
    main()
