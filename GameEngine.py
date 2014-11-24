#imports
import random


class GameEngine():

    def __init__(self,minesAmount,height,width):
        '''creates a gameEngine which have handles all player's commands'''
        self.height=height
        self.width=width
        self.minesAmount=minesAmount
        self.size=height*width
        self.minesActive=minesAmount
        self.alive=True
        self.mines=[]
        #Generating random mines
        for i in range(minesAmount):
            mine=random.randrange(1,self.size+1)
            while mine in self.mines:#we get random number and repeat if we got a number we already have
                mine=random.randrange(1,self.size+1)
            self.mines.append(mine)
        #generating field
        self.field=[]
        for i in range(self.size):
            #we assign a number of mines in vicinity of block to each block or M if there is a mine in the block
            self.field.append(self.MinesInVicinity(self.mines,i))
        #generating field s it is shown to player
        self.shownField=['X' for i in range(self.size)]#X indicates unexposed block


    def MinesInVicinity(self,mines,i):
        '''method that returns amount of mines in neighbouring blocks of a block i'''
        if i in mines:return 'M'#M indicates that there is a mine in the block
        width=self.width
        vicinity=[i-width-1,i-1,i+width-1,i-width,i+width,i-width+1,i+1,i+width+1]
        nearLeftEdge=i%width==0
        nearRightEdge=i%width==width-1
        if nearLeftEdge:vicinity=vicinity[3:]#excluding blocks that are on other side of the field
        elif nearRightEdge:vicinity=vicinity[:-3]
        
        amount=0
        for mine in mines:
            if mine in vicinity:
                amount+=1
        return amount


    def ExposeBlock(self,x,y):
        '''method that makes player move, changes shown field and returns player state'''
        block=y*self.width+x
        if block>self.size or block<0:#checking if input is wrong
            print('Wrong input')
            return self.alive

        
        if self.shownField[block]=='F':#checking if block has been flagged by player
            print('You belive there may be a mine! If you really want to unflag this block, right click it')
            return self.alive
        
        elif self.shownField[block]!='X':#checking if block is already exposed)
            return self.alive
        
        else:
            if self.field[block]=='M':#checking if there is a mine in the block
                self.alive=False
                print('You died')
            self.shownField[block]=self.field[block]#showing clicked block to player
            if self.field[block]==0:
                self.isZero(block)
        return self.alive



    def ManageFlags(self,x,y):
        '''Method that puts or takes a flag from block'''
        block=y*self.width+x
        if self.shownField[block]=='X':#if block is unexposed we flag it
            self.minesActive-=1#player thinks he eliminated one mine-> we show him number of remaining ones
            self.shownField[block]='F'
        elif self.shownField[block]=='F':#if block is flagged we unflag it
            self.minesActive+=1
            self.shownField[block]='X'
        else:
            print("Can't flag this")
        return

    def isZero(self,block):
        '''function that is called when block with value 0 is exposed'''
        vicinity=[block-self.width-1,block-1,block+self.width-1,block-self.width,block+self.width,block-self.width+1,block+1,block+self.width+1]
        nearLeftEdge=block%self.width==0
        nearRightEdge=block%self.width==self.width-1
        if nearLeftEdge:vicinity=vicinity[3:]#excluding blocks that are on other side of the field
        elif nearRightEdge:vicinity=vicinity[:-3]
        vicinity=[x for x in vicinity if 0<=x<self.size]
        for neighbour in vicinity:
            xNeighbour=neighbour%self.width
            yNeighbour=neighbour//self.width
            self.ExposeBlock(xNeighbour,yNeighbour)
                
        

    
    def GetStatus(self):
        '''Method that returns current shownField and minesActive'''
        return self.shownField,self.minesActive




            
