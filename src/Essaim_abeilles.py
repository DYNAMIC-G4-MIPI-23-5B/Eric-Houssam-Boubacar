# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:30:24 2021

@author: ericf
"""
import numpy as np

nb = 20
size = 12
nb_type = 4
reserves = 0
t = 7

class abeilles:
    def __ini__(self, ntype,nourriture,x,y,nt):
        self.ntype = ntype
        self.nourriture = nourriture
        self.x = x
        self.y = y
        self.nt = nt
        
def ini_une_abeille(ab,nb_type,size):
    ab.ntype = np.random.choice(nb_type)
    while(ab.ntype == 0 or ab.ntype > 3):
        ab.ntype = np.random.choice(nb_type)
    ab.nourriture = 0
    ab.x = np.random.choice(size//2)
    ab.y = np.random.choice(size)
    if(ab.ntype == 1):
        ab.nt = -25
    if(ab.ntype == 2):
        ab.nt = 0
    if(ab.ntype == 3):
        ab.nt = 15

def nb_abeilles(nb):
    l = []
    for i in range(nb):
        l.append(abeilles())
        
    return l

tab_abeilles = nb_abeilles(nb)

def ini_abeilles(nb,tab,nb_type,size):
    for i in range(nb):
        if(i == 0):
            tab[i].ntype = 1
        else:
            tab[i].ntype = np.random.choice(nb_type)
            while(tab[i].ntype <= 1 or tab[i].ntype > 3):
                tab[i].ntype = np.random.choice(nb_type)
        tab[i].nourriture = 0
        tab[i].x = np.random.choice(size//2)
        tab[i].y = np.random.choice(size)
        if(tab[i].ntype == 1):
            tab[i].nt = -25
        if(tab[i].ntype == 2):
            tab[i].nt = 0
        if(tab[i].ntype == 3):
            tab[i].nt = 15
        
ini_abeilles(nb,tab_abeilles,nb_type,size)

def show_world(cell,nb,tab,size):
    for i in range(nb):
        cell[tab[i].y,tab[i].x] = tab[i].ntype
    print(cell)

cell = np.zeros((size,size))
show_world(cell,nb,tab_abeilles,size)
cell = np.zeros((size,size))

def depl_ouv(ab,x,y):
    if(ab.x != x):
        if(ab.x < x):
            ab.x = ab.x + 1
        else:
            ab.x = ab.x - 1
    if(ab.y != y):
        if(ab.y < y):
            ab.y = ab.y + 1
        else:
            ab.y = ab.y - 1

def deplacement(ab,size):
    if(ab.ntype == 2 and ab.nourriture == 0):
        depl_ouv(ab,ab.x,size-1)
    else:
        a = np.random.choice(4)
    
    #vers le haut
        if(a == 0):
            if(ab.y < size-1):
                ab.y = ab.y + 1
    #vers le bas
        if(a == 1):
            if(ab.y > 0):
                ab.y = ab.y - 1
    #vers la gauche
        if(a == 2):
            if(ab.x > 0):
                ab.x = ab.x - 1
    #vers la droite
        if(a == 3):
            if(ab.x < size-1):
                ab.x = ab.x + 1


# actions

def birth(nb,tab):
    nb = nb + 1
    return tab.append(ini_une_abeille(abeilles()))
    
def death(nb,tab):
    for i in range(nb):
        if(tab[i].nt > t):
            nb = nb - 1
            tab.pop(i)

def obt_pollen(nb,tab,size):
    for i in range(nb):
        if(tab[i].ntype == 2):
            if(tab[i].x == size-2 or tab[i].x == size-1):
                tab[i].nourriture == 1

def reserve_ruche(nb,tab,reserve):
    for i in range(nb):
        reserve = reserve + tab[i].nourriture
        tab[i].nourriture = 0
    return reserve

def reine_des_abeilles(tab,size,nb):
    for i in range(nb):
        if(tab[i].ntype == 1):
            birth(nb,tab,size)

def faux_bourdon(tab,size,nb):
    for i in range(nb):
        if(tab[i].ntype == 3):
            death(nb,tab,i)

def essaim(tab,nb,cell,size):
    if(tab[0].ntype == 1):
        tab[1].x = tab[0].x - 1
        tab[1].y = tab[0].y - 1
        for i in range(1,nb):
            tab[i].x = tab[0].x + i
            tab[i].y = tab[0].y + i

for i in range(t):
    for i in range(nb):
        deplacement(tab_abeilles[i],size)
    obt_pollen(nb,tab_abeilles,size)
    show_world(cell,nb,tab_abeilles,size)
    cell = np.zeros((size,size))

