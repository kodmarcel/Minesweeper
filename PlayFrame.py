#imports
import sys
import tkinter as tk
import random


class PlayFrame():
    def __init__(self,width,height,shownField,ActiveMines):


#functions
def minesInVicinity(mines, i, j,width):
    neighbourMines=0
    position=i*width+j
    neighbours=[position-width-1,position-width,position-width+1,position+width+1,position-width-1,position-width,position-1,position+1]
    for mine in mines:
        if mine in neighbours:
            neighbourMines+=1
        elif mine==position:
            neighbourMines='M'
            break

    return neighbourMines



#paint function
def paint():
    minesIndicator=Label(playGui,text=str(minesAmount),fg='red',bg='black')
