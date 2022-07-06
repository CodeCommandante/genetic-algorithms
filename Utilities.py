"""    
    Program exploring genetic algorithms.
    Copyright (C) 2021  Jim Leon

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 08:21:06 2021

@author: jimleon
"""
import random

VALUE = [5,16,9,15,8,22,1,18,14,0,17,4,2,21,7,3,12,19,13,6,20,10,11]
#WEIGHT = [5,6,20,1,16,15,19,11,9,2,3,22,18,8,21,14,10,13,7,4,23,12,17]
WEIGHT = [12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12]
KNAPWGHT = 206

def breedNewMembers(Population,ChildPerPair):
    StartSize = len(Population)
    Iterations = int(StartSize/2)*ChildPerPair
    reshufflePop(Population)
    for i in range(Iterations):
        ParentA = Population[random.randint(0,int(len(Population)/2)-1)]
        ParentB = Population[random.randint(int(len(Population)/2),len(Population)-1)]
        Population.append(reproduce(ParentA,ParentB))
    for i in range(StartSize):
        del Population[i]
    sortByValue(Population)
       
def calculateValue(Member):
    Value = 0
    for i in range(len(Member)):
        Value = Value + Member[i]
    return Value

def calculateWeight(Member):
    Weight = 0
    for i in range(len(Member)):
        if Member[i] != 0:
            Weight = Weight + WEIGHT[i]
    return Weight

def getHighestValue(Population):
    sortByValue(Population)
    return calculateValue(Population[0])

def initializePopulation(Size):
    Pop = []
    for i in range(Size):
        Candidate = []
        for j in range(len(VALUE)):
            Candidate.append(VALUE[j]*random.randint(0,1))
        Pop.append(Candidate)
    return Pop

def isExtinct(Population):
    if len(Population) <= 1:
        return True
    return False

def mutate(Child):
    Gene = random.randint(0,len(Child)-1)
    if Child[Gene] == 0:
        Child[Gene] = VALUE[Gene]
    else:
        Child[Gene] = 0

def printTopFromPop(Population,Num=1,K=0):
    print("Chromosome","          ","          Weight   ","Value","     V/W")
    print("=====================================================================")
    if isExtinct(Population):
        print('Population went extinct...')
        return
    for i in range(Num):
        W = calculateWeight(Population[i])
        V = calculateValue(Population[i])
        print(toBitString(Population[i]),"      ",str(W),"      ",str(V),"     ",str(V/W))

def reproduce(MemberA,MemberB):
    Child = []
    SpliceLen = random.randint(1,len(MemberA)-1)
    index = 0
    while index < SpliceLen:
        Child.append(MemberA[index])
        index = index + 1
    while index < len(MemberA):
        Child.append(MemberB[index])
        index = index + 1
    mutate(Child)
    return Child

def selection(Population,MemLim=5):
    sortByValue(Population)
    #remove overweight
    index = 0
    while (len(Population) > 5) and (index < len(Population)):
        if calculateWeight(Population[index]) > KNAPWGHT:
            del Population[index]
            index = index - 1
        index = index + 1
    #kill lower limit
    if len(Population) > MemLim:
        while (len(Population) > 5) and (MemLim < len(Population)):
            del Population[MemLim]
            
def reshufflePop(Population):
    for i in range(int(len(Population)/2)):
        First = random.randint(0,len(Population)-1)
        Second = random.randint(0,len(Population)-1)
        Temp = Population[First]
        Population[First] = Population[Second]
        Population[Second] = Temp
    
def sortByValue(Population,Order=0):
    if Order == 0:
        for i in range(len(Population)-1):
            j = i + 1
            while j < len(Population):
                if calculateValue(Population[i]) < calculateValue(Population[j]):
                    Temp = Population[i]
                    Population[i] = Population[j]
                    Population[j] = Temp
                j = j + 1
    else:
        for i in range(len(Population)-1):
            j = i + 1
            while j < len(Population):
                if calculateValue(Population[i]) > calculateValue(Population[j]):
                    Temp = Population[i]
                    Population[i] = Population[j]
                    Population[j] = Temp
                j = j + 1
        
def toBitString(Member):
    BitString = ""
    for i in range(len(Member)):
        if Member[i] == 0:
            BitString = BitString + '0'
        else:
            BitString = BitString + '1'
    return BitString
