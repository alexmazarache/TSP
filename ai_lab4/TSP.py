from random import randint

import Chromosome

class TSP:
    def __init__(self,probParam,popsize):
        self.popSize = popsize
        self.data = probParam
        self.population=[]

    #cream populatie 
    def createPop(self):
        for _ in range(0,self.popSize):
            c = Chromosome.Chromosome(self.data)
            self.population.append(c)
        self.createFit()

    def createFit(self):
        for c in self.population:
            fit = self.getFit(c)
            c.setFitness(fit)

    def getFit(self,c):
        suma = 0.0
        matrix = self.data["matrix"]
        repres = c.repres

        for i in range(0,self.data["noNodes"]-1):
            suma+=matrix[repres[i]][repres[i+1]]
        suma+=matrix[repres[-1]][repres[0]]

        return suma

    def newGeneration(self):
        newGen = []
        for _ in range(self.popSize):
            #selectie
            pos1 = randint(0,self.popSize-1)
            pos2 = randint(0,self.popSize-1)
            c1 = self.population[pos1]
            c2 = self.population[pos2]
            newC1 = c1.crossover(c2)
            newC2 = c2.crossover(c1)
            newC1.mutation()
            newC2.mutation()

            newGen.append(newC1)
            newGen.append(newC2)
        self.population = newGen
        self.createFit()
        self.population.sort(key=lambda c:c.fitness)
        self.population = self.population[:self.popSize]

    def best(self):
        return self.population[0]

