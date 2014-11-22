#imports
import sys
import tkinter as tk


class PlayFrame(tk.Frame):
    def __init__(self,parent,height,width,blockHeight,blockWidth):
        tk.Frame.__init__(self,parent)
        self.parent=parent
        self.height=height
        self.width=width
        self.size=width*height
        self.blockWidth=blockWidth
        self.blockHeight=blockHeight

        #widgets
        self.minesIndicator=tk.Label(self,fg='red',bg='black')
        self.canvas=tk.Canvas(self,\
            height=self.height*self.blockHeight,width=self.width*self.blockWidth,bg="grey")

        self.minesIndicator.pack()
        self.canvas.pack()
        

        
    def Paint(self,activeMines,shownField):
        '''Function to paint on screen'''
        
        self.minesIndicator['text']=activeMines
        self.canvas.delete('all')
        for i in range(self.size):
            block=shownField[i]
            self.canvas.create_rectangle(\
                (i%self.width)*self.blockWidth,(i//self.width)*self.blockHeight,\
                (i%self.width)*self.blockWidth+self.blockWidth,\
                (i//self.width)*self.blockHeight+self.blockHeight)
               
            
            if block=='F':
                self.canvas.create_text(\
                (i%self.width)*self.blockWidth+self.blockWidth//2,(i//self.width)*self.blockHeight+self.blockHeight//2,\
                                        text='F',fill="blue",width=10)

            elif block=='M':
               self.canvas.create_text(\
                (i%self.width)*self.blockWidth+self.blockWidth//2,(i//self.width)*self.blockHeight+self.blockHeight//2,\
                                        text='M',fill="red",width=10)
            elif block=='X':
                pass
            elif 0<=block<=8 :
                 self.canvas.create_text(\
                (i%self.width)*self.blockWidth+self.blockWidth//2,(i//self.width)*self.blockHeight+self.blockHeight//2,\
                                        text=str(block),width=10)

        
