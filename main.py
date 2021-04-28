import pygame
import grid
import button

width=1280
height=720
screen_size=(width,height)

pygame.init()
pygame.display.set_caption("Jeu de la vie")
screen=pygame.display.set_mode(screen_size)
clock=pygame.time.Clock()
fps=20

#Colors
black=(0,0,0)
blue=(15, 0, 102)
white=(255,255,255)

scaler=20
offset=1

ButtonWidth=200
ButtonHeight=100

Grid = grid.Grid(width/1.22,height,scaler,offset)
Grid.first_gen()

Generate=button.Button(white,width-(ButtonWidth*1.1),height-(ButtonHeight*1.1),ButtonWidth,ButtonHeight,"Generate")
screen.fill(black)

#Texte de la generation
gen_num=0
font = pygame.font.SysFont('Arial', 30)
text = font.render('Generations:'+str(gen_num), True, white,black)
textRect = text.get_rect()
textRect.center = (width-(textRect.width) , textRect.height)

run= True

while run:
    clock.tick(fps)
    
    Generate.draw(screen)
    mousePosition=pygame.mouse.get_pos()
    screen.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if(Generate.isOver(mousePosition)):
                gen_num+=1
                Grid.ChangeGeneration(alive_color=blue,dead_color=white,surface=screen)
                text = font.render('Generations:'+str(gen_num), True, white,black)
    
    
    pygame.display.update()
