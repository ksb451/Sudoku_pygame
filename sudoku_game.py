import pygame

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

class cell:
    def __init__(self,x,y,width):
        self.x_cor=x
        self.y_cor=y
        self.width=width
        self.selected=False

class Sudoku_Grid:
    def __init__(self,width):
        self.Cells=[]

