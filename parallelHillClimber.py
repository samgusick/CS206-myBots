from solution import *
import numpy as numpy
from constants import *
import copy

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.nndf")
        self.nextAvailableID = 0
        self.parents = dict()
        for x in range(populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID +=1
            
        
        


    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(numberOfGenerations):
            self.Evolve_For_One_Generation()
    
    def Show_Best(self): 
        best_fit = self.parents[0]
        for x in range (self.parents.__len__()):
            if (best_fit.fitness < self.parents[x].fitness):
                best_fit = self.parents[x]
        best_fit.Start_Simulation("GUI")
        
        
        
        

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    def Spawn(self):
        self.children = dict()

        for x in range (self.parents.__len__()):
            self.children[x] = copy.deepcopy(self.parents[x])
            self.children[x].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Mutate(self):
        for x in range (self.children.__len__()):
            self.children[x].Mutate()

    def Select(self):
        for x in range (self.parents.__len__()):
            if (self.parents[x].fitness < self.children[x].fitness):
                self.parents[x] = self.children[x]

    def Print(self):
        for x in range (self.parents.__len__()):
            print("Parent " + str(x) + ": " + str(self.parents[x].fitness) + " Child " + str(x) + ": " + str(self.children[x].fitness))

    def Evaluate(self, solutions):
        for x in range(solutions.__len__()):
            solutions[x].Start_Simulation("DIRECT")
        
        for x in range(solutions.__len__()):
            solutions[x].Wait_For_Simulation_To_End()
        
        

        