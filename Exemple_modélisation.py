# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:30:24 2021

@author: ericf
"""
import numpy as np

nb = 5
size = 10
nb_type = 4
reserves = 0
lim_depl = 1


class abeilles:
    def __ini__(self, ntype,nourriture,x,y):
        self.ntype = ntype
        self.nourriture = nourriture
        self.x = x
        self.y = y
        
def ini_une_abeilles(a,nb_type,size):
    a.ntype = np.random.choice(nb_type);
    while(a.ntype == 0):
        a.ntype = np.random.choice(nb_type)
        a.nourriture = 0
        a.x = np.random.choice(size)
        a.y = np.random.choice(size)
    

def nb_abeilles(nb):
    l = []
    for i in range(nb):
        l.append(abeilles())
        
    return l

tab_abeilles = nb_abeilles(nb)

def ini_abeilles(nb,tab,nb_type,size):
    for i in range(nb):
        tab[i].ntype = np.random.choice(nb_type)
        while(tab[i].ntype == 0):
            tab[i].ntype = np.random.choice(nb_type)
        tab[i].nourriture = 0
        tab[i].x = np.random.choice(size)
        tab[i].y = np.random.choice(size)
        
ini_abeilles(nb,tab_abeilles,nb_type,size)

cell = np.zeros((size,size))
for i in range(nb):
    cell[tab_abeilles[i].x,tab_abeilles[i].y] = tab_abeilles[i].ntype
print(cell)

def deplacement(tab,lim,size):
    for i in range(lim):
        
        for i in range(nb):
            a = np.random.choice(4)
    
    #vers le haut
            if(a == 0):
                if(tab[i].y < size-1):
                    tab[i].y = tab[i].y + 1
    #vers le bas
            if(a == 1):
                if(tab[i].y > 0):
                    tab[i].y = tab[i].y - 1
    #vers la gauche
            if(a == 2):
                if(tab[i].x > 0):
                    tab[i].x = tab[i].x - 1
    #vers la droite
            if(a == 3):
                if(tab[i].x < size-1):
                    tab[i].x = tab[i].x + 1

cell = np.zeros((size,size))
deplacement(tab_abeilles,lim_depl,size)
for i in range(nb):
    cell[tab_abeilles[i].x,tab_abeilles[i].y] = tab_abeilles[i].ntype
print(cell)

# actions

def birth(nb,tab,size):
    if(reserve_ruche(tab,size) >= 30):
        nb = nb + 1
        return tab.append(ini_une_abeilles(abeilles()))

def obt_pollen(nb,tab,size):
    for i in range(nb):
        if(tab[i].ntype == 2):
            if(tab[i].x == 0 or tab[i].x == size-1 or tab[i].y == 0 or tab[i].y == size-1):
                tab[i].nourriture == 1

def reserve_ruche(nb,tab,reserve):
    for i in range(nb):
        reserve = reserve + tab[i].nourriture
        tab[i].nourriture = 0
    return reserve

def t_hiver(tab):
    return 0

def essaim(tab):
    return 0

def esp(tab):
    return 0