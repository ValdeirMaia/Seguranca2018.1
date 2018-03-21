#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 19:23:29 2018

@author: Abimael S. Barros e Francisco Valdeir M. Bandeira
"""

vetkey = []
vetfrase = []
mat=[]

def rmLetrasRepetidas(x,y):
    for i in x:
        if i not in y:
            y.append(i)

def rmEspacos(a,b):
    for i in range(len(a)):
        if a[i] != " ":
            b.append(a[i])
            
def addDemaisLetras(x):
    abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    for i in abc:
        if i not in x:
            x.append(i)
            
def criaMatrix(x):
    aux = 0
    for i in range(5):
        l = []
        for j in range(5):
            l.append(x[j+aux])
        mat.append(l)
        aux += 5

def rmLetrasRpt(x):
    v = []
    i = 0
    while i < len(x):
        if i==(len(x)-1):
            v.append(x[i])
        elif x[i] == x[i+1]:
            if x[i] == "X":
                v.append(x[i])
                v.append("Z")
                i -= 1
            else:
                v.append(x[i])
                v.append("X")
                i -= 1
        else:
            v.append(x[i])
            v.append(x[i+1])
        i += 2
    x = v
    return x

def ultLetra(x):
    if len(x)%2 != 0:
        if x[len(x)-1] == "X":
            x.append("Z")
        else:
            x.append("X")

def criptografa(x, y):
    fc = []
    l1 = 0
    c1 = 0
    l2 = 0
    c2 = 0
    for i in range(0, len(x), +2):
        for j in range(5):
            for k in range(5):
                if y[j][k] == x[i]:
                    l1 = j
                    c1 = k
                if y[j][k] == x[i+1]:
                    l2 = j
                    c2 = k
        if l1 == l2:
            fc.append(y[l1][(c1+1)%5])
            fc.append(y[l2][(c2+1)%5])
        elif c1 == c2:
            fc.append(y[(l1+1)%5][c1])
            fc.append(y[(l2+1)%5][c2])
        else:
            fc.append(y[l1][c2])
            fc.append(y[l2][c1])
    print "A frase codificada é: ",
    print ''.join(map(str, fc))

def descriptografa(x, y):
    fd = []
    l1 = 0
    c1 = 0
    l2 = 0
    c2 = 0
    for i in range(0, len(x), +2):
        for j in range(5):
            for k in range(5):
                if y[j][k] == x[i]:
                    l1 = j
                    c1 = k
                if y[j][k] == x[i+1]:
                    l2 = j
                    c2 = k
        if l1 == l2:
            fd.append(y[l1][(c1-1)%5])
            fd.append(y[l2][(c2-1)%5])
        elif c1 == c2:
            fd.append(y[(l1-1)%5][c1])
            fd.append(y[(l2-1)%5][c2])
        else:
            fd.append(y[l1][c2])
            fd.append(y[l2][c1])
    print "A frase decodificada é: ",
    print ''.join(map(str, fd))

opcao = input("Escolha uma opcao: \n 1: CIFRAR \n 2: DESCIFRAR \n --> ")

if opcao == 1:
    key = raw_input("Insira a palavra-chave: ").upper()
    frase = raw_input("Insira a frase: ").upper()
    key = key.replace("W", "V")
    frase = frase.replace("W", "V")
            
    rmLetrasRepetidas(key,vetkey); addDemaisLetras(vetkey);
    rmEspacos(frase,vetfrase); vetfrase = rmLetrasRpt(vetfrase);
    rmLetrasRpt(vetfrase); ultLetra(vetfrase);
    criaMatrix(vetkey); criptografa(vetfrase,mat)

if opcao == 2:
    key = raw_input("Insira a palavra-chave: ").upper()
    frase = raw_input("Insira a frase cifrada: ").upper()

    rmLetrasRepetidas(key,vetkey); addDemaisLetras(vetkey);
    criaMatrix(vetkey); descriptografa(frase,mat)