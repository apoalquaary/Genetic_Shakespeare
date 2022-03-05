'''
/**************************************************************
 *                                                            *
 *                     Done By: ApoAlquaary                   *
 *            Github: https://github.com/ApoAlquaary          *
 *                    Date: 23/10/2021                        *
 * 				   	 			                              *
 *************************************************************/
'''

from dna import DNA
from population import Population


target = "genetic shakespeare problem"
pop_size = 450
mu_ratio = 0.008


if __name__ == "__main__":


    population = Population(target, pop_size, mu_ratio)

    while(1):

        population.selection()
        population.generation()
        population.calculate_fitness()
        population.get_best_score()

        if(population.is_finished):
            break
