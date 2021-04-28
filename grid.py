import pygame
import random

class Grid:
    def __init__(self,width,height,scale,offset):
        self.scale = scale
        self.columns=int(height/scale)
        self.rows = int(width/scale)
        self.size=(self.rows,self.columns)
        self.array=[[0 for a in range(self.columns)] for b in range(self.rows)] 
        self.offset = offset

    def first_gen(self):
        #Créer la premiere generation
        for x in range(self.rows):
            for y in range(self.columns):
                #Créer un valeur pour chaque cellule tel que 0 = cellule morte et 1 = cellule vivante
                self.array[x][y]=random.randint(0,1)

    def ChangeGeneration(self,alive_color,dead_color,surface):
        #afficher le tableau
        for x in range(self.rows):
            for y in range(self.columns):
                #La position de la cellule sur l'ecran
                y_pos = y*self.scale
                x_pos = x*self.scale

                if self.array[x][y] == 1:
                    #pygame.draw.rect(surface,couleur,[position x,position y,largeur,longueur])
                    #si la cellule donnée est egal a 1 cad cellule vivante
                    pygame.draw.rect(surface,alive_color,[x_pos,y_pos,self.scale-self.offset,self.scale-self.offset])
                else:
                    #sinon, alors si elle est egal a zero cad cellule morte
                    pygame.draw.rect(surface,dead_color,[x_pos,y_pos,self.scale-self.offset,self.scale-self.offset])
        #Créer un nouveau 2 dimension array pour storer la generation suivante
        next=[[0 for i in range(self.columns)] for j in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.columns):
                valeur = self.array[x][y]
                voisins=self.get_voisins(x,y)
                #si cellule est morte et voisins = 3 alors cellule devient vivante
                if valeur == 0 and voisins == 3:
                    next[x][y] = 1
                #si cellule est vivante et voisins different de 2 et 3 alors cellule devient morte    
                elif valeur == 1 and (voisins < 2 or voisins > 3):
                    next[x][y] = 0
                #sinon, cellule ne change pas
                else:
                    next[x][y] = valeur
        #storer le nouveau tableau dans l'ancient pour le reafficher a la generation suivante
        self.array = next

    def get_voisins(self,x,y):
        total=0
        #un voisin avant et deux apres car 2 est exclue donc un avant et un apres
        for n in range(-1,2):
            #la meme chose pour y
            for m in range(-1,2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total+=self.array[x_edge][y_edge]

        total-=self.array[x][y]
        return total