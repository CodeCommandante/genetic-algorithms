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
Created on Sun Feb  7 16:17:23 2021

@author: jimleon
"""
import matplotlib.pyplot as plt
import Utilities as utils

def plotCurrentBest(plt,t,Pop,cs='go'):
    W = 0
    if utils.isExtinct(Pop) == True:
        W = 0
    else:
        W = utils.calculateWeight(Pop[0])
    plt.plot(t,W,cs)
    plt.pause(0.01)
    
def plotGeneralTrend(Gens,PopA,PopB,PopC):
    plt.axis([0,Gens,0,276])
    plt.yticks([0,36,70,104,138,172,206,240,276],[0,36,70,104,138,172,206,240,276])
    plt.grid() 
    plt.title('Evolutionary Algorithms')
    plt.xlabel('Generations')
    plt.ylabel('Candidate Weights')
    SumBeg = PopA[0] + PopB[0] + PopC[0]
    SumEnd = PopA[Gens-1] + PopB[Gens-1] + PopC[Gens-1]
    AveBeg = int(SumBeg/3)
    AveEnd = int(SumEnd/3)
    plt.plot([0,Gens],[utils.KNAPWGHT,utils.KNAPWGHT],'red','-')
    for i in range(Gens-1):
        plt.plot([i,i+1],[PopA[i],PopA[i+1]],'green','-')
        plt.plot([i,i+1],[PopB[i],PopB[i+1]],'yellow','-')
        plt.plot([i,i+1],[PopC[i],PopC[i+1]],'blue','-')
        plt.pause(0.01)           
    plt.plot([0,Gens],[AveBeg,AveEnd],'black','-')
    plt.pause(0.01)
    plt.show()

def setUpPlot(Gens):
    plt.axis([0,Gens,0,276])
    plt.yticks([0,36,70,104,138,172,206,240,276],[0,36,70,104,138,172,206,240,276])
    plt.grid() 
    plt.title('Evolutionary Algorithm')
    plt.xlabel('Generations')
    plt.ylabel('Knapsack Weight')
    plt.plot([0,Gens],[utils.KNAPWGHT,utils.KNAPWGHT],'red','-')
    return plt