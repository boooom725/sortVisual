import pygame as pg
import sys
import random as rnd
import time

class Node:

    def __init__(self, val):
        self.val = val
        self.color = (255,255,255)

    def draw(self, win, x, width):
        pg.draw.rect(win, self.color, (x, 550 - self.val, width, self.val))



pg.init()

win = pg.display.set_mode((800,600), 0, 32)



List = []

N = 100 



def  Randomize():
    List = []
    for i in range(N):
        List.append(Node(rnd.randint(1, 500)))
    return List

List = Randomize()


width = (800-2*50)/len(List)
width -= (len(List)-1) / len(List)


def swap(ide, pos):
    a = List[ide]
    List[ide] = List[pos]
    List[pos] = a




def BruteForce():

    pos = 0
    while pos < len(List):
        time.sleep(0.04)
        best = float('inf')
        ide = 0
        for ind in range(len(List)):
            val = List[ind].val
            if val < best and ind >= pos:
                best = val
                ide = ind
        
        List[ide].color = (255,0,0)
        List[pos].color = (255,0,0)

        swap(ide,pos)
        

        win.fill((60,60,60))
        for ind in range(len(List)):
            List[ind].draw(win, ind*width + 50 + ind, width)
        pg.display.update()

        List[ide].color = (255,255,255)
        List[pos].color = (0,255,0)

        pos+=1
    
def BubbleSort():
    
    
    end = len(List)-1

    while end > 0:
        ind = 0
        while ind < end and ind+1 < len(List):
            

            List[ind].color = (255,0,0)
            List[ind+1].color = (255,0,0)

            if List[ind].val > List[ind+1].val:
                swap(ind, ind+1)

            
            
            win.fill((60,60,60))
            for q in range(len(List)):
                List[q].draw(win, q*width + 50 + q, width)
            pg.display.update()

            
            List[ind].color = (255,255,255)
            List[ind+1].color = (0,255,0)

            ind += 1


            
        
        end -= 1

        






count = 0

rel = False
done = False

running = True

while running:

    win.fill((60,60,60))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if rel:
                    if not done:
                        count += 1
                        if count == 1:
                            print('bruteforce')
                            BruteForce()
                            done = True
                        elif count == 2:
                            print('BubbleSort')
                            BubbleSort()
                            done = True
                            count = 0
                    else:
                        print('Reset')
                        List = Randomize()
                        done = False
                                       
                    
                        
                rel = False

        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                rel = True

    


    for ind in range(len(List)):

        List[ind].draw(win, ind*width + 50 + ind, width)
    
    

    pg.display.update()
            

pg.quit()
sys.exit()