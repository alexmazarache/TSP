import os
from Repository import *
import TSP

def createNet():
   
    repo = Repository()
  
    network={}
    network["noNodes"] = repo.get_length()
    network["matrix"] = repo.get_graph()
    return network

def save(c):
    filePath = os.path.join(os.getcwd(),"output.txt")
    fileOutput = open(filePath,"a")

    fileOutput.writelines("Best fitness "+str(c.fitness)+'\n')
    list = c.repres
    l2 = [x+1 for x in list]
    fileOutput.write(str(l2))


def main():
    filePath = os.path.join(os.getcwd(), "easy_01_tsp.txt")
    data = createNet()

    popSize = 100
    generations = 50
    tsp = TSP.TSP(data,popSize)
    tsp.createPop()

    globalC = None
    localC =None
    genCount = 1

    
    while genCount< generations:
        genCount+=1
        tsp.newGeneration()

        localC=tsp.best()

        if globalC is None:
            globalC = localC
        elif globalC.fitness > localC.fitness:
            globalC = localC 
       

        print("------ gen: "+str(genCount)+"--------")
        print("Global: "+str(globalC.fitness))
        print("Local: "+ str(localC.fitness))
       

       
        
    save(globalC)
   
    

main()