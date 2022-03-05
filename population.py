
'''
/**************************************************************
 *                                                            *
 *                     Done By: ApoAlquaary                   *
 *            Github: https://github.com/ApoAlquaary          *
 *                    Date: 23/10/2021                        *
 *								                              *
 *************************************************************/
'''

from dna import DNA
import random

class Population:
    def __init__(self, target, population_size, mutation_ratio) -> None:
        self.target = target
        self.mu_ratio = mutation_ratio
        self.population = []
        for i in range(population_size):
            self.population.append(DNA(target))
        self.matin_pool = []
        self.calculate_fitness()
        self.generations = 0
        self.is_finished = False



    def calculate_fitness(self):
        for indivisual in self.population:
            indivisual.update_fitness(self.target)


    def selection(self):
        self.matin_pool.clear()
        for indivisual in self.population:
            n = int(indivisual.fit_value * 100)
            for j in range(n):
                self.matin_pool.append(indivisual)

    def generation(self):

        for i in range(len(self.population)):
            parents = random.choices(self.matin_pool, k=2)
            child = parents[0].cross_over(parents[1])
            child.mutation(self.mu_ratio)
            self.population[i] = child
        self.generations += 1

    def get_best_score(self):
        best_score = 0
        index = 0
        for i in range(len(self.population)):
            if (best_score < self.population[i].fit_value):
                best_score = self.population[i].fit_value
                index = i
                if(best_score == 1):
                    self.is_finished = True
                    break
        print(f"Generation: {self.generations},  {self.population[index].get_sentance()}")
