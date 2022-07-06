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

#! /usr/bin/python3

"""
Created on Thu Feb 11 08:47:07 2021

@author: jimleon
"""
import Utilities as utils
import Visual as viz

def calcAverageW(PopA,PopB,PopC,index):
    Ave = utils.calculateWeight(PopA[index]) + utils.calculateWeight(PopB[index]) + utils.calculateWeight(PopC[index])
    Ave = Ave/3
    return int(Ave)
    
def main():
    GENS = 500
    t = 0
    PopAp = []
    PopBp = []
    PopCp = []
    PopA = utils.initializePopulation(5)
    PopB = utils.initializePopulation(5)
    PopC = utils.initializePopulation(5)
    Start = calcAverageW(PopA,PopB,PopC,0)
    PopAp.append(utils.calculateWeight(PopA[0]))
    PopBp.append(utils.calculateWeight(PopB[0]))
    PopCp.append(utils.calculateWeight(PopC[0]))
    while t < GENS:
        utils.breedNewMembers(PopA,3)
        utils.breedNewMembers(PopB,3)
        utils.breedNewMembers(PopC,3)
        utils.selection(PopA,10)
        utils.selection(PopB,50)
        utils.selection(PopC,100)
        t = t + 1
        PopAp.append(utils.calculateWeight(PopA[0]))
        PopBp.append(utils.calculateWeight(PopB[0]))
        PopCp.append(utils.calculateWeight(PopC[0]))
    End = calcAverageW(PopA,PopB,PopC,0)
    print("POPULATION A")
    utils.printTopFromPop(PopA,5)
    print('\nPOPULATION B')
    utils.printTopFromPop(PopB,5)
    print('\nPOPULATION C')
    utils.printTopFromPop(PopC,5)
    print("AVERAGE START WEIGHT  :",str(Start))
    print("AVERAGE END WEIGHT  :",str(End))
    viz.plotGeneralTrend(GENS,PopAp,PopBp,PopCp)
    
main()
