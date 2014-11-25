#adding imports
from GameEngine import GameEngine as GE
from PlayFrame import PlayFrame as PF
import sys
from tkinter import Tk,Label,Frame,Button,messagebox,Scale,IntVar

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
        self.playWindow.geometry(str(blockWidth*width+blockWidth//2)+'x'+str(blockHeight*height+blockHeight//2)+'+200+200')
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
        main=MainMenu()
        main.main()





class MainMenu():
    def main(self):
        '''Function to run on game start'''
        self.mainMenu=Tk()
        self.mainMenu.geometry('200x300+200+200')
        self.mainMenu.title("Minesweeper")
        playButton=Button(self.mainMenu,text='Play',command=lambda:self.startPlay(None))

        self.height= IntVar()
        self.width= IntVar()
        self.minesAmount= IntVar()

        self.height.set(10)
        self.width.set(10)
        self.minesAmount.set(10)

        playButton.pack()
        
        xSlider=Scale(self.mainMenu,orient='horizontal',length=150,width=15,label='Height',sliderlength=20,from_=1,to=15,tickinterval=0,variable=self.height).pack()
        ySlider=Scale(self.mainMenu,orient='horizontal',length=150,width=15,label='Width',sliderlength=20,from_=1,to=15,tickinterval=0,variable=self.width).pack()      
        minesSlider=Scale(self.mainMenu,orient='horizontal',length=150,width=15,label='Mines',sliderlength=20,from_=0,to=15*15-1,tickinterval=0,variable=self.minesAmount).pack()
        
        aboutButton=Button(self.mainMenu,text='About',command=self.about)
        quitButton=Button(self.mainMenu,text='Quit',command=self.quitApp)

        
        
        aboutButton.pack()
        quitButton.pack()

    def startPlay(self,event):
        play=Play()
        minesAmount=self.minesAmount.get()
        height=self.height.get()
        width=self.width.get()
        if minesAmount>width*height-1:
            messagebox.showerror(title='Error',message="Amount of mines can't be bigger than total size of the field. Plese try again.")
            return
        self.mainMenu.destroy()
        play.StartGame(minesAmount,height,width)

    def about(self):
        messagebox.showinfo(title='About',message='Author:Marcel Salmič.')
        
    def quitApp(self):
        self.mainMenu.destroy()


if __name__=='__main__':
    main=MainMenu()
    main.main()
